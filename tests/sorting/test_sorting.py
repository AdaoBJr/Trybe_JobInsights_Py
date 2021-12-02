import pytest
from src.sorting import sort_by

job_list = [
    {'min_salary': 0, 'max_salary': 2000, 'date_posted': '2021-12-00'},
    {'min_salary': 1000, 'max_salary': 3000, 'date_posted': '2021-10-00'},
    {'min_salary': 250, 'max_salary': 4000, 'date_posted': '2021-08-00'},
    {'min_salary': 500, 'max_salary': 1000, 'date_posted': '2021-06-00'},
]

job_list_ordened_by_min_salary = [
    {'min_salary': 0, 'max_salary': 2000, 'date_posted': '2021-12-00'},
    {'min_salary': 250, 'max_salary': 4000, 'date_posted': '2021-08-00'},
    {'min_salary': 500, 'max_salary': 1000, 'date_posted': '2021-06-00'},
    {'min_salary': 1000, 'max_salary': 3000, 'date_posted': '2021-10-00'},
]

job_list_ordened_by_max_salary = [
    {'min_salary': 250, 'max_salary': 4000, 'date_posted': '2021-08-00'},
    {'min_salary': 1000, 'max_salary': 3000, 'date_posted': '2021-10-00'},
    {'min_salary': 0, 'max_salary': 2000, 'date_posted': '2021-12-00'},
    {'min_salary': 500, 'max_salary': 1000, 'date_posted': '2021-06-00'},
]

job_list_ordened_by_posted_date = [
    {'min_salary': 0, 'max_salary': 2000, 'date_posted': '2021-12-00'},
    {'min_salary': 1000, 'max_salary': 3000, 'date_posted': '2021-10-00'},
    {'min_salary': 250, 'max_salary': 4000, 'date_posted': '2021-08-00'},
    {'min_salary': 500, 'max_salary': 1000, 'date_posted': '2021-06-00'},
]

job_with_invalid_str_values = [
    {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    {'min_salary': '', 'max_salary': '', 'date_posted': ''},
]

job_with_list_values = [
    {'min_salary': [], 'max_salary': [], 'date_posted': []},
    {'min_salary': [], 'max_salary': [], 'date_posted': []},
    {'min_salary': [], 'max_salary': [], 'date_posted': []},
]


def test_raises_error_with_invalid_criteria():
    with pytest.raises(ValueError):
        sort_by([], 'invalid_criteira')


def test_sort_by_max_salary_criteria():
    assert sort_by(job_list, 'max_salary') == job_list_ordened_by_max_salary


def test_sort_with_max_salary_str():
    with pytest.raises(ValueError):
        sort_by(job_with_invalid_str_values, 'max_salary')


def test_sort_with_max_salary_list():
    with pytest.raises(TypeError):
        sort_by(job_with_list_values, 'max_salary')


def test_sort_by_min_salary_criteria():
    assert sort_by(job_list, 'min_salary') == job_list_ordened_by_min_salary


def test_sort_with_min_salary_str():
    with pytest.raises(ValueError):
        sort_by(job_with_invalid_str_values, 'min_salary')


def test_sort_with_min_salary_list():
    with pytest.raises(TypeError):
        sort_by(job_with_list_values, 'min_salary')


def test_sort_by_date_posted_criteria():
    assert sort_by(job_list, 'date_posted') == job_list_ordened_by_posted_date


def test_sort_with_date_posted_str():
    with pytest.raises(NameError):
        sort_by(job_with_invalid_str_values, 'date_posted')


def test_sort_with_date_posted_list():
    with pytest.raises(NameError):
        sort_by(job_with_list_values, 'date_posted')
