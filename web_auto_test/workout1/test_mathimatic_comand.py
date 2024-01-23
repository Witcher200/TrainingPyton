from conftest import set_up
import pytest

@pytest.mark.parametrize('x, y, result', [(4, 4, 8),
														(1928, 82940, 84868),
														(1, 1, 2),
														(30, -4, 26)])
def test_sum_number(x, y, result, set_up):
	assert x + y == result
	assert x + y == result
	
@pytest.mark.parametrize('x, y, result', [(10, 5, 5),
														(20, 10, 10),
														(50, 30, 20),
														(-53, 11, -64)])
def test_minus_number(x, y, result, set_up):
	assert x - y == result
	assert x - y == result

@pytest.mark.parametrize('x, y, result', [(98,5, 588),
														(100, 10, 1000),
														(-39, 50, -1500),
														(4, 4, 16)])
def test_multiplication_number(x, y, result, set_up):
	assert x * y == result
	assert x * y == result

@pytest.mark.parametrize('x, y, result', [()])