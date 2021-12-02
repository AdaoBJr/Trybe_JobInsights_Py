from src.sorting import sort_by
import pytest


jobs = [
    {"max_salary": 15000, "min_salary": 0, 'date_posted': '2020-01-01'},
    {"max_salary": 10, "min_salary": 100, 'date_posted': '2011-01-01'},
    {"max_salary": 10000, "min_salary": 200, 'date_posted': '2014-01-01'},
    {"max_salary": 0, "min_salary": 10, 'date_posted': '2013-01-01'},
    {"max_salary": 1500, "min_salary": 0, 'date_posted': '2012-01-01'},
]

resultMax = [
    jobs[0],
    jobs[2],
    jobs[4],
    jobs[1],
    jobs[3]
]

resultMin = [
    jobs[0],
    jobs[4],
    jobs[3],
    jobs[1],
    jobs[2]
]

resultDate = [
    jobs[0],
    jobs[2],
    jobs[3],
    jobs[4],
    jobs[1]
]


def test_sort_by_criteria():
    sort_by(jobs, 'max_salary')
    assert jobs == resultMax

    sort_by(jobs, 'min_salary')
    assert jobs == resultMin

    sort_by(jobs, 'date_posted')
    assert jobs == resultDate

    # with pytest.raises(ZeroDivisionError, match='division by zero'):
    #     divide(2,0)

    with pytest.raises(ValueError, match='invalid sorting criteria: Py > Js'):
        sort_by(jobs, 'Py > Js')
        assert print('Noooo! Just kidding :)')


#     x = [
#     {"max_salary": 15000, "min_salary": 0, 'date_posted': '2020-01-01'},
#     {"max_salary": 10, "min_salary": 100, 'date_posted': '2011-01-01'},
#     {"max_salary": 10000, "min_salary": 200, 'date_posted': '2014-01-01'},
#     {"max_salary": 0, "min_salary": 10, 'date_posted': '2013-01-01'},
#     {"max_salary": 1500, "min_salary": 0, 'date_posted': '2012-01-01'},
# ]

# def myFunc(e):
#   return e['max_salary']

# a = x.sort(key=myFunc)
# print(x)
