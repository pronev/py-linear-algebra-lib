from vector import Vector
from decimal import *
getcontext().prec = 16

def test(answer, true_answer):
	if type(answer) is Vector and type(true_answer) is Vector:
		if answer != true_answer:
			raise Exception('Test not passed')
	else:
		if Decimal(str(answer)) != Decimal(str(true_answer)):
			raise Exception('Test not passed')


v411 = Vector([8.218, -9.341])
v412 = Vector([-1.129, 2.111])
v421 = Vector([7.119, 8.215])
v422 = Vector([-8.223, 0.878])
v43 = Vector([1.671, -1.012, -0.318])
# print(v411 + v412)
# print(v421 - v422)
# print(v43.mul_scalar(7.41))
test(v411 + v412, Vector([7.089, -7.23]))
test(v421 - v422, Vector([15.342, 7.337]))
test(v43.mul_scalar(7.41), Vector([12.38211, -7.49892, -2.35638]))


v61 = Vector([-0.221, 7.437])
v62 = Vector([8.813, -1.331, -6.247])
v63 = Vector([5.581, -2.136])
v64 = Vector([1.996, 3.108, -4.554])
# print(v61.mag())
# print(v62.mag())
# print(v63.norm())
# print(v64.norm())
test(v61.mag(), 7.440282924728064)
test(v62.mag(), 10.88418756729229)
test(v63.norm(), Vector([0.9339352140866404, -0.35744232526233]))
test(v64.norm(), Vector([0.3404012959433013, 0.5300437012984872, -0.7766470449528027]))


v811 = Vector([7.887, 4.138])
v812 = Vector([-8.802, 6.776])
v821 = Vector([-5.955, -4.904, -1.874])
v822 = Vector([-4.496, -8.755, 7.103])
v831 = Vector([3.183, -7.627])
v832 = Vector([-2.668, 5.319])
v841 = Vector([7.35, 0.221, 5.188])
v842 = Vector([2.751, 8.259, 3.985])
# print(v811*v812)
# print(v821*v822)
# print(v831.ang_rad(v832))
# print(v841.ang(v842))
test(v811*v812, -41.38228599999998)
test(v821*v822, 56.39717800000000)
test(v831.ang_rad(v832), 3.072026309837249)
test(v841.ang(v842), 60.27581120523091)
















print('All tests were passed successfully')