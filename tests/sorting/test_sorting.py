import pytest
from src.sorting import sort_by
from src.jobs import read
from src.insights import get_min_salary


def test_sort_by_criteria():
    path = 'src/jobs.csv'
    jobs = read(path)

    criteria1 = 'batata'
    criteria2 = 'min_salary'

    assert sort_by(jobs, criteria2)[0][criteria2] == get_min_salary(path)
    assert type(sort_by(jobs, criteria2)) == list
    assert len(sort_by(jobs, criteria2)) == len(jobs)

    with pytest.raises(
        ValueError,
        match=f'invalid sorting criteria: {criteria1}'
    ):
        sort_by(jobs, criteria1)
