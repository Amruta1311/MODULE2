There are 3 parts of this folder attached -->
1.) realtime.py ==> Checks the realtime conditions and provides the alert/no alert based on it and can be run by the command 'python realtime.py'
2.) To develop rest api based interaction system we have the api folder, __main__.py and test.py ==> __main__.py is run in the virtual environment 
using the command 'python __main__.py' and test.py is run on a separate command prompt outside the virtual environment with the command 'python test.py'. 
We give the input on running the test.py file and get the desired output. The __main__.py is run on the url http://127.0.0.1:5000/. For example ->

The URL : http://127.0.0.1:5000/?x=1234,29,29,29
will provide the following output in JSON format:

{
  "alert": "(NO ALERT,1234)"
}

The URL : http://127.0.0.1:5000/?x=1234,67,78,89
will provide the following output in JSON format:

{
  "alert": "(ALERT,1234, MEMORY UTILZATION VIOLATED, DISK UTILIZATION VIOLATED)"
}

3.) unittest.py ==> There are 5 unit test cases that return an OK status after implementing them using assert thus assuring that the code is working and 
giving the desired output. This can be run by the command 'python unittest.py'