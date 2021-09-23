import pypinyin


def get_pinyin(wordlist):

    list_pinyin = list()
    gap = ''
    for words in wordlist:
        piny = gap.join(pypinyin.lazy_pinyin(words))
        list_pinyin.append(piny)
    return list(list_pinyin)
