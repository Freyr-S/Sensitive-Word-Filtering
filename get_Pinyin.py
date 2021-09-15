import pypinyin


def get_pinyin(text):

    gap = ''
    piny = gap.join(pypinyin.lazy_pinyin(text))
    return piny
