import pytest

class example:
	def square_eq_solver(a, b, c):
		example.result = []
		example.discriminant =  b * b - 4 * a * c

		if example.discriminant == 0:
			example.result.append(-b / (2 * a))
		elif example.discriminant > 0:


			example.result.append((-b + sqrt(discriminant)) / (2 * a))
			example.result.append((-b - sqrt(discriminant)) / (2 * a))

		return example.result	

		
class test_exapmle(example):
	def test_no_root():
	   example.result = square_eq_solver(10, 0 ,2)
	   assert len() == 0

	def test_single_root():
	   example.result = square_eq_solver(10, 0, 0)
	   assert len(res) == 1
	   assert result == [0]

	def test_multiple_root():
	   res = square_eq_solver(2, 5, -3)
	   assert len(res) == 3
	   assert res == [0.5, -3] 

e = test_example()
e.square_eq_solver()
	# команда для вызова теста в терминале   pytest.exe src/main/example/example.py