from apis.covid.functions import CovidDeaths, Test


def initialize_routes(api):
    api.add_resource(CovidDeaths, '/covid')
    api.add_resource(Test, '/')
