from src.sorting import sort_by

jobs = [
    {"min_salary": 3000, "max_salary": 5500, "date_posted": "2021-11-09"},
    {"min_salary": 1000, "max_salary": 3500, "date_posted": "2020-01-19"},
    {"min_salary": 2000, "max_salary": 5500, "date_posted": "2022-01-09"}
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 3000, "max_salary": 5500, "date_posted": "2021-11-09"},
        {"min_salary": 1000, "max_salary": 3500, "date_posted": "2020-01-19"},
        {"min_salary": 2000, "max_salary": 5500, "date_posted": "2022-01-09"}
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 3000, "max_salary": 5500, "date_posted": "2021-11-09"},
        {"min_salary": 1000, "max_salary": 3500, "date_posted": "2020-01-19"},
        {"min_salary": 2000, "max_salary": 5500, "date_posted": "2022-01-09"}
    ]

    sort_by(jobs, "data_posted")
    assert jobs == [
        {"min_salary": 3000, "max_salary": 5500, "date_posted": "2021-11-09"},
        {"min_salary": 1000, "max_salary": 3500, "date_posted": "2020-01-19"},
        {"min_salary": 2000, "max_salary": 5500, "date_posted": "2022-01-09"}
    ]
