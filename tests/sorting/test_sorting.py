from src.sorting import sort_by
import pytest

job_list = [
    {'min_salary': 0, 'max_salary': 2000, 'date_posted': '2021-12-00'},
    {'min_salary': 500, 'max_salary': 1000, 'date_posted': '2021-06-00'},
    {'min_salary': 250, 'max_salary': 4000, 'date_posted': '2021-08-00'},
    {'min_salary': 1000, 'max_salary': 3000, 'date_posted': '2021-10-00'},
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

job_list_ordened_by_date_posted = [
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


def test_sort_by_criteria():
    assert sort_by(job_list, 'max_salary') == job_list_ordened_by_max_salary
    assert sort_by(job_list, 'min_salary') == job_list_ordened_by_min_salary
    assert sort_by(job_list, 'date_posted') == job_list_ordened_by_date_posted
    with pytest.raises(ValueError):
        sort_by([], 'invalid_criteira')
    with pytest.raises(ValueError):
        sort_by(job_with_invalid_str_values, 'max_salary')
    with pytest.raises(TypeError):
        sort_by(job_with_list_values, 'max_salary')
    with pytest.raises(ValueError):
        sort_by(job_with_invalid_str_values, 'min_salary')
    with pytest.raises(TypeError):
        sort_by(job_with_list_values, 'min_salary')
    with pytest.raises(NameError):
        sort_by(job_with_invalid_str_values, 'date_posted')
    with pytest.raises(NameError):
        sort_by(job_with_list_values, 'date_posted')
    assert sort_by(job_list, 'max_salary') == job_list_ordened_by_max_salary


# def test_sort_by_min_salary():
#     assert sort_by(job_list, 'min_salary') == job_list_ordened_by_min_salary


# def test_sort_by_date_posted():
# assert sort_by(job_list, 'date_posted') == job_list_ordened_by_date_posted


# def test_sort_by_when_a_invalid_criteria_is_sent():
#     with pytest.raises(ValueError):
#         sort_by([], 'invalid_criteira')
