import numpy as np


def test_function(array: np.ndarray, factor: float) -> np.ndarray:
    """Just a test function

    Args:
        array (np.ndarray): Array to be multiplied
        factor (float): Multiplication factor

    Returns:
        np.ndarray: Multiplied array
    """

    # Do something with the array
    for dim in array:
        dim *= factor

    # Print other stuff
    print(array.shape)

    # return array
    return array
