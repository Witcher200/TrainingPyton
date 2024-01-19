import pytest
from mathimatic_operation import *

def test_edition():
	assert edition(7, 66)
	
print('')

def test_subtraction():
	assert subtraction(15, 6)

print(' ')

def test_division():
	assert division(6, 3)

print(' ')

def test_multiplication():
	assert multiplication(1, 1)	