from src.sorting import sort_by

jobs = [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-01-01"},
    {"min_salary": 3000, "max_salary": 9000, "date_posted": "2021-02-05"},
    {"min_salary": 2000, "max_salary": 6000, "date_posted": "2021-03-10"},
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-01-01"},
        {"min_salary": 2000, "max_salary": 6000, "date_posted": "2021-03-10"},
        {"min_salary": 3000, "max_salary": 9000, "date_posted": "2021-02-05"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 3000, "max_salary": 9000, "date_posted": "2021-02-05"},
        {"min_salary": 2000, "max_salary": 6000, "date_posted": "2021-03-10"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-01-01"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 2000, "max_salary": 6000, "date_posted": "2021-03-10"},
        {"min_salary": 3000, "max_salary": 9000, "date_posted": "2021-02-05"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2021-01-01"},
    ]
