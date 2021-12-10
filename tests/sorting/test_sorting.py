from src.sorting import sort_by

test = [
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2021-12-02"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2021-12-03"},
    {"max_salary": 1600, "min_salary": 100, "date_posted": "2021-12-01"},
]

ordered = [
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2021-12-03"},
    {"max_salary": 1600, "min_salary": 100, "date_posted": "2021-12-01"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2021-12-02"},
]


def test_sort_by_criteria():
    sort_by(test, "min_salary")
    assert test == ordered
