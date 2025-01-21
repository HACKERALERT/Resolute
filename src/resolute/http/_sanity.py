from multiprocessing import cpu_count

try:
	assert False == True
except AssertionError:
	pass
else:
	raise Exception("Assertions are not enabled!")

assert cpu_count()

sane = True
