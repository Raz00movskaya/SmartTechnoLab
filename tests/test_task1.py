import pytest
from my_funcs.task1 import bonus_cups


@pytest.mark.parametrize("a, result", [(0, 0),
                                       (6, 1),
                                       (11, 1),
                                       (12, 2),
                                       (-1, 0),
                                       ('14', 2)])
def test_task1(a, result):
    assert bonus_cups(a) == result


@pytest.mark.parametrize("a, expected_exception", [('sfsf', ValueError),
                                                   # ('1', TypeError)
                                                   ])
def test_task1_with_errors(a, expected_exception):
    with pytest.raises(expected_exception):
        assert bonus_cups(a)
