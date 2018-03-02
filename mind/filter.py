import sys
from smarts import actions

COMMAND_KEYWORDS = {
    "calculate":actions.basicArithmatic,
    "search":actions.searchSpecific,
    "search video":actions.youtubeSearch,
    "search videos":actions.youtubeSearch,
    "search image":actions.searchImageSpecific,
    "search images":actions.searchImageSpecific,
    "search picture":actions.searchImageSpecific,
    "search pictures":actions.searchImageSpecific,
    "search pic":actions.searchImageSpecific,
    "search pics":actions.searchImageSpecific,
    "open":actions.opener
}

OMIT_WORDS = {
    "of", "a", "the", "for"
}

def textFilter(text):
    words = set(text.split(" "))
    most = 0
    command = None
    for key in COMMAND_KEYWORDS:
        #print set(key.split(" "))
        #print words
        #print set(key.split(" ")).intersection(words)
        #print most
        intNum = len(set(key.split(" ")).intersection(words))
        #print intNum
        if most < intNum or (most == intNum and len(set(key.split(" ")))<len(set(command.split(" "))) if command else 0):
            most = intNum
            command = key

    comRet = None
    if command:
        terms = ' '.join(words.difference(set(command.split(" "))).difference(OMIT_WORDS))
        if COMMAND_KEYWORDS[command]:
            comRet = COMMAND_KEYWORDS[command](terms)
        print "Command: %s\nFunction: %s\nKeywords: %s" % (command, COMMAND_KEYWORDS[command], terms)


    prin = "Answer :)\n"
    if comRet:
        prin += str(comRet)
    print prin



if __name__ == "__main__":
    textFilter(sys.argv[1])
    #textFilter("calculate 4*13/2+1")
    #textFilter("hey, open www.github.com please")
    #textFilter("image search very fast of dog running at incredibly high speed")

