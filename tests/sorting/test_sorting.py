import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    with pytest.raises(ValueError, match="invalid sorting criteria: Error"):
        sort_by([{}, {}], "Error")
