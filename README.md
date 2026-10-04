# Quant Research Notebooks

Quantitative finance research notebooks, one folder per topic.

## Topics

- **Backtest Overfitting: the Deflated Sharpe Ratio and PBO** — [notebook](BacktestOverfitting/BacktestOverfitting.ipynb) · [PDF](BacktestOverfitting/BacktestOverfitting.pdf)
- **Correlation Breakdown in Stressed Markets: Is Crypto Contagion Real?** — [notebook](CorrelationBreakdown/CorrelationBreakdown.ipynb) · [PDF](CorrelationBreakdown/CorrelationBreakdown.pdf)
- **Hierarchical Risk Parity vs Mean-Variance vs 1/N** — [notebook](HierarchicalRiskParity/HierarchicalRiskParity.ipynb) · [PDF](HierarchicalRiskParity/HierarchicalRiskParity.pdf)
- **Mean-Variance Portfolio Optimization with Real Crypto Data** — [notebook](MeanVariance/MeanVariance.ipynb) · [PDF](MeanVariance/MeanVariance.pdf)
- **The Merton Model: Reading Default Risk from Stock Prices** — [notebook](MertonCredit/MertonCredit.ipynb) · [PDF](MertonCredit/MertonCredit.pdf)
- **GARCH Volatility Forecasting and Volatility Targeting for Bitcoin and Ether** — [notebook](VolTargeting/VolTargeting.ipynb) · [PDF](VolTargeting/VolTargeting.pdf)

## Setup

Notebooks that use crypto prices download them with `src/data.py` (`pip install ccxt pandas`). Other dependencies: numpy, pandas, scipy, matplotlib, scikit-learn, yfinance.
