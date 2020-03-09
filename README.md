
2019 Novel Coronavirus COVID-19 (2019-nCoV) Prediction by using data analytics
============================================

## This is the data and modeling repository for the Coronaprediction website

## Website: http://www.coronaprediction.com

## Data source:

* Johns hopkins university: https://github.com/CSSEGISandData/COVID-19#2019-novel-coronavirus-covid-19-2019-ncov-data-repository-by-johns-hopkins-csse
* World Health Organization (WHO): https://www.who.int/
* DXY.cn. Pneumonia. 2020. http://3g.dxy.cn/newh5/view/pneumonia.
* BNO News: https://bnonews.com/index.php/2020/02/the-latest-coronavirus-cases/
* National Health Commission of the People’s Republic of China (NHC):
* http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml
* China CDC (CCDC): http://weekly.chinacdc.cn/news/TrackingtheEpidemic.htm
* Hong Kong Department of Health: https://www.chp.gov.hk/en/features/102465.html
* Macau Government: https://www.ssm.gov.mo/portal/
* Taiwan CDC: https://sites.google.com/cdc.gov.tw/2019ncov/taiwan?authuser=0
* US CDC: https://www.cdc.gov/coronavirus/2019-ncov/index.html
* Government of Canada: https://www.canada.ca/en/public-health/services/diseases/coronavirus.html
* Australia Government Department of Health: https://www.health.gov.au/news/coronavirus-update-at-a-glance
* European Centre for Disease Prevention and Control (ECDC): https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases
* Ministry of Health Singapore (MOH): https://www.moh.gov.sg/covid-19
* Italy Ministry of Health: http://www.salute.gov.it/nuovocoronavirus

## Modeling idea:

I got an idea that Spreading virus looks like a social network. The virus is spreading from person-to-person like SNS does.
So I thought that prophet algoritms from Facebook could be useful to predict the future trends.
According to Facebook, Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects.
But, there are a few wrong prediction data that are less than former number. These numbers are replace by median number.

## Hope:

I hope the website helps people to guess the number of confirmed cases, recovered patients, and death toll in order to make effective ways to prevent COVID-19 Spread in Communities.

## Terms of Use:

This GitHub repo and its contents herein, including all data, mapping, and analysis, copyright 2020 HAM HO-SIK, all rights reserved, is provided to the public strictly for educational and academic research purposes. The Website relies upon publicly available data from multiple sources, that do not always agree. The website hereby disclaims any and all representations and warranties with respect to the Website, including accuracy, fitness for use, and merchantability. Reliance on the Website for medical guidance or use of the Website in commerce is strictly prohibited.
(Similar to the git repo of JHU: https://github.com/CSSEGISandData/COVID-19#2019-novel-coronavirus-covid-19-2019-ncov-data-repository-by-johns-hopkins-csse)
