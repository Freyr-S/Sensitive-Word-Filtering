import pypinyin


def get_pinyin(txt):

    gap = ''
    piny = gap.join(pypinyin.lazy_pinyin(txt))
    return piny
