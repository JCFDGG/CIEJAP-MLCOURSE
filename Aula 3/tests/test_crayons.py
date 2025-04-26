from crayons import hello_world

def test_hello_world_default():
    """
    Test the default behavior of hello_world.
    Testing: the default condition (True).
    Expected results: it returns "Hello, world!".
    """
    # arrange
    # act
    result = hello_world()
    # assert
    assert result == "Hello, world!"