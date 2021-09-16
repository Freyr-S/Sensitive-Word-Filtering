import pypinyin


def get_initial(txt):

    gap = ''
    initial = gap.join(i[0][0] for i in pypinyin.lazy_pinyin(txt))
    return initial
