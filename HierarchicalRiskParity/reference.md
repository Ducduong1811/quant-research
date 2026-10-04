# References — Hierarchical Risk Parity vs Mean-Variance vs 1/N

Source module: WQU MScFE 560, Module 3 (Correlation). Notes covered: portfolio return/volatility, correlation and diversification, correlations changing in stressed markets.

## Core papers
1. López de Prado, M. (2016). *Building Diversified Portfolios that Outperform Out-of-Sample.* Journal of Portfolio Management 42(4). SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2708678
   The original HRP paper: tree clustering, quasi-diagonalization, recursive bisection, and a Monte Carlo comparison against CLA and IVP.
2. DeMiguel, V., Garlappi, L., Uppal, R. (2009). *Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?* Review of Financial Studies 22(5). https://doi.org/10.1093/rfs/hhm075
   Why estimated mean-variance portfolios often lose to 1/N out-of-sample.
3. Ledoit, O., Wolf, M. (2004). *Honey, I Shrunk the Sample Covariance Matrix.* Journal of Portfolio Management 30(4). http://www.ledoit.net/honey.pdf
   Covariance shrinkage, used here so the minimum-variance benchmark is fair.

## Course required reading (Module 3)
4. Loretan, M., English, W. B. (2000). *Evaluating Changes in Correlations during Periods of High Market Volatility.* BIS Quarterly Review. https://www.bis.org/publ/r_qt0006e.pdf
   Correlations appear to rise when volatility rises, which is the stress regime HRP is supposed to handle.
5. *Financial Management* (open textbook), Michigan State University, 2021. https://openbooks.lib.msu.edu/financialmanagement/
   Portfolio return, variance and Sharpe ratio basics.
6. Diez, Çetinkaya-Rundel, Barr. *OpenIntro Statistics.* https://www.openintro.org/book/os/
   Correlation and covariance.

## Explanations & implementations
7. Wikipedia: *Hierarchical Risk Parity.* https://en.wikipedia.org/wiki/Hierarchical_Risk_Parity
   Algorithm steps, the distance metric d = sqrt((1-ρ)/2), and the split factor α = 1 − V₁/(V₁+V₂).
8. PyPortfolioOpt: *Other Optimizers (HRPOpt).* https://pyportfolioopt.readthedocs.io/en/latest/OtherOptimizers.html
   Reference implementation (default single linkage), adapted from López de Prado's code.
9. Riskfolio-Lib HRP tutorial (Medium). https://medium.com/@orenji.eirl/hierarchical-risk-parity-with-python-and-riskfolio-lib-c0e60b94252e
10. NVIDIA Technical Blog: *Hierarchical Risk Parity on RAPIDS.* https://developer.nvidia.com/blog/hierarchical-risk-parity-on-rapids-an-ml-approach-to-portfolio-allocation/
11. Quantopian forum: *HRP: Comparing various Portfolio Diversification Techniques.* https://www.quantopian.com/posts/hierarchical-risk-parity-comparing-various-portfolio-diversification-techniques

## Critical / follow-up evidence
12. *Hierarchical risk parity: Efficient implementation and real world analysis* (2025). Future Generation Computer Systems. https://www.sciencedirect.com/science/article/abs/pii/S0167739X25000391
    Real-data study reporting that 1/N often matches or beats HRP on risk-adjusted return.
13. *Schur Complementary Allocation: A Unification of HRP and Minimum Variance Portfolios* (2024). arXiv:2411.05807. https://arxiv.org/pdf/2411.05807
14. *Machine Learning Portfolio Optimization: HRP and Modern Portfolio Theory* (ResearchGate). https://www.researchgate.net/publication/342178924
