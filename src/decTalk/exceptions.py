class DecTalkExecutableIsMissingException(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class DecTalkFailedToGenerateSpeechFileException(Exception):

    def __init__(self, message: str):
        super().__init__(message)
