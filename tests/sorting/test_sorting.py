from src.sorting import sort_by


default_list = [
    {"min_salary": 500, "max_salary": 800, "date_posted": "2021-12-09"},
    {"min_salary": 400, "max_salary": 700, "date_posted": "2021-11-09"},
    {"min_salary": 600, "max_salary": 900, "date_posted": "2021-10-09"},
]

min_salary = [
    {"min_salary": 400, "max_salary": 700, "date_posted": "2021-11-09"},
    {"min_salary": 500, "max_salary": 800, "date_posted": "2021-12-09"},
    {"min_salary": 600, "max_salary": 900, "date_posted": "2021-10-09"},
]

max_salary_or_data_posted = [
    {"min_salary": 600, "max_salary": 900, "date_posted": "2021-10-09"},
    {"min_salary": 500, "max_salary": 800, "date_posted": "2021-12-09"},
    {"min_salary": 400, "max_salary": 700, "date_posted": "2021-11-09"},
]


def test_sort_by_criteria():
    assert sort_by(default_list, "min_salary") == min_salary
    assert sort_by(default_list, "max_salary") == max_salary_or_data_posted
    assert sort_by(default_list, "date_posted") == max_salary_or_data_posted
