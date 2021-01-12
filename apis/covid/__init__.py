# from flask import Blueprint, render_template, abort
from flask import Response, request
# covid = Blueprint('covid', __name__ )

from flask_restful import Resource
import numpy as np
import pandas as pd


class CovidAPI(Resource):
    def get(self):
        values = np.random.random(1000)
        print(values)
        movies = {
            'total': list(values)
        }
        return Response(dict(movies), mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        return "asa", 200

