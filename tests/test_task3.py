import pytest
from my_funcs.task3 import number_of_legs


@pytest.mark.parametrize("chikens, pigs, cows, result", [(1, 1, 1, 10),
                                                         (1, 2, 3, 22),
                                                         (2, 1, 1, 12)])
def test_task3(chikens, pigs, cows, result):
    assert number_of_legs(chikens, pigs, cows) == result

