# Weighted decision curve analysis

Analytic workflows that support two case studies and simulations estimating the impact of weighting preferences in a decision curve analysis (DCA).

# Citation

Weissman GE and Faraji Z. When does a decision curve analysis benefit from an explicit quantification of end-user preferences?: A case report and simulation study. 2023. *Under Review*

```
@article{weissman_dca_2023,
  author   = "Weissman, Gary E and Faraji, Zahra",
  title    = "When does a decision curve analysis benefit from an explicit quantification of end-user preferences?: A case report and simulation study",
  journal  = "Under Reivew",
  year     = 2023,
  volume   = "X",
  number   = "X",
  pages    = "X",
}
```

# Explanation of files

* 00_nlst_data_preprocess.py - This file preprocess the data for NLST case study by creating new features and dropping unwanted features. The final output is saved as a cvs file and laoded in the 03_nlst_netbenefit.Rmd file for further processing and modeling. 

* 01_hirid_netbenefit.Rmd - This file is using the HIRID case study to build prediction models (Elastic Net, XGBoost, Naive Bayes) and visualize the DCA plot for various weights. The predicted probabilities of the models are saved in the output folder. The performance and DCA plots are saved in the exhibit folder. 
* 01_hirid_netbenefit.html - this file is the output of 01_hirid_netbenefit.Rmd in the HTML format which includes the plots and results. 

* 02_hirid_extra_analysis.Rmd  - This file loads the predicted probabilities from the HIRID models and generates performance measures.
* 02_hirid_extra_analysis.html- This file is the output of 02_hirid_extra_analysis.Rmd in the HTML format which includes the plots and results. 

* 03_nlst_netbenefit.Rmd - This file is using the NLST case study to build prediction models (Elastic Net, XGBoost, Naive Bayes) and visualize the DCA plot for various weights. The predicted probabilities of the models are saved in the output folder. The performance and DCA plots are saved in the exhibit folder. 
* 03_nlst_netbenefit.html - this file is the output of 03_nlst_netbenefit.Rmd in the HTML format which includes the plots and results. 

* 05_fig_perf_comb.Rmd - This file creates a combined performance plot for both case studies which shows the calibration and precision-recall plots together. 
* 05_fig_perf_comb.html - this file is the output of 05_fig_perf_comb.Rmd in the HTML format which includes the plots and results. 

* runall.sh - This is a bash script to run and compile everything at once. 

# Dependencies

This repository needs R, Python,and Rmarkdown. The required packages/libraries are listed at the top of each script. 
