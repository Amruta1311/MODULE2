def realtime(x):

	lt = list(x.split(","))
	x = ""
	if int(lt[1]) > 85:
		x = x + ', CPU UTILZATION VIOLATED'
	if int(lt[2]) > 75:
		x = x + ', MEMORY UTILZATION VIOLATED'
	if int(lt[3]) > 60:
		x = x + ', DISK UTILIZATION VIOLATED'
	if x != "":
		x = "(ALERT," + str(lt[0]) + x + ")"
	elif x == "":
		x = "(NO ALERT," + str(lt[0]) + ")"
	return x

def test():
	assert realtime("1234,7,7,7") == "(NO ALERT,1234)",'ERROR'
	assert realtime("1234,89,89,89") == "(ALERT,1234, CPU UTILZATION VIOLATED, MEMORY UTILZATION VIOLATED, DISK UTILIZATION VIOLATED)",'ERROR'
	assert realtime("234,96,67,45") == "(ALERT,234, CPU UTILZATION VIOLATED)",'ERROR'
	assert realtime("234,67,97,45") == "(ALERT,234, MEMORY UTILZATION VIOLATED)",'ERROR'
	assert realtime("234,67,70,80") == "(ALERT,234, DISK UTILIZATION VIOLATED)",'ERROR'

if __name__ == '__main__':
	test()
	print("All Unit Test Cases Passed.")