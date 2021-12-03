from src.sorting import sort_by


def test_sort_by_criteria():
    assert sort_by([
                        {"job_title": "Engenheiro"},
                        {"job_title": "Desenvolvedor"}
                    ], "min_salary") is None
