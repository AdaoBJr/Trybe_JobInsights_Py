from src.sorting import sort_by

jobs_list = [
    {
        "max_salary": 2000,
        "min_salary": 1000,
        "date_posted": "2022-01-11",
    },
    {
        "max_salary": 4000,
        "min_salary": 2000,
        "date_posted": "2022-01-12",
    },
]

min_salary_order = [
    {
        "max_salary": 2000,
        "min_salary": 1000,
        "date_posted": "2022-01-11",
    },
    {
        "max_salary": 4000,
        "min_salary": 2000,
        "date_posted": "2022-01-12",
    },
]

max_salary_order = [
    {
        "max_salary": 4000,
        "min_salary": 2000,
        "date_posted": "2022-01-12",
    },
    {
        "max_salary": 2000,
        "min_salary": 1000,
        "date_posted": "2022-01-11",
    },
]

date_posted_order = [
    {
        "max_salary": 4000,
        "min_salary": 2000,
        "date_posted": "2022-01-12",
    },
    {
        "max_salary": 2000,
        "min_salary": 1000,
        "date_posted": "2022-01-11",
    },
]


def test_sort_by_criteria():
    sort_by(jobs_list, "min_salary")
    assert jobs_list == min_salary_order

    sort_by(jobs_list, "max_salary")
    assert jobs_list == max_salary_order

    sort_by(jobs_list, "date_posted")
    assert jobs_list == date_posted_order
