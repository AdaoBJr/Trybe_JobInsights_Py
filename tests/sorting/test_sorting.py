from src.sorting import sort_by
import pytest

# recebi a ajuda do Eder Paixa e Lara Capila para a resolução dos requisito 8, 9 e 10

jobs = [
    {"min_salary": 2500, "max_salary": 3500, "date_posted": "2021-12-01"},
    {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-11-01"},
    {"min_salary": 1500, "max_salary": 2500, "date_posted": "2021-10-01"},
]

min_salary_ordered = [jobs[2], jobs[1], jobs[0]]
max_salary_ordered = [jobs[0], jobs[1], jobs[2]]
date_ordered = [jobs[0], jobs[1], jobs[2]]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == min_salary_ordered
    sort_by(jobs, "max_salary")
    assert jobs == max_salary_ordered
    sort_by(jobs, "date_posted")
    assert jobs == date_ordered

    with pytest.raises(ValueError, match='invalid sorting'):
        sort_by(jobs, 'premium')
