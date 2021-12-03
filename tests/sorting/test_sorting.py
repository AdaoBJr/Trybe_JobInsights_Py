from src.sorting import sort_by

salary_list = [
    {"min_salary": 4000, "max_salary": 4500, "date_posted": "2021-01-04"},
    {"min_salary": 2000, "max_salary": 2500, "date_posted": "2021-01-02"},
    {"min_salary": 1000, "max_salary": 1500, "date_posted": "2021-01-01"},
    {"min_salary": 5000, "max_salary": 5500, "date_posted": "2021-01-05"},
    {"min_salary": 3000, "max_salary": 3500, "date_posted": "2021-01-03"},
]

min_salary_list = [
    {"min_salary": 1000, "max_salary": 1500, "date_posted": "2021-01-01"},
    {"min_salary": 2000, "max_salary": 2500, "date_posted": "2021-01-02"},
    {"min_salary": 3000, "max_salary": 3500, "date_posted": "2021-01-03"},
    {"min_salary": 4000, "max_salary": 4500, "date_posted": "2021-01-04"},
    {"min_salary": 5000, "max_salary": 5500, "date_posted": "2021-01-05"},
]

max_salary_list = [
    {"min_salary": 5000, "max_salary": 5500, "date_posted": "2021-01-05"},
    {"min_salary": 4000, "max_salary": 4500, "date_posted": "2021-01-04"},
    {"min_salary": 3000, "max_salary": 3500, "date_posted": "2021-01-03"},
    {"min_salary": 2000, "max_salary": 2500, "date_posted": "2021-01-02"},
    {"min_salary": 1000, "max_salary": 1500, "date_posted": "2021-01-01"},
]


def test_sort_by_criteria():
    assert sort_by(salary_list, "min_salary") == min_salary_list
    assert sort_by(salary_list, "max_salary") == max_salary_list
    assert sort_by(salary_list, "date_posted") == max_salary_list
