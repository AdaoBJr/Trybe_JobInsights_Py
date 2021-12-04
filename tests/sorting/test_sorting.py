# import pytest
from src.sorting import sort_by

jobs = [
    {"max_salary": 1000, "min_salary": 10, "data_posted": "2021-10-15"},
    {"max_salary": 2000, "min_salary": 20, "data_posted": "2021-10-30"},
    {"max_salary": 500, "min_salary": 5, "data_posted": "2021-10-05"},
]

resp_min_salary = [
    {"max_salary": 500, "min_salary": 5, "data_posted": "2021-10-05"},
    {"max_salary": 1000, "min_salary": 10, "data_posted": "2021-10-15"},
    {"max_salary": 2000, "min_salary": 20, "data_posted": "2021-10-30"},
]

resp_max_salary = [
    {"max_salary": 2000, "min_salary": 20, "data_posted": "2021-10-30"},
    {"max_salary": 1000, "min_salary": 10, "data_posted": "2021-10-15"},
    {"max_salary": 500, "min_salary": 5, "data_posted": "2021-10-05"},
]

resp_date = [
    {"max_salary": 2000, "min_salary": 20, "data_posted": "2021-10-30"},
    {"max_salary": 1000, "min_salary": 10, "data_posted": "2021-10-15"},
    {"max_salary": 500, "min_salary": 5, "data_posted": "2021-10-05"},
]


def test_sort_by_criteria():
    jobs_sorted = sort_by(jobs, "min_salary")
    assert jobs_sorted == resp_min_salary

    jobs_sorted = sort_by(jobs, "max_salary")
    assert jobs_sorted == resp_max_salary

    jobs_sorted = sort_by(jobs, "date_posted")
    assert jobs_sorted == resp_date
