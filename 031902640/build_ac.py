def is_english(check_str):

    ii = 0
    for s in check_str:
        if (u'\u0041' <= s <= u'\u005a') or (u'\u0061' <= s <= u'\u007a'):
            ii += 1
    if ii == len(check_str):
        return True
    else:
        return False


class Node(object):
    def __init__(self):
        self.fail = None
        self.child = dict()
        self.isWord = False
        self.word = ''


class BuildAc(object):
    def __init__(self):
        self.root = Node()
        self.meaningless = [' ', '|', '/', '&', '!', '！', '@', '.', ',', ':', ';', '"', "'", '{', '}', '\\', '-', '#',
                            '$', '￥', '*', '^', '%', '?', '？', '<', '>', '《', '》', '(', ')', '+', '~', '`', '1', '2', 
                            '3', '4', '5', '6', '7', '8', '9', '0', '[', ']', '【', '】', '…', '_', '（', '）', '—', '=',
                            '{', '}', '、', '\'', '‘', '”', '：', '；']

    def add_word(self, word):
        temp_root = self.root
        for key, value in word.items():
            for w in value:
                for char in w:
                    if char not in temp_root.child.keys():
                        temp_root.child[char] = Node()
                    temp_root = temp_root.child[char]
                temp_root.isWord = True
                temp_root.word = key
                temp_root = self.root

    def make_fail(self):
        temp_que = list()
        temp_que.append(self.root)
        while len(temp_que) != 0:
            temp = temp_que.pop(0)
            p = None
            for key, value in temp.child.items():
                if temp == self.root:
                    temp.child[key].fail = self.root
                else:
                    p = temp.fail
                    while p is not None:
                        if key in p.child:
                            temp.child[key].fail = p.child[key]
                            break
                        elif key not in p.child and p == self.root:
                            temp.child[key].fail = p
                            break
                        p = p.fail
                    if p is None:
                        temp.child[key].fail = self.root
                temp_que.append(temp.child[key])

    def search(self, txt, txt_list, txt_o):

        p = self.root
        result = list()
        i = 0
        curren = -1
        length = 0
        flag1 = False
        start = 0
        end = 0
        for j in range(len(txt_list)):
            for cnt in range(len(txt_list[j])):
                curren += 1
                word_se = txt[curren]
                if word_se in self.meaningless:
                    if flag1 is False:
                        continue
                    else:
                        i += 1
                        if flag1 is True and i <= 20:
                            continue
                        elif flag1 is True and i > 20:
                            p = self.root
                            flag1 = False
                            i = 0
                            continue
                while word_se in p.child is False and p != self.root:
                    p = p.fail
                if word_se in p.child:
                    p = p.child[word_se]
                    flag1 = True
                    if is_english(txt_o[j]):
                        length += 1
                    elif ~(is_english(txt_o[j])):
                        if cnt == len(txt_list[j]) - 1:
                            length += 1
                else:
                    p = self.root
                if p.isWord:
                    if ~(is_english(txt_o[j])) and ~(cnt == len(txt_list[j]) - 1):
                        length += 1
                    if is_english(txt_o[j]):
                        length -= 1
                    end = j + 1
                    start = end - i - length
                    str_o = ''
                    for z in txt_o[start: end]:
                        str_o = ''.join(txt_o[start: end])
                    result.append([p.word, str_o])
                    p = self.root
                    i = 0
                    flag1 = False
                    length = 0

        return result
