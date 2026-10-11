# Quant Research Notebooks

Quantitative finance research notebooks, one folder per topic.

## Topics

- **Backtest Overfitting: the Deflated Sharpe Ratio and PBO** — [notebook](BacktestOverfitting/BacktestOverfitting.ipynb) · [PDF](BacktestOverfitting/BacktestOverfitting.pdf)
- **Backtesting Value-at-Risk Models through Crises: Bitcoin, Ether and the S&P 500** — [notebook](VaRBacktest/VaRBacktest.ipynb) · [PDF](VaRBacktest/VaRBacktest.pdf)
- **CDO Tranches and Default Correlation: Why "AAA" Failed in 2008** — [notebook](CDOTranche/CDOTranche.ipynb) · [PDF](CDOTranche/CDOTranche.pdf)
- **Correlation Breakdown in Stressed Markets: Is Crypto Contagion Real?** — [notebook](CorrelationBreakdown/CorrelationBreakdown.ipynb) · [PDF](CorrelationBreakdown/CorrelationBreakdown.pdf)
- **Delta Hedging: Where an Option Dealer's P&L Really Comes From** — [notebook](DeltaHedging/DeltaHedging.ipynb) · [PDF](DeltaHedging/DeltaHedging.pdf)
- **GARCH Volatility Forecasting and Volatility Targeting for Bitcoin and Ether** — [notebook](VolTargeting/VolTargeting.ipynb) · [PDF](VolTargeting/VolTargeting.pdf)
- **Hierarchical Risk Parity vs Mean-Variance vs 1/N** — [notebook](HierarchicalRiskParity/HierarchicalRiskParity.ipynb) · [PDF](HierarchicalRiskParity/HierarchicalRiskParity.pdf)
- **Mean-Variance Portfolio Optimization with Real Crypto Data** — [notebook](MeanVariance/MeanVariance.ipynb) · [PDF](MeanVariance/MeanVariance.pdf)
- **The Merton Model: Reading Default Risk from Stock Prices** — [notebook](MertonCredit/MertonCredit.ipynb) · [PDF](MertonCredit/MertonCredit.pdf)

## Setup

Notebooks that use crypto prices download them with `src/data.py` (`pip install ccxt pandas`). Other dependencies: numpy, pandas, scipy, matplotlib, scikit-learn, yfinance.
