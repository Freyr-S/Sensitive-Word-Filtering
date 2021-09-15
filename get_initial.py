import pypinyin


def get_initial(text):

    gap = ''
    initial = gap.join(i[0][0] for i in pypinyin.lazy_pinyin(text))
    return initial
