from vector import Vector
from decimal import *

TEST_PRECISION = 12

def test(answer, control):
	if type(answer) is Vector and type(control) is Vector:
		answer_coords = [round(Decimal(x), TEST_PRECISION) for x in answer.coordinates]
		control_coords = [round(Decimal(x), TEST_PRECISION) for x in control.coordinates]
		if answer_coords != control_coords:
			print("Expected: {0}; Got: {1} ".format(control_coords, answer_coords))
			raise Exception('Test not passed')
	elif type(answer) is bool and type(control) is bool:
		if answer != control:
			print("Expected: {0}; Got: {1} ".format(control, answer))
			raise Exception('Test not passed')
	else:
		if round(Decimal(answer), TEST_PRECISION) != round(Decimal(control), TEST_PRECISION):
			print("Expected: {0}; Got: {1} ".format(control, answer))
			raise Exception('Test not passed')


v411 = Vector(['8.218', '-9.341'])
v412 = Vector(['-1.129', '2.111'])
v421 = Vector(['7.119', '8.215'])
v422 = Vector(['-8.223', '0.878'])
v43 = Vector(['1.671', '-1.012', '-0.318'])
# print(v411 + v412)
# print(v421 - v422)
# print(v43.mul_scalar(7.41))
test(v411 + v412, Vector(['7.089', '-7.23']))
test(v421 - v422, Vector(['15.342', '7.337']))
test(v43.mul_scalar('7.41'), Vector(['12.38211', '-7.49892', '-2.35638']))


v61 = Vector(['-0.221', '7.437'])
v62 = Vector(['8.813', '-1.331', '-6.247'])
v63 = Vector(['5.581', '-2.136'])
v64 = Vector(['1.996', '3.108', '-4.554'])
# print(v61.mag())
# print(v62.mag())
# print(v63.norm())
# print(v64.norm())
test(v61.mag(), '7.440282924728064')
test(v62.mag(), '10.88418756729229')
test(v63.norm(), Vector(['0.9339352140866404', '-0.35744232526233']))
test(v64.norm(), Vector(['0.3404012959433013', '0.5300437012984872', '-0.7766470449528027']))


v811 = Vector(['7.887', '4.138'])
v812 = Vector(['-8.802', '6.776'])
v821 = Vector(['-5.955', '-4.904', '-1.874'])
v822 = Vector(['-4.496', '-8.755', '7.103'])
v831 = Vector(['3.183', '-7.627'])
v832 = Vector(['-2.668', '5.319'])
v841 = Vector(['7.35', '0.221', '5.188'])
v842 = Vector(['2.751', '8.259', '3.985'])
# print(v811.dot(v812))
# print(v821.dot(v822))
# print(v831.ang(v832, False))
# print(v841.ang(v842))
test(v811.dot(v812), '-41.382286')
test(v821.dot(v822), '56.397178')
test(v831.ang(v832, False), '3.0720263098372507')
test(v841.ang(v842), '60.275811205230916')


v1011 = Vector(['-7.579', '-7.88'])
v1012 = Vector(['22.737', '23.64'])
v1021 = Vector(['-2.029', '9.97', '4.172'])
v1022 = Vector(['-9.231', '-6.639', '-7.245'])
v1031 = Vector(['-2.328', '-7.284', '-1.214'])
v1032 = Vector(['-1.821', '1.072', '-2.94'])
v1041 = Vector(['2.118', '4.827'])
v1042 = Vector(['0', '0'])
# print(v1011.ang(v1012))
# print(v1011.is_orthogonal_to(v1012))
# print(v1011.is_parallel_to(v1012))
# print(v1021.ang(v1022))
# print(v1021.is_orthogonal_to(v1022))
# print(v1021.is_parallel_to(v1022))
# print(v1031.ang(v1032))
# print(v1031.is_orthogonal_to(v1032))
# print(v1031.is_parallel_to(v1032))
# print(v1041.is_orthogonal_to(v1042))
# print(v1041.is_parallel_to(v1042))
test(v1011.is_orthogonal_to(v1012), False)
test(v1011.is_parallel_to(v1012), True)
test(v1021.is_orthogonal_to(v1022), False)
test(v1021.is_parallel_to(v1022), False)
test(v1031.is_orthogonal_to(v1032), True)
test(v1031.is_parallel_to(v1032), False)
test(v1041.is_orthogonal_to(v1042), True)
test(v1041.is_parallel_to(v1042), True)



print('All tests were passed successfully')