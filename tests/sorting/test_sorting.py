from src.sorting import sort_by

jobs = [
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-02-03"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-02-04"},
    {"max_salary": 1600, "min_salary": 9, "date_posted": "2020-02-01"},
]

criteria_keys = ["date_posted", "max_salary", "min_salary"]

expected_jobs_min_salary = [
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-02-04"},
    {"max_salary": 1600, "min_salary": 9, "date_posted": "2020-02-01"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-02-03"},
]

expected_jobs_max_salary = [
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-02-03"},
    {"max_salary": 1600, "min_salary": 9, "date_posted": "2020-02-01"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-02-04"},
]

expected_jobs_date_posted = [
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-02-04"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-02-03"},
    {"max_salary": 1600, "min_salary": 9, "date_posted": "2020-02-01"},
]


def test_sort_by_criteria():
    "Para o critério de min_salary deve retornar em ordem decrescente"
    sort_by(jobs, criteria_keys[2])
    assert jobs == expected_jobs_min_salary

    "Para o critério de max_salary deve retornar em ordem crescente"
    sort_by(jobs, criteria_keys[1])
    assert jobs == expected_jobs_max_salary

    "Para o critério de date_posted deve retornar em ordem crescente"
    sort_by(jobs, criteria_keys[0])
    assert jobs == expected_jobs_date_posted
