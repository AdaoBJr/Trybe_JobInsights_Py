from src.sorting import sort_by
import pytest

works_list = [
    {"date_posted": "2020-01-01", "max_salary": 6000, "min_salary": 2000},
    {"date_posted": "2021-01-01", "max_salary": 5000, "min_salary": 1000},
    {"date_posted": "2019-01-01", "max_salary": 7000, "min_salary": 3000},
]

works_list_min = [
    works_list[1],
    works_list[0],
    works_list[2],
]

works_list_max = [
    works_list[2],
    works_list[0],
    works_list[1],
]

works_list_date = [
    works_list[1],
    works_list[0],
    works_list[2],
]

sort_by(
    [
        {"date_posted": "2021-01-01", "max_salary": 5000, "min_salary": 1000},
        {"date_posted": "2020-01-01", "max_salary": 6000, "min_salary": 2000},
        {"date_posted": "2019-01-01", "max_salary": 7000, "min_salary": 3000},
    ],
    "date_posted",
)


def test_sort_by_criteria():
    sort_by(works_list, "min_salary")
    assert works_list == works_list_min

    sort_by(works_list, "max_salary")
    assert works_list == works_list_max

    sort_by(works_list, "date_posted")
    assert works_list == works_list_date

    with pytest.raises(
        TypeError, match="missing 1 required positional argument: 'criteria'"
    ):
        sort_by(works_list)
