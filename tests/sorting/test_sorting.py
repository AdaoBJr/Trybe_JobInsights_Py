from src.sorting import sort_by


def test_sort_by_criteria():
    assert (
        sort_by([
            {"job_title": "Full Stack Developer"},
            {"company": "Trybe"}
        ], "min_salary") is None
    )
