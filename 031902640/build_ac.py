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
        self.len = 0


class BuildAc(object):
    def __init__(self):
        self.root = Node()
        self.meaningless = [' ', '|', '/', '&', '!', '！', '@', '.', ',', ':', ';', '"', "'", '{', '}', '\\', '-', '#',
                            '$', '￥', '*', '^', '%', '?', '？', '<', '>', '《', '》', '(', ')', '+', '~', '`', '1', '2', 
                            '3', '4', '5', '6', '7', '8', '9', '0', '[', ']', '【', '】', '…', '_', '（', '）', '—', '=',
                            '{', '}', '、', '\'', '‘', '”', '：', '；', '\"', '。']

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
        #q = self.root
        result = list()
        i = 0
        curren = -1
        length = 0
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        #flag5 = False
        templist = list()
        ttemplist = list()
        for j in range(len(txt_list)):
            cnt = -1
            flag3 = False
            #for cnt in range(len(txt_list[j])):
            while(cnt < len(txt_list[j]) - 1):
                cnt += 1
                curren += 1
                word_se = txt[curren]
                if word_se in self.meaningless:
                    if flag4 is True:
                        i = 0
                        flag4 = False
                    if flag1 is False:
                        continue
                    else:
                        i += 1
                        if flag1 is True and i <= 20:
                            templist.append(word_se)
                            continue
                        elif flag1 is True and i > 20:
                            p = self.root
                            flag1 = False
                            length = 0
                            i = 0
                            flag2 = False
                            flag3 = False
                            templist.clear()
                            continue
                while word_se in p.child is False and p != self.root:
                    p = p.fail
                #if(flag2 == True and word_se not in p.child):
                 #   flag2 = False
                 #   i = 0
                 #   length = 0
                 #   continue
                if word_se in p.child:
                    flag4 = True
                    p = p.child[word_se]
                    flag1 = True
                    flag2 = True
                    if flag3 == False and is_english(txt_o[j]) is False:
                        templist.append(txt_o[j])
                        flag3 = True
                    if is_english(txt_o[j]):
                        templist.append(txt_o[j])
                    #if curren < len(txt)-1:
                     #   if (txt[curren+1] not in p.child):
                     #       flag2 = False
                     #       i = 0
                    #        length = 0
                    #if is_english(txt_o[j]):
                     #   length += 1
                    #elif ~(is_english(txt_o[j])):
                     #   if cnt == len(txt_list[j]) - 1:#0:
                     #       length += 1
                else:
                    #if flag5 is True:
                        #result.append([p.word, str_o])
                        #flag5 = False
                    if flag2 == True:
                        flag4 = False
                        flag3 = False
                        flag2 = False
                        flag1 = False
                        templist.clear()
                        cnt -= 1
                        curren -= 1
                        p = self.root
                    p = self.root
                if p.isWord:
                    #if p.child:
                     #   flag5 = True
                     #   str_o = ''
                     #   for z in templist:
                      #      str_o = ''.join(templist)
                       # ttemplist.append(templist)
                      #  continue
                    str_o = ''
                    for z in templist:
                        str_o = ''.join(templist)
                    result.append([p.word, str_o])
                    p = self.root
                    i = 0
                    flag1 = False
                    flag2 = False
                    flag3 = False
                    flag4 = False
                    flag5 = False
                    length = 0
                    templist.clear()

        return result
