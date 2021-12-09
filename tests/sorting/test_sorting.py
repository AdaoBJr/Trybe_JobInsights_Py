from src.sorting import sort_by
from src.insights import get_min_salary
from src.jobs import read

# ME AUXILIEI NO CÓDIGO DE ANDRE ARNONI TURMA 10 - B


def test_sort_by_criteria():
    jobs_file = read("src/jobs.csv")

    sort_by(jobs_file, "min_salary")
    sorted = jobs_file[0]["min_salary"]

    assert type(jobs_file) is list
    assert sorted == str(get_min_salary("src/jobs.csv"))
