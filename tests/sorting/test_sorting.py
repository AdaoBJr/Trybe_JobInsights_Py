from src.sorting import sort_by


list_dicts = [
    {
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": "2022-01-01",
        "status": "SP",
    },
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2022-01-02",
        "status": "RJ",
    },
    {
        "min_salary": 5000,
        "max_salary": 10000,
        "date_posted": "2022-01-03",
        "status": "MA",
    },
]

list_asc_by_min = [
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2022-01-02",
        "status": "RJ",
    },
    {
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": "2022-01-01",
        "status": "SP",
    },
    {
        "min_salary": 5000,
        "max_salary": 10000,
        "date_posted": "2022-01-03",
        "status": "MA",
    },
]

list_desc_by_max = [
    {
        "min_salary": 5000,
        "max_salary": 10000,
        "date_posted": "2022-01-03",
        "status": "MA",
    },
    {
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": "2022-01-01",
        "status": "SP",
    },
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2022-01-02",
        "status": "RJ",
    },
]

list_desc_by_date = [
    {
        "min_salary": 5000,
        "max_salary": 10000,
        "date_posted": "2022-01-03",
        "status": "MA",
    },
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2022-01-02",
        "status": "RJ",
    },
    {
        "min_salary": 2000,
        "max_salary": 4000,
        "date_posted": "2022-01-01",
        "status": "SP",
    },
]


def test_sort_by_criteria():

    sort_by(list_dicts, "min_salary")
    assert list_dicts == list_asc_by_min

    sort_by(list_dicts, "max_salary")
    assert list_dicts == list_desc_by_max

    sort_by(list_dicts, "date_posted")
    assert list_dicts == list_desc_by_date
