# factory pattern









api1 = ApiRequestFactory.get_api_request("rest")
api2 = ApiRequestFactory.get_api_request("soap")

assert isinstance(api1, RestApiRequest)
assert isinstance(api2, SoapApiRequest)
assert api1.request() == "rest"
assert api2.request() == "soap"
