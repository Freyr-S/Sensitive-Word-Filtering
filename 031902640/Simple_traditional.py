from hanziconv import HanziConv


def tradition2sim(txt):

    traditional = HanziConv.toTraditional(txt)
    return traditional
