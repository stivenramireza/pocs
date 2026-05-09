import pytest

from src.complex_job import find_highest_calorie_cereal, diamond


@pytest.fixture(scope='module')
def cereals():
    return [
        {"name": "hi-cal cereal", "calories": 400},
        {"name": "lo-cal cereal", "calories": 50},
    ]


def test_find_highest_calorie_cereal(cereals):
    result = find_highest_calorie_cereal(cereals)
    assert result == 'hi-cal cereal'


def test_diamond():
    result = diamond.execute_in_process()
    assert result.success
    assert result.output_for_node('find_highest_protein_cereal') == 'Special K'
