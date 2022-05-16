class ServiceUnavailable(Exception):
    def __init__(self, message="api service unavailable"):
        super().__init__(message)
