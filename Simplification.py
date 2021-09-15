from hanziconv import HanziConv


def simplification(text):

    simple = HanziConv.toSimplified(text)
    return simple
