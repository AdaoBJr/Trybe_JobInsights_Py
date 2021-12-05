from src.sorting import sort_by
import pytest


jobs = [
    {"min_salary": 10, "max_salary": 1000, "date_posted": 2021-10-13},
    {"min_salary": 5, "max_salary": 2000, "date_posted": 2021-10-15},
    {"min_salary": 15, "max_salary": 1500, "date_posted": 2021-10-14}
    ]

max_salary = [
    {"min_salary": 5, "max_salary": 2000, "date_posted": 2021-10-15},
    {"min_salary": 15, "max_salary": 1500, "date_posted": 2021-10-14},
    {"min_salary": 10, "max_salary": 1000, "date_posted": 2021-10-13}
    ]

min_salary = [
    {"min_salary": 5, "max_salary": 2000, "date_posted": 2021-10-15},
    {"min_salary": 10, "max_salary": 1000, "date_posted": 2021-10-13},
    {"min_salary": 15, "max_salary": 1500, "date_posted": 2021-10-14}
    ]

maximum_salary = "2000"
minimum_salary = 5
number = 1000


def test_sort_by_criteria():
    assert sort_by(jobs, "max_salary") == max_salary
    assert sort_by(jobs, "min_salary") == min_salary
    assert sort_by(jobs, "date_posted") == max_salary
    with pytest.raises(ValueError, match="invalid sorting criteria: 1000"):
        sort_by(jobs, number)
    pass
