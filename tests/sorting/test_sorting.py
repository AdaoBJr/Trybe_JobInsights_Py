from src.sorting import sort_by
import pytest


def test_sort_by_criteria():
    data = [
        {"date_posted": "06/06/2021", "max_salary": 14, "min_salary": 12},
        {"date_posted": "07/06/2021", "max_salary": 15, "min_salary": 11},
        {"date_posted": "08/06/2021", "max_salary": 16, "min_salary": 10},
    ]

    data_sort_max = [data[2], data[1], data[0]]
    data_sort_min = [data[2], data[1], data[0]]
    data_sort_posted = [data[2], data[1], data[0]]

    sort_by(data, "max_salary")
    assert data == data_sort_max

    sort_by(data, "min_salary")
    assert data == data_sort_min

    sort_by(data, "date_posted")
    assert data == data_sort_posted

    with pytest.raises(
        TypeError, match="criteria"
    ):
        sort_by(data)
