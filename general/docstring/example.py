class RuntimeErrorWithCode(Exception):
    """
    DOCSTRING
    Exception raised when a specific error code is needed.
    """
    def __init__(self, message, code) -> None:
        super().__init__(f'Error code {code}: {message}')
        self.code = code

class UncountableError(ValueError):
    def __init__(self, wrong_value):
        super().__init__(f'Invalid value for n, {wrong_value}. n must be greater than 0.')

raise RuntimeErrorWithCode('Example error message', 500)
err = RuntimeErrorWithCode('An error happened.', 500)
print(err.__doc__) # display the docstring
