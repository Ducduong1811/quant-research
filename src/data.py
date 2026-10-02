#!/usr/bin/env python3
"""
Download historical OHLCV candles for cryptocurrencies from any exchange that
ccxt supports, and save one CSV per symbol.

Usage:
    python data.py BTC/USDT
    python data.py BTC/USDT ETH/USDT SOL/USDT --timeframe 1h --since 2024-01-01
    python data.py BTC/USDT --exchange okx --until 2025-01-01
    python data.py --list-timeframes --exchange bybit

Re-running for the same symbol/timeframe only downloads candles newer than the
last row already in the CSV, so it doubles as an updater.

Output: <out>/<EXCHANGE>_<BASE>-<QUOTE>_<timeframe>.csv with columns
Date, Open, High, Low, Close, Volume (UTC) — the format backtesting.py reads.

Requires: pip install ccxt pandas
"""

import argparse
import sys
import time
from pathlib import Path

import ccxt
import pandas as pd

COLUMNS = ["Date", "Open", "High", "Low", "Close", "Volume"]


def make_exchange(name: str) -> ccxt.Exchange:
    if name not in ccxt.exchanges:
        sys.exit(f"Error: unknown exchange '{name}'. See ccxt.exchanges for the list.")
    exchange = getattr(ccxt, name)({"enableRateLimit": True})
    if not exchange.has.get("fetchOHLCV"):
        sys.exit(f"Error: {name} does not provide OHLCV history")
    return exchange


def to_ms(date: str | None) -> int | None:
    return int(pd.Timestamp(date, tz="UTC").timestamp() * 1000) if date else None


def fetch_range(exchange: ccxt.Exchange, symbol: str, timeframe: str,
                since: int, until: int | None, limit: int) -> list[list]:
    """Page forward from `since` until `until` (or now), one request per page."""
    step = exchange.parse_timeframe(timeframe) * 1000
    end = until or exchange.milliseconds()
    rows: list[list] = []
    cursor = since
    while cursor < end:
        for attempt in range(5):
            try:
                batch = exchange.fetch_ohlcv(symbol, timeframe, since=cursor, limit=limit)
                break
            except (ccxt.NetworkError, ccxt.RateLimitExceeded) as e:
                wait = 2 ** attempt
                print(f"    {type(e).__name__}, retrying in {wait}s…")
                time.sleep(wait)
        else:
            sys.exit(f"Error: giving up on {symbol} after 5 failed requests")

        if not batch:
            # No candles here (e.g. before the listing date): jump ahead one page.
            cursor += step * limit
            continue
        rows.extend(r for r in batch if r[0] < end)
        print(f"    {len(rows):>7} candles, up to {pd.Timestamp(batch[-1][0], unit='ms')}")
        next_cursor = batch[-1][0] + step
        if next_cursor <= cursor:
            break
        cursor = next_cursor
    return rows


def output_path(out_dir: Path, exchange: str, symbol: str, timeframe: str) -> Path:
    safe = symbol.replace("/", "-").replace(":", "-")
    return out_dir / f"{exchange.upper()}_{safe}_{timeframe}.csv"


def fetch_symbol(exchange: ccxt.Exchange, symbol: str, args) -> None:
    path = output_path(args.out, exchange.id, symbol, args.timeframe)
    existing = None
    since = to_ms(args.since)

    if path.exists() and not args.full:
        existing = pd.read_csv(path, parse_dates=["Date"])
        if not existing.empty:
            last = int(existing["Date"].iloc[-1].tz_localize("UTC").timestamp() * 1000)
            since = last + exchange.parse_timeframe(args.timeframe) * 1000
            print(f"  {symbol}: updating {path.name} from {pd.Timestamp(since, unit='ms')}")
    if existing is None:
        print(f"  {symbol}: downloading from {pd.Timestamp(since, unit='ms')}")

    rows = fetch_range(exchange, symbol, args.timeframe, since, to_ms(args.until), args.limit)

    # Drop the still-forming candle so saved data never changes after the fact.
    now = exchange.milliseconds()
    step = exchange.parse_timeframe(args.timeframe) * 1000
    rows = [r for r in rows if r[0] + step <= now]

    new = pd.DataFrame(rows, columns=COLUMNS)
    new["Date"] = pd.to_datetime(new["Date"], unit="ms")
    df = pd.concat([existing, new]) if existing is not None else new
    df = df.drop_duplicates("Date").sort_values("Date")

    if df.empty:
        print(f"  {symbol}: no candles returned")
        return
    df.to_csv(path, index=False)
    print(f"  {symbol}: saved {len(df)} candles ({len(new)} new) "
          f"{df['Date'].iloc[0]} → {df['Date'].iloc[-1]} → {path}")


def main():
    parser = argparse.ArgumentParser(description="Download crypto OHLCV history to CSV")
    parser.add_argument("symbols", nargs="*", help="Market symbols, e.g. BTC/USDT ETH/USDT")
    parser.add_argument("--exchange", default="binance", help="Any ccxt exchange id (default: binance)")
    parser.add_argument("--timeframe", default="1d", help="Candle size, e.g. 1m 5m 1h 4h 1d 1w")
    parser.add_argument("--since", default="2017-01-01", help="Start date (UTC), default 2017-01-01")
    parser.add_argument("--until", default=None, help="End date (UTC, exclusive), default now")
    parser.add_argument("--out", type=Path, default=Path(__file__).parent / "data",
                        help="Output folder (default: src/data)")
    parser.add_argument("--limit", type=int, default=1000, help="Candles per request")
    parser.add_argument("--full", action="store_true", help="Ignore existing CSVs and re-download")
    parser.add_argument("--list-timeframes", action="store_true")
    args = parser.parse_args()

    exchange = make_exchange(args.exchange)

    if args.list_timeframes:
        print(" ".join(exchange.timeframes or {}) or "Exchange does not list timeframes")
        return
    if not args.symbols:
        parser.error("give at least one symbol, e.g. BTC/USDT")

    if exchange.timeframes and args.timeframe not in exchange.timeframes:
        sys.exit(f"Error: {exchange.id} has no '{args.timeframe}' timeframe. "
                 f"Options: {' '.join(exchange.timeframes)}")

    exchange.load_markets()
    missing = [s for s in args.symbols if s not in exchange.markets]
    if missing:
        sys.exit(f"Error: not listed on {exchange.id}: {', '.join(missing)}")

    args.out.mkdir(parents=True, exist_ok=True)
    print(f"{exchange.id} · {args.timeframe} · {len(args.symbols)} symbol(s)")
    for symbol in args.symbols:
        fetch_symbol(exchange, symbol, args)


if __name__ == "__main__":
    main()
