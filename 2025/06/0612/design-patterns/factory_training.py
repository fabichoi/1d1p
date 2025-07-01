# factory pattern

class ApiRequestFactory:
    @staticmethod
    def get_api_request(method):
        if method == "rest":
            return RestApiRequest()
        if method == "soap":
            return SoapApiRequest()
        raise ValueError()


class ApiRequest:
    def request(self):
        raise NotImplementedError


class RestApiRequest(ApiRequest):
    def request(self):
        return "rest"


class SoapApiRequest(ApiRequest):
    def request(self):
        return "soap"


api1 = ApiRequestFactory.get_api_request("rest")
api2 = ApiRequestFactory.get_api_request("soap")

assert isinstance(api1, RestApiRequest)
assert isinstance(api2, SoapApiRequest)
assert api1.request() == "rest"
assert api2.request() == "soap"
