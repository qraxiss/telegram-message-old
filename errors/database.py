class NoOperationsError(Exception):
    status = 404
    def __init__(self, msg='The document you requested cannot be accessed or does not exist.', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)