from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 10000, "min_salary": 200, "date_posted": "09-12-2021"},
        {"max_salary": 15000, "min_salary": 10, "date_posted": "10-12-2021"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "11-12-2021"},
        {"max_salary": 100, "min_salary": 15},
        {"max_salary": 130, "date_posted": "14-12-2021"},
        {"min_salary": 70, "date_posted": "05-12-2021"},
    ]
    assert sort_by(jobs, "max_salary") == [
        {"max_salary": 15000, "min_salary": 10, "date_posted": "10-12-2021"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "09-12-2021"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "11-12-2021"},
        {"max_salary": 130, "date_posted": "14-12-2021"},
        {"max_salary": 100, "min_salary": 15},
        {"min_salary": 70, "date_posted": "05-12-2021"},
    ]

    assert sort_by(jobs, "min_salary") == [
        {"max_salary": 1500, "min_salary": 0, "date_posted": "09-12-2021"},
        {"max_salary": 15000, "min_salary": 10, "date_posted": "10-12-2021"},
        {"max_salary": 100, "min_salary": 15}
        {"min_salary": 70, "date_posted": "05-12-2021"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "11-12-2021"},
        {"max_salary": 130, "date_posted": "14-12-2021"},
    ]

    assert sort_by(jobs, "date_posted") == [
        {"max_salary": 130, "date_posted": "14-12-2021"}
        {"max_salary": 1500, "min_salary": 0, "date_posted": "11-12-2021"},
        {"max_salary": 15000, "min_salary": 10, "date_posted": "10-12-2021"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "09-12-2021"},
        {"min_salary": 10, "date_posted": "05-12-2021"},
        {"max_salary": 100, "min_salary": 15}
    ]
