from code import Toggler

foo = Toggler()

sample = []
for i in range(10):
	sample.append(foo.get())
if sample == [True, False, True, False, True, False, True, False, True, False]:
	print("Test Case 1 Passed!")
else:
	print("Test Case 1 Failed, read a Toggler 10 times and got", sample)