# decorator pattern

class WebRequest:
    def handle_request(self):
        return "web request"


class BaseDecorator:
    def __init__(self, request):
        self.request = request

    def handle_request(self):
        raise NotImplementedError


class LoggingDecorator(BaseDecorator):
    def handle_request(self):
        return "logging " + self.request.handle_request()


class AuthenticationDecorator(BaseDecorator):
    def handle_request(self):
        return "auth " + self.request.handle_request()


request = WebRequest()
logged_request = LoggingDecorator(request)
auth_request = AuthenticationDecorator(request)
logged_auth_request = LoggingDecorator(AuthenticationDecorator(request))

assert request.handle_request() == "web request"
assert logged_request.handle_request() == "logging web request"
assert auth_request.handle_request() == "auth web request"
assert logged_auth_request.handle_request() == "logging auth web request"
