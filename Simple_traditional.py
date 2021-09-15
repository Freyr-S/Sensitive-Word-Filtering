from hanziconv import HanziConv


def sim2tradition(text):

    simple = HanziConv.toSimplified(text)
    return simple

def tradition2sim(text):

    traditional = HanziConv.toTraditional(text)
    return traditional
