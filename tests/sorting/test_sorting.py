from src.sorting import sort_by

salary = [
    {"min_salary": 3000, "max_salary": 1000, "date_posted": "2022-02-15"},
    {"min_salary": 1192, "max_salary": 12000, "date_posted": "2021-02-01"},
    {"min_salary": 3500, "max_salary": 5000, "date_posted": "2021-12-06"},
]

sorted_by_min = [
    {"min_salary": 1192, "max_salary": 12000, "date_posted": "2021-02-01"},
    {"min_salary": 3000, "max_salary": 1000, "date_posted": "2022-02-15"},
    {"min_salary": 3500, "max_salary": 5000, "date_posted": "2021-12-06"},
]

sorted_by_max = [
    {"min_salary": 3000, "max_salary": 1000, "date_posted": "2022-02-15"},
    {"min_salary": 3500, "max_salary": 5000, "date_posted": "2021-12-06"},
    {"min_salary": 1192, "max_salary": 12000, "date_posted": "2021-02-01"},
]

sorted_by_date = [
    {"min_salary": 1192, "max_salary": 12000, "date_posted": "2021-02-01"},
    {"min_salary": 3500, "max_salary": 5000, "date_posted": "2021-12-06"},
    {"min_salary": 3000, "max_salary": 1000, "date_posted": "2022-02-15"},
]

def test_sort_by_criteria():
    assert sort_by(salary, 'min_salary') == sorted_by_min
    assert sort_by(salary, 'max_salary') == sorted_by_max
    assert sort_by(salary, 'date_posted') == sorted_by_date
