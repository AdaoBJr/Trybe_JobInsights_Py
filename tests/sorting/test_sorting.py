from src.sorting import sort_by
import pytest


def test_sort_by_criteria():
    jobs = [
        {'min_salary': '91443', 'max_salary': '155868',
         'date_posted': '2020-05-02'},
        {'min_salary': '44587', 'max_salary': '82162',
         'date_posted': '2020-05-08'},
        {'min_salary': '122296', 'max_salary': '148734',
         'date_posted': '2020-04-28'},
           ]

    criteria = 'min_salary'
    expectResult = [
                    {'min_salary': '44587', 'max_salary': '82162',
                     'date_posted': '2020-05-08'},
                    {'min_salary': '91443', 'max_salary': '155868',
                     'date_posted': '2020-05-02'},
                    {'min_salary': '122296', 'max_salary': '148734',
                     'date_posted': '2020-04-28'},
                   ]
    sort_by(jobs, criteria)
    assert jobs == expectResult

    criteria = 'max_salary'
    expectResult = [
                    {'min_salary': '91443', 'max_salary': '155868',
                     'date_posted': '2020-05-02'},
                    {'min_salary': '122296', 'max_salary': '148734',
                     'date_posted': '2020-04-28'},
                    {'min_salary': '44587', 'max_salary': '82162',
                     'date_posted': '2020-05-08'},
                   ]
    sort_by(jobs, criteria)
    assert jobs == expectResult

    criteria = 'date_posted'
    expectResult = [
                    {'min_salary': '44587', 'max_salary': '82162',
                     'date_posted': '2020-05-08'},
                    {'min_salary': '91443', 'max_salary': '155868',
                     'date_posted': '2020-05-02'},
                    {'min_salary': '122296', 'max_salary': '148734',
                     'date_posted': '2020-04-28'},
                   ]
    sort_by(jobs, criteria)
    assert jobs == expectResult

    criteria = 'xablau'
    # with pytest.raises(KeyError):
    with pytest.raises(ValueError,
                       match=f"invalid sorting criteria: {criteria}"):
        sort_by(jobs, criteria)
