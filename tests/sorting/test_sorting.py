from src.sorting import sort_by


salary_list = [
    {"min_salary": 700, "max_salary": 3000, "date_posted": "2020-02-10"},
    {"min_salary": 600, "max_salary": 2000, "date_posted": "2020-02-09"},
    {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-02-08"},
]

sorted_by_min_salary = [
    {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-02-08"},
    {"min_salary": 600, "max_salary": 2000, "date_posted": "2020-02-09"},
    {"min_salary": 700, "max_salary": 3000, "date_posted": "2020-02-10"},
]

sorted_by_max_salary = [
    {"min_salary": 700, "max_salary": 3000, "date_posted": "2020-02-10"},
    {"min_salary": 600, "max_salary": 2000, "date_posted": "2020-02-09"},
    {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-02-08"},
]

sorted_by_date_posted = [
    {"min_salary": 700, "max_salary": 3000, "date_posted": "2020-05-10"},
    {"min_salary": 600, "max_salary": 2000, "date_posted": "2020-05-09"},
    {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-05-08"},
]


def test_sort_by_criteria():
    assert sort_by(salary_list, "min_salary") == sorted_by_min_salary
    assert sort_by(salary_list, "max_salary") == sorted_by_max_salary
    assert sort_by(salary_list, "date_posted") == sorted_by_date_posted
