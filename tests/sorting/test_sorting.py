from src.sorting import sort_by


def test_sort_by_criteria():
    assert (
        sort_by(
            [{'title_job': 'Senior Software Engineer', 'Company': 'Google'}],
            'min_salary',
        )
        is None
    )
