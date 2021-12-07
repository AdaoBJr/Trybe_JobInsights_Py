from src.sorting import sort_by

"""Defini as listas que o parametro criteria de ter
com min_salary, max_salary, date_posted """

"""Lista com todos os salarios"""
salaries = [
    {"min_salary": 900, "max_salary": 2000, "date_posted": "2021-01-01"},
    {"min_salary": 800, "max_salary": 1000, "date_posted": "2021-01-01"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-01-01"},
]

""" Ordem crescente: """
min_salary = [
    {"min_salary": 800, "max_salary": 1000, "date_posted": "2021-01-01"},
    {"min_salary": 900, "max_salary": 2000, "date_posted": "2021-01-01"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-01-01"},
]

""" Ordem decrescentes: """
max_salary = [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-01-01"},
    {"min_salary": 900, "max_salary": 2000, "date_posted": "2021-01-01"},
    {"min_salary": 800, "max_salary": 1000, "date_posted": "2021-01-01"},
]

date_posted = [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-01-01"},
    {"min_salary": 900, "max_salary": 2000, "date_posted": "2021-01-01"},
    {"min_salary": 800, "max_salary": 1000, "date_posted": "2021-01-01"},
]


def test_sort_by_criteria():
    pass
    assert sort_by(salaries, "min_salary") == min_salary
    assert sort_by(salaries, "max_salary") == max_salary
    assert sort_by(salaries, "date_posted") == salaries
