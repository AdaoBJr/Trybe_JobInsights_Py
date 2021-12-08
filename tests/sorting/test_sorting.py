from src.sorting import sort_by

list = [
    {'min_salary': 1500, 'max_salary': 22000, 'date_posted': '2020-04-19'},
    {'min_salary': 2300, 'max_salary': 25000, 'date_posted': '2019-01-19'},
    {'min_salary': 3000, 'max_salary': 50000, 'date_posted': '2021-01-21'},
]

min_salary_list = [
    {'min_salary': 2300, 'max_salary': 25000, 'date_posted': '2019-01-19'},
    {'min_salary': 1500, 'max_salary': 22000, 'date_posted': '2020-04-19'},
    {'min_salary': 3000, 'max_salary': 50000, 'date_posted': '2021-01-21'},
]

max_salary_list = [
    {'min_salary': 2300, 'max_salary': 25000, 'date_posted': '2019-01-19'},
    {'min_salary': 3000, 'max_salary': 50000, 'date_posted': '2021-01-21'},
    {'min_salary': 1500, 'max_salary': 22000, 'date_posted': '2020-04-19'},
]

date_posted_list = [
    {'min_salary': 3000, 'max_salary': 50000, 'date_posted': '2021-01-21'},
    {'min_salary': 1500, 'max_salary': 22000, 'date_posted': '2020-04-19'},
    {'min_salary': 2300, 'max_salary': 25000, 'date_posted': '2019-01-19'},
]


def test_sort_by_criteria():
    assert sort_by(list, 'min_salary') == min_salary_list
    assert sort_by(list, 'max_salary') == max_salary_list
    assert sort_by(list, 'date_posted') == date_posted_list
