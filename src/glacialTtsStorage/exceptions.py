class GlacialTtsAlreadyExists(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class GlacialTtsFolderIsNotAFolder(Exception):

    def __init__(self, message: str):
        super().__init__(message)
