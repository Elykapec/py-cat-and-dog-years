from app.main import get_human_age


def test_zero_age() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_less_than_first_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_exactly_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_between_first_and_second_threshold() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_exactly_second_threshold() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_after_second_threshold() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_different_growth_rates() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_large_numbers() -> None:
    assert get_human_age(100, 100) == [21, 17]
