# factory pattern

class Request:
    def request(self):
        raise NotImplementedError()


class RestApiRequest(Request):
    def request(self):
        return "rest"


class SoapApiRequest(Request):
    def request(self):
        return "soap"


class ApiRequestFactory:
    @staticmethod
    def get_api_request(req_type):
        if req_type == 'rest':
            return RestApiRequest()
        if req_type == 'soap':
            return SoapApiRequest()


api1 = ApiRequestFactory.get_api_request("rest")
api2 = ApiRequestFactory.get_api_request("soap")

assert isinstance(api1, RestApiRequest)
assert isinstance(api2, SoapApiRequest)
assert api1.request() == "rest"
assert api2.request() == "soap"
