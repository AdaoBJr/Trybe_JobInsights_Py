from src.sorting import sort_by

jobs_list = [
    {'min_salary': 15948, 'max_salary': 20154, 'date_posted': '2020-04-19'},
    {'min_salary': 25478, 'max_salary': 50000, 'date_posted': '2019-01-19'},
    {'min_salary': 36985, 'max_salary': 79521, 'date_posted': '2021-01-21'},
]

list_min_salary = [
    {'min_salary': 25478, 'max_salary': 50000, 'date_posted': '2019-01-19'},
    {'min_salary': 15948, 'max_salary': 20154, 'date_posted': '2020-04-19'},
    {'min_salary': 36985, 'max_salary': 79521, 'date_posted': '2021-01-21'},
]

list_max_salary = [
    {'min_salary': 25478, 'max_salary': 50000, 'date_posted': '2019-01-19'},
    {'min_salary': 36985, 'max_salary': 79521, 'date_posted': '2021-01-21'},
    {'min_salary': 15948, 'max_salary': 20154, 'date_posted': '2020-04-19'},
]

list_date_posted = [
    {'min_salary': 36985, 'max_salary': 79521, 'date_posted': '2021-01-21'},
    {'min_salary': 15948, 'max_salary': 20154, 'date_posted': '2020-04-19'},
    {'min_salary': 25478, 'max_salary': 50000, 'date_posted': '2019-01-19'},
]


def test_sort_by_criteria():
    assert sort_by(jobs_list, 'min_salary') == list_min_salary
    assert sort_by(jobs_list, 'max_salary') == list_max_salary
    assert sort_by(jobs_list, 'date_posted') == list_date_posted
