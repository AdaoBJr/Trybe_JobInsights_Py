from src.sorting import sort_by
import pytest


data = [
    {"date_posted": "01/01/2000", "max_salary": 1, "min_salary": 1},
    {"date_posted": "02/01/2000", "max_salary": 2, "min_salary": 2},
    {"date_posted": "03/01/2000", "max_salary": 3, "min_salary": 3},
]


# expected
expected_min_salary = [data[0], data[1], data[2]]

expected_max_salary = [data[2], data[1], data[0]]


def test_sort_by_criteria():
    sort_by(data, "min_salary")
    assert expected_min_salary == data

    sort_by(data, "max_salary")
    assert expected_max_salary == data

    sort_by(data, "date_posted")
    assert expected_max_salary == data

    with pytest.raises(
        TypeError, match="missing 1 required positional argument: 'criteria'"
    ):
        sort_by(data)
