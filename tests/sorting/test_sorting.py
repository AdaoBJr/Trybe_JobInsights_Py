from src.sorting import sort_by

MIN_SALARY = "min_salary"
MAX_SALARY = "max_salary"
DATE_POSTED = "date_posted"

mock = [
    {
        "min_salary": 1000,
        "max_salary": 5000,
        "date_posted": "2021-12-09",
    },
    {
        "min_salary": 6000,
        "max_salary": 10000,
        "date_posted": "2021-07-19",
    },
    {
        "min_salary": 11000,
        "max_salary": 15000,
        "date_posted": "2021-02-01",
    },
]

min_salary_asc = [
    mock[0],
    mock[1],
    mock[2],
]

max_salary_desc = [
    mock[2],
    mock[1],
    mock[0],
]

date_posted_desc = [
    mock[2],
    mock[1],
    mock[0],
]


def test_sort_by_criteria():
    # minimum salary ascendent
    sort_by(mock, MIN_SALARY)
    assert mock == min_salary_asc
    # maximum salary descendent
    sort_by(mock, MAX_SALARY)
    assert mock == max_salary_desc
    # date posted descendent
    sort_by(mock, DATE_POSTED)
    assert mock == date_posted_desc
