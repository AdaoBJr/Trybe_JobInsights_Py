from src.sorting import sort_by
import pytest


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by('xablau')

    with pytest.raises(AttributeError):
        sort_by('xablau', 'max_salary')
