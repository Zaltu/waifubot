COMS = [".com", ".net", ".org", ".io", ".gg"]
OMIT_WORDS = {"of", "a", "the", "for"}


def basicArithmatic(strEquation):
    return eval(strEquation)


def searchSpecific(keywords):
    import subprocess
    search = subprocess.Popen(['firefox', 'https://www.google.com/search?q=%s'%keywords])
    return "Search launched! Process %s" % search.pid


def execute(program, keywords=None):
    import subprocess
    program = subprocess.Popen([program, keywords] if keywords else [program])
    return "%s launched! Process %s" % (program, program.pid)


def searchImageSpecific(keywords):
    import subprocess
    search = subprocess.Popen(['firefox', 'https://www.google.com/search?q=%s&tbm=isch'%keywords])
    return "Search launched! Process %s" % search.pid


def openSite(site):
    import subprocess
    browser = subprocess.Popen(['firefox', 'https://%s'%site])
    return "Site opened! Process %s" % browser.pid


def youtubeSearch(keywords):
    import subprocess
    search = subprocess.Popen(['firefox', 'https://www.youtube.com/search?q=%s'%keywords])
    return "Search launched! Process %s" % search.pid


def opener(keywords, terms=""):
    for com in COMS:
        if com in keywords:
            ewOp = keywords.split(" ")
            for chunk in ewOp:
                if com in chunk:
                    site = chunk
            return openSite(site)
    command = terms.split(" ")
    print command
    try:
        return execute(command[0], command[1:] or None)
    except OSError:
        return "That program isn't in the PATH..."


def interface(commandKeyword, command, fullTerms):
    import re
    fullTerms = re.sub('[!@#$,:;?]', '', fullTerms)
    words = set(fullTerms.split(" "))
    terms = words.difference(set(commandKeyword.split(" "))).difference(OMIT_WORDS)
    print "Command: %s\nFunction: %s\nKeywords: %s" % (commandKeyword, command, terms)
    if command is opener:
        return command(' '.join(terms), ' '.join(fullTerms.split(" ")[fullTerms.split(" ").index(commandKeyword)+1:]))  # This is the cancer :stringmanipulation:
    return command(' '.join(terms))



if __name__ == "__main__":
    print basicArithmatic("3*4+1")
    print searchImageSpecific("test")
