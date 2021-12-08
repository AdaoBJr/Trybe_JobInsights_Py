from src.sorting import sort_by

jobs = [
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": "2021-12-01",
    },
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": "2021-12-10",
    },
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": "2021-12-03",
    },
]

ascending = [
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": "2021-12-10",
    },
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": "2021-12-01",
    },
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": "2021-12-03",
    },
]

descending = [
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": "2021-12-03",
    },
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": "2021-12-01",
    },
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": "2021-12-10",
    },
]

dateposted = [
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": "2021-12-10",
    },
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": "2021-12-03",
    },
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": "2021-12-01",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == descending
    sort_by(jobs, "max_salary")
    assert jobs == ascending
    sort_by(jobs, "date_posted")
    assert jobs == dateposted
