# factory pattern

class ApiRequest:
    def request(self):
        raise NotImplementedError


class RestApiRequest(ApiRequest):
    def request(self):
        return "rest"


class SoapApiRequest(ApiRequest):
    def request(self):
        return "soap"


class ApiRequestFactory:
    @staticmethod
    def get_api_request(req_type):
        if req_type == 'rest':
            return RestApiRequest()
        if req_type == 'soap':
            return SoapApiRequest()

        raise ValueError()


api1 = ApiRequestFactory.get_api_request("rest")
api2 = ApiRequestFactory.get_api_request("soap")

assert isinstance(api1, RestApiRequest)
assert isinstance(api2, SoapApiRequest)
assert api1.request() == "rest"
assert api2.request() == "soap"
