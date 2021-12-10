from src.sorting import sort_by


# Ajuda de Eder Paiva
jobs = [
    {"min_salary": 950, "max_salary": 2500, "date_posted": "2021-01-01"},
    {"min_salary": 800, "max_salary": 1000, "date_posted": "2021-01-01"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-01-01"},
]

min_salary = [
    {"min_salary": 850, "max_salary": 1500, "date_posted": "2021-01-01"},
    {"min_salary": 900, "max_salary": 2000, "date_posted": "2021-01-01"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-01-01"},
]

max_salary = [
    {"min_salary": 1500, "max_salary": 3500, "date_posted": "2020-01-01"},
    {"min_salary": 900, "max_salary": 2000, "date_posted": "2021-01-01"},
    {"min_salary": 800, "max_salary": 1000, "date_posted": "2021-01-01"},
]

date_posted = [
    {"min_salary": 1500, "max_salary": 3500, "date_posted": "2020-01-01"},
    {"min_salary": 900, "max_salary": 2000, "date_posted": "2021-01-01"},
    {"min_salary": 800, "max_salary": 1000, "date_posted": "2021-01-01"},
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == min_salary

    sort_by(jobs, "max_salary")
    assert jobs == max_salary

    sort_by(jobs, "date_posted")
    assert jobs == date_posted
