import pytest
from src.sorting import sort_by

jobs = [
    {
        "job_title": "Web Developer",
        "min_salary": 4500,
        "max_salary": 15000,
        "date_posted": "2021-12-23",
    },
    {
        "job_title": "iOS Developer",
        "min_salary": 4000,
        "max_salary": 12000,
        "date_posted": "2021-09-30",
    },
    {
        "job_title": "Android Developer",
        "min_salary": 3800,
        "max_salary": 10000,
        "date_posted": "2021-02-17",
    },
]

min_salary = [
    {
        "job_title": "Android Developer",
        "min_salary": 3800,
        "max_salary": 10000,
        "date_posted": "2021-02-17",
    },
    {
        "job_title": "iOS Developer",
        "min_salary": 4000,
        "max_salary": 12000,
        "date_posted": "2021-09-30",
    },
    {
        "job_title": "Web Developer",
        "min_salary": 4500,
        "max_salary": 15000,
        "date_posted": "2021-12-23",
    },
]

max_salary = [
    {
        "job_title": "Web Developer",
        "min_salary": 4500,
        "max_salary": 15000,
        "date_posted": "2021-12-23",
    },
    {
        "job_title": "iOS Developer",
        "min_salary": 4000,
        "max_salary": 12000,
        "date_posted": "2021-09-30",
    },
    {
        "job_title": "Android Developer",
        "min_salary": 3800,
        "max_salary": 10000,
        "date_posted": "2021-02-17",
    },
]

date_posted = [
    {
        "job_title": "Web Developer",
        "min_salary": 4500,
        "max_salary": 15000,
        "date_posted": "2021-12-23",
    },
    {
        "job_title": "iOS Developer",
        "min_salary": 4000,
        "max_salary": 12000,
        "date_posted": "2021-09-30",
    },
    {
        "job_title": "Android Developer",
        "min_salary": 3800,
        "max_salary": 10000,
        "date_posted": "2021-02-17",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == min_salary

    sort_by(jobs, "max_salary")
    assert jobs == max_salary

    sort_by(jobs, "date_posted")
    assert jobs == date_posted

    with pytest.raises(TypeError):
        sort_by(jobs)
