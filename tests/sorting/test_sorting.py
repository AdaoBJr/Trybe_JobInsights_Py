import pytest
from src.sorting import sort_by
from pytest import fixture


@fixture
def test_sort_by_criteria():
    with pytest.raises(ValueError):
        sort_by([], "not a valid criteria")
        sort_by("not a valid job", "min_salary")
        sort_by([{"still": "not", "a": "valid", "job": ""}], "max_salary")
    pass
