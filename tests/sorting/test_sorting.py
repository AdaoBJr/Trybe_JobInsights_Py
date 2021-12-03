from src.sorting import sort_by
import pytest


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 4458, "max_salary": 8216, "date_posted": "2020-05-08"},
        {"min_salary": 9471, "max_salary": 10327, "date_posted": "2020-05-05"},
        {"min_salary": 2000, "max_salary": 3500, "date_posted": "2020-05-07"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 2000, "max_salary": 3500, "date_posted": "2020-05-07"},
        {"min_salary": 4458, "max_salary": 8216, "date_posted": "2020-05-08"},
        {"min_salary": 9471, "max_salary": 10327, "date_posted": "2020-05-05"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 9471, "max_salary": 10327, "date_posted": "2020-05-05"},
        {"min_salary": 4458, "max_salary": 8216, "date_posted": "2020-05-08"},
        {"min_salary": 2000, "max_salary": 3500, "date_posted": "2020-05-07"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 9471, "max_salary": 10327, "date_posted": "2020-05-05"},
        {"min_salary": 4458, "max_salary": 8216, "date_posted": "2020-05-08"},
        {"min_salary": 2000, "max_salary": 3500, "date_posted": "2020-05-07"},
    ]

    with pytest.raises(ValueError):
        sort_by(jobs, "min_salary")

    pass
