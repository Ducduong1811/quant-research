# References — Backtest Overfitting: Deflated Sharpe Ratio and PBO

Source module: WQU MScFE 560, Module 6 (Model Failure and Crises), Lesson 4 "More than one way to pick a stock" (technical analysis, momentum, behavioural biases). Also Module 5 Lesson 2 (valuation challenges and model risk).

## Core papers
1. Bailey, D. H., López de Prado, M. (2014). *The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality.* Journal of Portfolio Management 40(5). SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2460551
   Slides/PDF: https://pdfs.semanticscholar.org/c215/d0a2064ce1a3565d276475abc84305418f0f.pdf
   PSR, the expected maximum Sharpe ratio across N trials, DSR, and the worked example (annual SR 2.5, N=100 → DSR ≈ 0.90).
2. Bailey, D. H., Borwein, J. M., López de Prado, M., Zhu, Q. J. (2017). *The Probability of Backtest Overfitting.* Journal of Computational Finance 20(4). PDF: https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf
   The CSCV algorithm, the logit of the OOS rank, PBO, and performance degradation.
3. Bailey, D. H., Borwein, J. M., López de Prado, M., Zhu, Q. J. (2014). *Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance.* Notices of the AMS 61(5). https://www.ams.org/notices/201405/rnoti-p458.pdf
4. Bailey, D. H. et al. *Statistical Overfitting and Backtest Performance.* https://sdm.lbl.gov/oapapers/ssrn-id2507040-bailey.pdf
5. Harvey, C. R., Liu, Y. (2015). *Backtesting.* Journal of Portfolio Management 42(1). SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2345489
   Haircut Sharpe ratios under multiple testing.
6. Lo, A. W. (2002). *The Statistics of Sharpe Ratios.* Financial Analysts Journal 58(4). https://doi.org/10.2469/faj.v58.n4.2453

## Course required reading (Module 6, Lesson 4)
7. de Souza, M. J. S. et al. (2018). *Examination of the profitability of technical analysis based on moving average strategies in BRICS.* Financial Innovation 4(3). https://jfin-swufe.springeropen.com/articles/10.1186/s40854-018-0087-z
   MA-crossover rules, the strategy family whose parameter grid is searched here.
8. Drakopoulou, V. (2016). *A Review of Fundamental and Technical Stock Analysis Techniques.* Journal of Stock & Forex Trading 5(1).
9. Arratia, A. et al. (2021). *Sentiment Analysis of Financial News: Mechanics and Statistics.* In Data Science for Economics and Finance, Springer. https://link.springer.com/chapter/10.1007/978-3-030-66891-4_9

## Implementations
10. pypbo (Python): https://github.com/esvhd/pypbo. PBO, DSR, PSR, minimum track record length.
11. Kodezilla0725/deflated-sharpe: https://github.com/Kodezilla0725/deflated-sharpe. Reproduces both papers to four decimals and lists errata.
12. iqueipopg/backtest-overfitting: https://github.com/iqueipopg/backtest-overfitting. DSR + CSCV on a 147-trial strategy zoo on SPY.
13. WatchTree-19/overfit: https://github.com/WatchTree-19/overfit. Notes that V[SR] must be the variance of Sharpe estimates across trials, not of returns.
14. jarvisss007/backtest-overfitting: https://github.com/jarvisss007/backtest-overfitting. Includes minimum backtest length.
