from flask import Flask, jsonify, request


app = Flask(__name__)



@app.route('/',methods=['GET'])
def index():
	x = request.args.get('x')
	lt = list(x.split(","))
	server_id = lt[0]
	cpu_util = lt[1]
	disk_util = lt[2]
	resource_util = lt[3]
	resp_data = {}
	resp_data['alert'] = ''
	x = ''
	if int(cpu_util) > 85:
		x = x + ', CPU UTILZATION VIOLATED'

	if int(resource_util) > 75:
		x = x + ', MEMORY UTILZATION VIOLATED'

	if int(disk_util) > 60:
		x = x + ', DISK UTILIZATION VIOLATED'

	if x != "":
		resp_data['alert'] = "(ALERT," + str(server_id) + x + ")"

	elif x == "":
		resp_data['alert'] = "(NO ALERT," + str(server_id) + ")"
	return resp_data