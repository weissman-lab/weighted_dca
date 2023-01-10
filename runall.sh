#!/bin/bash

start=$SECONDS

echo Doing NLST_Pre_processing...
python3 00_nlst_data_preprocess.py > log/00_nlst_data_preprocess.log

echo Running HIRID stuff...
R --vanilla -e  "rmarkdown::render('01_hirid_netbenefit.Rmd')" > log/01_hirid_netbenefit.log

R --vanilla -e  "rmarkdown::render('02_hirid_extra_analysis.Rmd')" > log/02_hirid_extras_analysis.log


echo Doing NLST stuff...
R --vanilla -e  "rmarkdown::render('03_nlst_netbenefit.Rmd')" > log/03_nlst_netbenefit.log
R --vanilla -e  "rmarkdown::render('04_nlst_extra_analysis.Rmd')" > log/04_nlst_extra_analysis.log

echo Doing fig_perf_comb stuff...
R --vanilla -e  "rmarkdown::render('05_fig_perf_comb.Rmd')" > log/05_fig_perf_comb.log


echo All done!

end=$SECONDS
echo "Script completed in: $((end-start)) seconds."
echo "Script completed in: $((end-start)) seconds." > log/time.log
