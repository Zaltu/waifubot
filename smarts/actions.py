
def basicArithmatic(strEquation):
    return eval(strEquation)


def searchSpecific(keywords):
    import subprocess
    search = subprocess.Popen(['firefox', 'https://www.google.com/search?q=%s'%keywords])
    return "Search launched! Process %s" % search.pid


def execute(program, keywords=""):
    import subprocess
    search = subprocess.Popen([program, keywords])
    return "%s launched! Process %s" % (program, search.pid)


def searchImageSpecific(keywords):
    import subprocess
    search = subprocess.Popen(['firefox', 'https://www.google.com/search?q=%s&tbm=isch'%keywords])
    return "Search launched! Process %s" % search.pid


def openSite(site):
    import subprocess
    search = subprocess.Popen(['firefox', 'https://%s'%site])
    return "Search launched! Process %s" % search.pid


def youtubeSearch(keywords):
    import subprocess
    search = subprocess.Popen(['firefox', 'https://www.youtube.com/search?q=%s'%keywords])
    return "Search launched! Process %s" % search.pid



if __name__ == "__main__":
    print basicArithmatic("3*4+1")
    print searchImageSpecific("test")