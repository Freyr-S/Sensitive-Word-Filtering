from hanziconv import HanziConv


def sim2tradition(txt):

    simple = HanziConv.toSimplified(txt)
    return simple

def tradition2sim(txt):

    traditional = HanziConv.toTraditional(txt)
    return traditional
