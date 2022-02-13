import pytest

from generators import my_range


@pytest.mark.parametrize('params, expected_values', [
    ((4, ), (0, 1, 2, 3)),
    ((2, 5), (2, 3, 4)),
    ((0, 7, 2), (0, 2, 4, 6))
])
def test_generator(params, expected_values):
    gen = my_range(*params)

    for value in expected_values:
        assert next(gen) == value

    with pytest.raises(StopIteration):
        next(gen)
