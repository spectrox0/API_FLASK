from apis.covid import CovidDeaths
from apis.covid import Test


def initialize_routes(api):
    api.add_resource(CovidDeaths, '/covid')
    api.add_resource(Test, '/')
