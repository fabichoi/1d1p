# factory pattern

class ApiRequestFactory:
    @staticmethod
    def get_api_request(req_type):
        if req_type == 'rest':
            return RestApiRequest()
        if req_type == 'soap':
            return SoapApiRequest()

        raise ValueError


class BaseApiRequest:
    def request(self):
        raise NotImplementedError


class RestApiRequest(BaseApiRequest):
    def request(self):
        return "rest"


class SoapApiRequest(BaseApiRequest):
    def request(self):
        return "soap"


api1 = ApiRequestFactory.get_api_request("rest")
api2 = ApiRequestFactory.get_api_request("soap")

assert isinstance(api1, RestApiRequest)
assert isinstance(api2, SoapApiRequest)
assert api1.request() == "rest"
assert api2.request() == "soap"
