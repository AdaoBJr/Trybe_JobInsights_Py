from src.sorting import sort_by
import pytest

job_list = [
    {
        "job": "Driver",
        "min_salary": 500,
        "max_salary": 800,
        "date_posted": "2021-02-09",
    },
    {
        "job": "Teacher",
        "min_salary": 800,
        "max_salary": 1000,
        "date_posted": "2020-02-09",
    },
    {
        "job": "Teacher",
        "min_salary": 900,
        "max_salary": 1200,
        "date_posted": "2022-02-09",
    },
]

sorted_min_salary = [
    {
        "job": "Driver",
        "min_salary": "500",
        "max_salary": "800",
        "date_posted": "2021-02-09",
    },
    {
        "job": "Teacher",
        "min_salary": "800",
        "max_salary": "1000",
        "date_posted": "2020-02-09",
    },
    {
        "job": "Teacher",
        "min_salary": "800",
        "max_salary": "1200",
        "date_posted": "2022-02-09",
    },
]

sorted_max_salary_date_posted = [
    {
        "job": "Teacher",
        "min_salary": "800",
        "max_salary": "1200",
        "date_posted": "2022-02-09",
    },
    {
        "job": "Teacher",
        "min_salary": "800",
        "max_salary": "1000",
        "date_posted": "2021-02-09",
    },
    {
        "job": "Driver",
        "min_salary": "500",
        "max_salary": "800",
        "date_posted": "2020-02-09",
    },
]


def test_sort_by_criteria():
    sort_by(job_list, "min_salary")
    assert job_list == sorted_min_salary

    sort_by(job_list, "max_salary")
    assert job_list == sorted_max_salary_date_posted

    sort_by(job_list, "date_posted")
    assert job_list == sorted_max_salary_date_posted

    with pytest.raises(
        ValueError, match="ValueError: invalid sorting criteria: anything"
    ):
        sort_by(job_list, "anything")
