COMS = [".com", ".net", ".org", ".io", ".gg"]



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
    return "Site opened! Process %s" % search.pid


def youtubeSearch(keywords):
    import subprocess
    search = subprocess.Popen(['firefox', 'https://www.youtube.com/search?q=%s'%keywords])
    return "Search launched! Process %s" % search.pid


def opener(keywords):
    for com in COMS:
        if com in keywords:
            ewOp = keywords.split(" ")
            for chunk in ewOp:
                if com in chunk:
                    site = chunk
            return openSite(site)
    #execute() we got a hash problem :thinking:



if __name__ == "__main__":
    print basicArithmatic("3*4+1")
    print searchImageSpecific("test")