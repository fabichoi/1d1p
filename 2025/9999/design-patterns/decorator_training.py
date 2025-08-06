# decorator pattern

class WebRequest:
    def handle_request(self):
        return "web request"


class RequestDecorator:
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def handle_request(self):
        return self._wrapped.handle_request()


class LoggingDecorator(RequestDecorator):
    def handle_request(self):
        return "logging " + super().handle_request()


class AuthenticationDecorator(RequestDecorator):
    def handle_request(self):
        return "auth " + super().handle_request()


request = WebRequest()
logged_request = LoggingDecorator(request)
auth_request = AuthenticationDecorator(request)
logged_auth_request = LoggingDecorator(AuthenticationDecorator(request))

assert request.handle_request() == "web request"
assert logged_request.handle_request() == "logging web request"
assert auth_request.handle_request() == "auth web request"
assert logged_auth_request.handle_request() == "logging auth web request"
