# decorator pattern









request = WebRequest()
logged_request = LoggingDecorator(request)
auth_request = AuthenticationDecorator(request)
logged_auth_request = LoggingDecorator(AuthenticationDecorator(request))

assert request.handle_request() == "web request"
assert logged_request.handle_request() == "logging web request"
assert auth_request.handle_request() == "auth web request"
assert logged_auth_request.handle_request() == "logging auth web request"