# import pytest

from src.sorting import sort_by
from src.jobs import read
from src.insights import get_min_salary


def test_sort_by_criteria():
    path = 'src/jobs.csv'
    jobs = read(path)

    criteria2 = 'min_salary'
    # criteria1 = 'batata'

    # try:
    #     sort_by(jobs, criteria1)
    # except KeyError:
    #     raise AssertionError

    # with pytest.raises(
    #     ValueError,
    #     match=f'invalid sorting criteria: {criteria1}'
    # ):
    #     print(type(jobs))
    #     print(len(jobs))

    sort_by(jobs, criteria2)

    assert type(jobs) == list
    assert jobs[0][criteria2] == str(get_min_salary(path))
