from src.sorting import sort_by
from src.insights import get_max_salary
from src.jobs import read


def test_sort_by_criteria():
    jobs = read("src/jobs.csv")
    criteria = "max_salary"

    sort_by(jobs, criteria)
    sort_jobs = jobs[0][criteria]

    assert type(jobs) is list
    assert sort_jobs == str(get_max_salary("src/jobs.csv"))
