from sensitive_word import *
import sys
from build_ac import *
import pypinyin


def get_pinyin(wordlist):

    list_pinyin = list()
    gap = ''
    for words in wordlist:
        piny = gap.join(pypinyin.lazy_pinyin(words))
        list_pinyin.append(piny)
    return list(list_pinyin)


def get_initial(word_i):

    gap = ''
    initial = gap.join(i[0][0] for i in pypinyin.lazy_pinyin(word_i))
    return initial



def is_english(check_str):

    i = 0
    for s in check_str:
        if (u'\u0041' <= s <= u'\u005a') or (u'\u0061' <= s <= u'\u007a'):
            i += 1
    if i == len(check_str):
        return True
    else:
        return False


if __name__ == '__main__':

    word_file = sys.argv[1]
    org_file = sys.argv[2]
    ans_file = sys.argv[3]
    with open(word_file, 'r', encoding='utf-8') as f:
        words = f.read().splitlines()
    sensitiveword = dict()
    for word_m in words:
        if is_english(word_m):
            sensitiveword.update({word_m: [word_m]})
            continue
        sensitiveword.update(sensitive_word(word_m))
    tree = BuildAc()
    print(sensitiveword)
    tree.add_word(sensitiveword)
    tree.make_fail()
    answer = dict()
    filet = open(org_file, 'r+', encoding='utf-8')
    with open(org_file, 'r', encoding='utf-8') as f:
        txt1 = f.read().splitlines()
    for i in range(len(txt1)):
        pinyin_list = get_pinyin(txt1[i])
        pinyin_txt = ''
        for ii in pinyin_list:
            pinyin_txt = ''.join(pinyin_list)
        count = int(i) + 1
        answer.update({count: tree.search(pinyin_txt.lower(), pinyin_list, list(txt1[i]))})
    sum = 0
    for i in answer.values():
        for ii in i:
            sum += 1
    filea = open(ans_file, 'w+', encoding='utf-8')
    filea.write('Total: {}'.format(sum)+'\n')
    for key, value in answer.items():
        for i in value:
            print('Line{}: <{}> {}'.format(key, i[0], i[1]))
            filea.write('Line{}: <{}> {}'.format(key, i[0], i[1])+'\n')
    filea.close()

if __name__ == '__main__':

    word_file = sys.argv[1]
    org_file = sys.argv[2]
    ans_file = sys.argv[3]
    with open(word_file, 'r', encoding='utf-8') as f:
        words = f.read().splitlines()
    sensitiveword = dict()
    for word_m in words:
        if is_english(word_m):
            sensitiveword.update({word_m: [word_m]})
            continue
        sensitiveword.update(sensitive_word(word_m))
    tree = BuildAc()
    print(sensitiveword)
    tree.add_word(sensitiveword)
    tree.make_fail()
    answer = dict()
    filet = open(org_file, 'r+', encoding='utf-8')
    with open(org_file, 'r', encoding='utf-8') as f:
        txt1 = f.read().splitlines()
    for i in range(len(txt1)):
        pinyin_list = get_pinyin(txt1[i])
        pinyin_txt = ''
        for ii in pinyin_list:
            pinyin_txt = ''.join(pinyin_list)
        count = int(i) + 1
        answer.update({count: tree.search(pinyin_txt.lower(), pinyin_list, list(txt1[i]))})
    sum = 0
    for i in answer.values():
        for ii in i:
            sum += 1
    filea = open(ans_file, 'w+', encoding='utf-8')
    filea.write('Total: {}'.format(sum)+'\n')
    for key, value in answer.items():
        for i in value:
            print('Line{}: <{}> {}'.format(key, i[0], i[1]))
            filea.write('Line{}: <{}> {}'.format(key, i[0], i[1]))
    filea.close()
