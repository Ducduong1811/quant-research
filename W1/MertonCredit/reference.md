# References — Merton Structural Credit Model

Source modules: WQU MScFE 560, Module 1 (Credit Risk and Financing), Module 4 Lesson 3 (Home equity as an option), Module 5 Lesson 3 (Liquidity and the credit market: probability of default, credit spreads), Module 6 Lesson 1 (The balance sheet: leverage and default, where equity is a call option on assets).

## Core papers
1. Merton, R. C. (1974). *On the Pricing of Corporate Debt: The Risk Structure of Interest Rates.* Journal of Finance 29(2), 449–470. https://doi.org/10.1111/j.1540-6261.1974.tb03058.x
   Equity as a European call on firm assets, and risky debt as risk-free debt minus a put.
2. Crosbie, P., Bohn, J. (2003). *Modeling Default Risk.* Moody's KMV. https://www.moodysanalytics.com/-/media/whitepaper/before-2011/12-18-03-modeling-default-risk.pdf
   KMV default point (short-term debt + ½ long-term debt), distance to default, EDF mapping.
3. Vassalou, M., Xing, Y. (2004). *Default Risk in Equity Returns.* Journal of Finance 59(2). https://doi.org/10.1111/j.1540-6261.2004.00650.x
   The iterative estimation procedure on daily equity values.
4. Bharath, S. T., Shumway, T. (2008). *Forecasting Default with the Merton Distance to Default Model.* Review of Financial Studies 21(3). https://doi.org/10.1093/rfs/hhn044
   The "naive" DD that skips the iteration and forecasts about as well.
5. Jones, E. P., Mason, S. P., Rosenfeld, E. (1984). *Contingent Claims Analysis of Corporate Capital Structures: An Empirical Investigation.* Journal of Finance 39(3). https://doi.org/10.1111/j.1540-6261.1984.tb03890.x
   The two-equation (E, σ_E) solution and early evidence that Merton spreads are too low.

## Course required reading
6. Foote, C. L., Willen, P. (2017). *Mortgage-Default Research and the Recent Foreclosure Crisis.* FRB Boston WP 17-3. https://www.bostonfed.org/publications/research-department-working-paper/2017/mortgage-default-research-and-the-recent-foreclosure-crisis.aspx
   Negative equity as the option-theoretic trigger for default (M6 L1).
7. Solomon, D. (2011). *Non-Recourse, No Down Payment and the Mortgage Meltdown.* Fordham Journal of Corporate & Financial Law 16(3). https://ir.lawnet.fordham.edu/jcfl/vol16/iss3/4/
   Limited liability and non-recourse make equity a call option (M4 L3).
8. Misankova, M. et al. (2015). *Determination of Default Probability by Loss Given Default.* Procedia Economics and Finance 26. https://www.sciencedirect.com/science/article/pii/S2212567115008151
   PD, LGD and their link to the credit spread (M5 L2).
9. TU Delft OCW. *Introduction to Credit Risk Management.* https://ocw.tudelft.nl/courses/introduction-credit-risk-management/

## Tutorials & implementations
10. Gao, M. *Estimate Merton Distance-to-Default.* https://mingze-gao.com/posts/merton-dd/
    Step-by-step iterative algorithm, convergence tolerance 1e-3, and the Bharath-Shumway naive DD.
11. Christoffersen, B. (2020). *DtD: Distance to Default* (R package vignette). https://cran.r-project.org/web/packages/DtD/vignettes/Distance-to-default.pdf
    Compares the iterative KMV method with MLE; shows the iterative method equals MLE up to a Jacobian term.
12. Tetereva, A. (2012). *Distance-to-Default (According to KMV model).* http://home.lu.lv/~valeinis/lv/seminars/Tetereva_05042012.pdf
13. mariatejedorg/credit-risk-merton-model (GitHub). https://github.com/mariatejedorg/credit-risk-merton-model
    Ford example with yfinance data and Newton-Raphson inversion.
14. Wikipedia: *Merton model.* https://en.wikipedia.org/wiki/Merton_model
15. Huang, J.-Z., Huang, M. (2012). *How Much of the Corporate-Treasury Yield Spread Is Due to Credit Risk?* Review of Asset Pricing Studies 2(2). https://doi.org/10.1093/rapstu/ras011
    The "credit spread puzzle": structural models under-predict investment-grade spreads.
