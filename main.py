from build_ac import *
from sensitive_word import *
from Simple_traditional import *
from query import *
from get_Pinyin import *
import json


if __name__ == '__main__':
    fileo = open('C:/Users/86189/AppData/Local/Programs/Python/words (1).txt')
    words = []
    while 1:
        line = fileo.readline()
        if not line:
            break
        words.append(line)
    fileo.close()
    meaningless = [' ', '|', '/', '&', '!', '！', '@', '.', ',', ':', ';', '"', "'", '{', '}', '\\', '-', '#', '$',
                   '￥', '*', '^', '%', '?', '？', '<', '>', '《', '》', '(', ')', '+', '~', '`']
    sensitiveword = sensitive_word(words)
    tree = build_ac(sensitiveword)
    fileo = open('C:/Users/86189/AppData/Local/Programs/Python/org (1).txt')
    text = fileo.read()
    simple_text = sim2tradition(text)
    pinyin_text = get_pinyin(text)
    answer1 = query(simple_text)
    answer3 = dict()
    answer = dict()
    for i in sorted(answer1):
        answer3[i] = answer1[i]
    answer2 = query(pinyin_text)
    for i in sorted(answer2):
        answer3[i] = answer2[i]
    for i in sorted(answer3):
        answer[i] = answer3[i]
        with open('C:/Users/86189/AppData/Local/Programs/Python/ans.txt', 'w') as f:
            txt_str = json.dumps(answer, indent=0)
            f.write(txt_str)
            f.write('\n')
        f.close()

