from src.sorting import sort_by

data = [
    {"min_salary": 3, "max_salary": 3, "date_posted": "03/01/2000"},
    {"min_salary": 1, "max_salary": 1, "date_posted": "01/01/2000"},
    {"min_salary": 2, "max_salary": 2, "date_posted": "02/01/2000"},
]

expected_min_salary = [
    {"min_salary": 1, "max_salary": 1, "date_posted": "01/01/2000"},
    {"min_salary": 2, "max_salary": 2, "date_posted": "01/01/2000"},
    {"min_salary": 3, "max_salary": 3, "date_posted": "01/01/2000"},
]

expected_max_salary = [
    {"min_salary": 3, "max_salary": 3, "date_posted": "03/01/2000"},
    {"min_salary": 2, "max_salary": 2, "date_posted": "02/01/2000"},
    {"min_salary": 1, "max_salary": 1, "date_posted": "01/01/2000"},
]


def test_sort_by_criteria():
    report = sort_by(data, "max_salary")
    assert expected_max_salary in report
