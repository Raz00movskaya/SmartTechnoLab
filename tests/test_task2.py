import pytest
from my_funcs.task2 import function_coordinates


@pytest.mark.parametrize("x1,y1, x2, y2, result", [(6, 4, 2, 8, 5.657),
                                                   (1, 2, 6, 1, 5.099)])
def test_task2(x1, y1, x2, y2, result):
    assert function_coordinates(x1, y1, x2, y2) == result


@pytest.mark.parametrize("x1, y1, x2, y2, expected_exception", [
    # ('1', '4', '6', '2', TypeError),
    ('vsv', 'ssa', 'asas', 'fgnfnjd', ValueError)])
def test_task2_with_errors(x1, y1, x2, y2, expected_exception):
    with pytest.raises(expected_exception):
        assert function_coordinates(x1, y1, x2, y2)
