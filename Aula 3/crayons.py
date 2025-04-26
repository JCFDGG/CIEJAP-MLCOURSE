
def hello_world(condition: bool = True) -> str:
    '''
    Example function to illustrate unit testing.

    Parameters:
    condition (bool): A boolean condition to determine the return value.

    Returns:
    str: A greeting message.
    '''
    if condition:
        return "Hello, world!"
    else:
        return "Goodbye, world!"
