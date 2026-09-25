import pytest
from app.main import get_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected", [
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (18, 18, [1, 1]),
    (28, 28, [3, 2]),
    (29, 29, [3, 3]),
    (100, 100, [21, 17]),
    (28, 29, [3, 3])
])
def test_animal_if_age_less_15(cat_age: int,
                               dog_age: int,
                               expected: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected
