from src.sorting import sort_by


jobs = [
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2019-10-08"},
    {"min_salary": 2500, "max_salary": 5500, "date_posted": "2020-10-08"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2021-10-08"},
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2019-10-08"},
        {"min_salary": 2500, "max_salary": 5500, "date_posted": "2020-10-08"},
        {"min_salary": 3000, "max_salary": 6000, "date_posted": "2021-10-08"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 3000, "max_salary": 6000, "date_posted": "2021-10-08"},
        {"min_salary": 2500, "max_salary": 5500, "date_posted": "2020-10-08"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2019-10-08"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 3000, "max_salary": 6000, "date_posted": "2021-10-08"},
        {"min_salary": 2500, "max_salary": 5500, "date_posted": "2020-10-08"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2019-10-08"},
    ]
