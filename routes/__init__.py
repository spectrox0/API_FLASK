from apis.covid import CovidAPI


def initialize_routes(api):
    api.add_resource(CovidAPI, '/covid')
