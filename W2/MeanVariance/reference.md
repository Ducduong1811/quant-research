# References — Mean-Variance Portfolio Optimization

## Core papers
1. Markowitz, H. (1952). *Portfolio Selection.* Journal of Finance 7(1), 77–91. https://doi.org/10.2307/2975974
   The original mean-variance framework: investors trade off expected return against variance, and diversification depends on covariances.
2. Tobin, J. (1958). *Liquidity Preference as Behavior Towards Risk.* Review of Economic Studies 25(2), 65–86. https://doi.org/10.2307/2296205
   Separation theorem: with a risk-free asset, every investor holds the same risky (tangency) portfolio.
3. Merton, R. C. (1972). *An Analytic Derivation of the Efficient Portfolio Frontier.* Journal of Financial and Quantitative Analysis 7(4), 1851–1872. https://doi.org/10.2307/2329621
   The closed-form frontier with the A, B, C, D constants used in Section 6.

## Estimation error
4. Michaud, R. O. (1989). *The Markowitz Optimization Enigma: Is 'Optimized' Optimal?* Financial Analysts Journal 45(1), 31–42. https://doi.org/10.2469/faj.v45.n1.31
   Mean-variance optimizers as "estimation-error maximizers"; motivates the bootstrap in Section 7.
5. DeMiguel, V., Garlappi, L., Uppal, R. (2009). *Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?* Review of Financial Studies 22(5), 1915–1953. https://doi.org/10.1093/rfs/hhm075
   Estimated mean-variance portfolios often fail to beat 1/N out-of-sample; the benchmark in Section 8.
6. Ledoit, O., Wolf, M. (2004). *Honey, I Shrunk the Sample Covariance Matrix.* Journal of Portfolio Management 30(4). http://www.ledoit.net/honey.pdf
   Covariance shrinkage, one remedy for estimation error.
7. Black, F., Litterman, R. (1992). *Global Portfolio Optimization.* Financial Analysts Journal 48(5), 28–43. https://doi.org/10.2469/faj.v48.n5.28
   Replaces raw historical means with equilibrium returns blended with investor views.

## Explanations & implementations
8. Wikipedia: *Modern Portfolio Theory.* https://en.wikipedia.org/wiki/Modern_portfolio_theory
9. PyPortfolioOpt documentation: *Mean-Variance Optimization.* https://pyportfolioopt.readthedocs.io/en/latest/MeanVariance.html
10. Riskfolio-Lib documentation. https://riskfolio-lib.readthedocs.io/

## Data
11. ccxt — cryptocurrency exchange trading library, used by `src/data.py` to download Binance daily OHLCV. https://github.com/ccxt/ccxt
