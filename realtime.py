x = input()
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

print(x)
	