import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    sort_this_jobs = [
        {"min_salary": 100, "max_salary": 2000,  "date_posted": "2020-10-08"},
        {"min_salary": 200, "max_salary": 10000,  "date_posted": "2020-11-11"},
    ]
    jobs_by_min_salary = [
        {"min_salary": 100, "max_salary": 2000,  "date_posted": "2020-10-08"},
        {"min_salary": 200, "max_salary": 10000,  "date_posted": "2020-11-11"},
    ]

    jobs_by_max_salary = [
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-11-11"},
        {"max_salary": 2000, "min_salary": 100, "date_posted": "2020-10-08"},
    ]

    with pytest.raises(TypeError):
        sort_by(sort_this_jobs)

    sort_by(sort_this_jobs, 'max_salary')
    assert(sort_this_jobs == jobs_by_max_salary)

    sort_by(sort_this_jobs, 'min_salary')
    assert(sort_this_jobs == jobs_by_min_salary)
