
def basicArithmatic(strEquation):
	return eval(strEquation)


def searchSpecific(keywords):
	import subprocess
	search = subprocess.Popen(['firefox', 'https://www.google.com/search?q=%s'%keywords])
	return "Search launched! Process %s" % search.pid


print basicArithmatic("3*4+1")
print searchSpecific("test")