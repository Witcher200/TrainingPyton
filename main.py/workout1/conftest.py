import pytest

@pytest.fixture()
def set_up():
	print('Выполнение теста')
	yield
	print('Конец выполнения теста')

@pytest.fixture(scope='module')
def test_sum_number_1():
	print('Начало')
	yield
	print('Конец')