import hug

@hug.get("/hello_world")
def hello_world():
	return "hello world"