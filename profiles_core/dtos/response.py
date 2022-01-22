class BaseResponse:
    def __init__(self, *args, **kwargs):
        self.is_success = kwargs["is_success"]
        self.message = kwargs["message"]
        self.status_code = kwargs["status_code"]
        self.payload = kwargs["payload"]

    @property
    def JSON(self):
        return self.__dict__
