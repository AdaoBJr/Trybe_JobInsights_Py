# from src.sorting import sort_by
from pytest import fixture
from src.sorting import sort_by


@fixture
def data():
    return [
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2021-12-14"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2020-12-14"},
        {"min_salary": 5000, "max_salary": 6000, "date_posted": "2019-12-14"},
        {"min_salary": 7000, "max_salary": 8000, "date_posted": "2018-12-14"},
        {"min_salary": 7000, "max_salary": 8000, "date_posted": "2017-12-14"},
        {"min_salary": 7000, "max_salary": 8000, "date_posted": "2016-12-14"},
        {"min_salary": 7000, "max_salary": 8000, "date_posted": "2015-12-14"},
    ]


def test_sort_by_criteria(data):
    sort_by(data, "min_salary")
    min_salary = []
    for minimum in data:
        min_salary.append(minimum["min_salary"])
    assert min_salary == sorted(min_salary)

    sort_by(data, "max_salary")
    max_salary = []
    for maximum in data:
        max_salary.append(maximum["max_salary"])
    assert max_salary == sorted(max_salary, reverse=True)

    sort_by(data, "date_posted")
    date_posted = []
    for date in data:
        date_posted.append(date["date_posted"])
    assert date_posted == sorted(date_posted, reverse=True)
