import pytest
from my_funcs.task6 import counter_of_nums


@pytest.mark.parametrize("a, result", [(5, 8),
                                       (3, 3),
                                       ('0', 0),
                                       ('dfdfd', None)])
def test_task6(a, result):
    assert counter_of_nums(a) == result


