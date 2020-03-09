# -*- coding: utf-8 -*-

import os
import pandas as pd
from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation

import matplotlib.pyplot as plt

confirmed_data = pd.read_csv("deaths_20200308.csv")
world_df= pd.DataFrame({'ds': confirmed_data['ds'], 'y': confirmed_data['world']})
china_df= pd.DataFrame({'ds': confirmed_data['ds'], 'y': confirmed_data['china']})
us_df= pd.DataFrame({'ds': confirmed_data['ds'], 'y': confirmed_data['us']})
italy_df= pd.DataFrame({'ds': confirmed_data['ds'], 'y': confirmed_data['italy']})
korea_df= pd.DataFrame({'ds': confirmed_data['ds'], 'y': confirmed_data['korea']})
germany_df= pd.DataFrame({'ds': confirmed_data['ds'], 'y': confirmed_data['germany']})
france_df= pd.DataFrame({'ds': confirmed_data['ds'], 'y': confirmed_data['france']})
japan_df= pd.DataFrame({'ds': confirmed_data['ds'], 'y': confirmed_data['japan']})
iran_df= pd.DataFrame({'ds': confirmed_data['ds'], 'y': confirmed_data['iran']})
uk_df= pd.DataFrame({'ds': confirmed_data['ds'], 'y': confirmed_data['uk']})


# world
world_prophet = Prophet(changepoint_range=0.9, changepoint_prior_scale=0.4)
world_prophet.fit(world_df)

world_future = world_prophet.make_future_dataframe(periods=5)
world_forecast = world_prophet.predict(world_future)

# china
china_prophet = Prophet(changepoint_range=0.9, changepoint_prior_scale=0.4)
china_prophet.fit(china_df)

china_future = china_prophet.make_future_dataframe(periods=5)
china_forecast = china_prophet.predict(china_future)

# us
us_prophet = Prophet(changepoint_range=0.9, changepoint_prior_scale=0.4)
us_prophet.fit(us_df)

us_future = us_prophet.make_future_dataframe(periods=5)
us_forecast = us_prophet.predict(us_future)

# italy
italy_prophet = Prophet(changepoint_range=0.9, changepoint_prior_scale=0.4)
italy_prophet.fit(italy_df)

italy_future = italy_prophet.make_future_dataframe(periods=5)
italy_forecast = italy_prophet.predict(italy_future)

# korea
korea_prophet = Prophet(changepoint_range=0.9, changepoint_prior_scale=0.4)
korea_prophet.fit(korea_df)

korea_future = korea_prophet.make_future_dataframe(periods=5)
korea_forecast = korea_prophet.predict(korea_future)

# germany
germany_prophet = Prophet(changepoint_range=0.9, changepoint_prior_scale=0.4)
germany_prophet.fit(germany_df)

germany_future = germany_prophet.make_future_dataframe(periods=5)
germany_forecast = germany_prophet.predict(germany_future)

# france
france_prophet = Prophet(changepoint_range=0.9, changepoint_prior_scale=0.4)
france_prophet.fit(france_df)

france_future = france_prophet.make_future_dataframe(periods=5)
france_forecast = france_prophet.predict(france_future)

# japan
japan_prophet = Prophet(changepoint_range=0.9, changepoint_prior_scale=0.4)
japan_prophet.fit(japan_df)

japan_future = japan_prophet.make_future_dataframe(periods=5)
japan_forecast = japan_prophet.predict(japan_future)

#iran
iran_prophet = Prophet(changepoint_range=0.9, changepoint_prior_scale=0.4)
iran_prophet.fit(iran_df)

iran_future = iran_prophet.make_future_dataframe(periods=5)
iran_forecast = iran_prophet.predict(iran_future)

# uk
uk_prophet = Prophet(changepoint_range=0.9, changepoint_prior_scale=0.4)
uk_prophet.fit(uk_df)

uk_future = uk_prophet.make_future_dataframe(periods=5)
uk_forecast = uk_prophet.predict(uk_future)


t_df= pd.DataFrame({'date': world_forecast['ds'], 'world': world_forecast['yhat'], \
                    'china': china_forecast['yhat'], 'us': us_forecast['yhat'], 'italy': italy_forecast['yhat'],\
                    'korea': korea_forecast['yhat'], 'germany': germany_forecast['yhat'], 'france': france_forecast['yhat'], \
                    'japan': japan_forecast['yhat'], 'iran': iran_forecast['yhat'], 'uk': uk_forecast['yhat'] }).tail(10)
t_df.to_csv('deaths_result.csv')

