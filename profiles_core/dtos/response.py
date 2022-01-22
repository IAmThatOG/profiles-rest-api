class BaseResponse:
    def __init__(
        self, is_success: bool, message: str, status_code: int, payload: object
    ):
        self.is_success = is_success
        self.message = message
        self.status_code = status_code
        self.payload = payload

    @property
    def JSON(self):
        return self.__dict__
