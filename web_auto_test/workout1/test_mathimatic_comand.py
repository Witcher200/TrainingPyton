from conftest import set_up
from mathimatic_comand import *
import pytest

@pytest.mark.parametrize('x, y, result', [(4, 4, 8),
														(1928, 82940, 84868),
														(1, 1, 2),
														(30, -4, 26)])
def test_adition_number(x, y, result, set_up):
	assert adition(x, y) == result


@pytest.mark.parametrize('x, y, result', [(10, 5, 5),
														(20, 10, 10),
														(50, 30, 20),
														(-53, 11, -64)])
def test_subtraction_number(x, y, result):
	assert subtraction(x, y) == result


@pytest.mark.parametrize('x, y, result', [(98,5, 490),
														(100, 10, 1000),
														(-39, 50, -1950),
														(4, 4, 16)])
def test_multiplication_number(x, y, result):
	assert multiplication(x, y) == result


@pytest.mark.parametrize('x, y, result', [(50, 10, 5),
																					(10, 2, 5),
																					(6,3, 2),
																					(100, 10, 10)])
def test_division_number(x, y, result):
	assert division(x, y) == result


@pytest.mark.parametrize("expected_excaption, divider, divisionable",
												 											[(ZeroDivisionError, 0, 10),
																							(TypeError, "2", 13)])
def test_division_with_erroe(expected_excaption, divider, divisionable):
	with pytest.raises(expected_excaption):
		division(divisionable, divider)