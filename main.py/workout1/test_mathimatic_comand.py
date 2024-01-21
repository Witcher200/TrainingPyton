import pytest

from conftest import set_up

def test_sum_number(set_up):
	assert 4+4 == 8
	assert 1928+82940 == 84868
	
def test_minus_number(set_up):
	assert 4-4 == 0
	assert 16-9 == 7

def test_multiplication_number(set_up):
	assert 98*6 == 588
	assert 100*10 == 1000