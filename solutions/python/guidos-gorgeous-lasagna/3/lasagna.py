EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time.

    Parameters:
        number_of_layers (int): the number of layers for lasagna.

    Returns:
        int: The remaining prepating time (in minutes) derived from 'PREPARATION_TIME'.
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    Parameters:
        number_of_layers (int): the number of layers for lasagna.
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: Total elapsed time for lazagna in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time