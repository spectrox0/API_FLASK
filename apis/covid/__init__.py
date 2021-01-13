# from flask import Blueprint, render_template, abort
from flask import Response, request
# covid = Blueprint('covid', __name__ )

from flask_restful import Resource
import numpy as np
import pandas as pd
from apis.constants import base_url_api_covid

confirmed_cases_data_url = base_url_api_covid + 'time_series_covid19_confirmed_global.csv'
death_cases_data_url = base_url_api_covid + 'time_series_covid19_deaths_global.csv'
recovery_cases_data_url = base_url_api_covid + 'time_series_covid19_recovered_global.csv'


def convert_dataframe(raw_data, list_countries=None, days=30):
    if list_countries is None:
        list_countries = ['Venezuela', 'Colombia', 'Argentina', 'Uruguay', 'Brazil', 'Chile', 'Ecuador', 'Peru',
                          'Mexico', 'Spain']

    df = raw_data.groupby('Country/Region').sum().drop(['Lat', 'Long'], axis=1).transpose()
    df.set_index(pd.DatetimeIndex(df.index), inplace=True)
    return df[list_countries].last(f'{days}D')


class Test(Resource):
    def get(self):
        return {"Hola": 'as'}


class CovidDeaths(Resource):
    def get(self):
        # Import datasets as pandas dataframes
        raw_data_confirmed = pd.read_csv(confirmed_cases_data_url)
        raw_data_deaths = pd.read_csv(death_cases_data_url)
        raw_data_recovered = pd.read_csv(recovery_cases_data_url)

        confirmed = convert_dataframe(raw_data_confirmed)
        deaths = convert_dataframe(raw_data_deaths)
        recovered = convert_dataframe(raw_data_recovered)

        response = {
            'confirmed': confirmed.to_json(),
            'deaths': deaths.to_json(),
            'recovered': recovered.to_json()
        }
        return response

    def post(self):
        body = request.get_json()
        return "asa", 200
