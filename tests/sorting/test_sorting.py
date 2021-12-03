import pytest
from src.sorting import sort_by


@pytest.fixture()
def jobs():
    return [
        {'date_posted': '06/12/21', 'max_salary': '', 'min_salary': 56},
        {'date_posted': '01/10/21', 'max_salary': 300, 'min_salary': 50},
        {'date_posted': '10/12/21', 'max_salary': 1000, 'min_salary': 20},
        {'date_posted': '02/12/21', 'max_salary': 200, 'min_salary': 110},
    ]


def test_sort_by_criteria(jobs):
    assert sort_by(jobs, 'max_salary') is None
