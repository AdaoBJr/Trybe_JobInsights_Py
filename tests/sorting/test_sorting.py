from src.sorting import sort_by

jobs = [
    {
        "max_salary": 10000,
        "min_salary": 5000,
        "date_posted": "2019-01-01",
    },
    {
        "max_salary": 20000,
        "min_salary": 10000,
        "date_posted": "2019-01-02",
    },
]

min_salary_order = [
    {
        "max_salary": 10000,
        "min_salary": 5000,
        "date_posted": "2019-01-01",
    },
    {
        "max_salary": 20000,
        "min_salary": 10000,
        "date_posted": "2019-01-02",
    },
]

max_salary_order = [
    {
        "max_salary": 20000,
        "min_salary": 10000,
        "date_posted": "2019-01-02",
    },
    {
        "max_salary": 10000,
        "min_salary": 5000,
        "date_posted": "2019-01-01",
    },
]

date_posted_order = [
    {
        "max_salary": 20000,
        "min_salary": 10000,
        "date_posted": "2019-01-02",
    },
    {
        "max_salary": 10000,
        "min_salary": 5000,
        "date_posted": "2019-01-01",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == min_salary_order

    sort_by(jobs, "max_salary")
    assert jobs == max_salary_order

    sort_by(jobs, "date_posted")
    assert jobs == date_posted_order
