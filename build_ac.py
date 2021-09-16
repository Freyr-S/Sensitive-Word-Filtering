import ahocorasick


class Node(object):
    def __init__(self):
        self.fail = None
        self.child = dict()
        self.isWord = False
        self.word = ''


class BuildAc(object):
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        temp_root = self.root
        for w in word:
            if w not in temp_root.next:
                temp_root.child[w] = Node()
            temp_root = temp_root.child[w]
        temp_root.isWord = True
        temp_root.word = word

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
                    while p is not None:
                        if key in p.child:
                            temp.child[key].fail = p.child
                            break
                        p = p.fail
                    if p is None:
                        temp.child[key].fail = self.root
                temp_que.append(temp.child[key])

    def search(self,txt):
        p = self.root
        result = list()
        curren = 0
        while curren < len(txt):
            word = txt[curren]
            while word in p.child==False and p != self.root
                p = p.fail
            if word in p.child:
                p = p.child[word]
            else:
                p = self.root
            if p.isWord:
                result.append(p.word)
                p = self.root
            curren += 1
        return result







"""
def build_ac(wordlist):

    tree = ahocorasick.Automaton()
    for index, word in enumerate(wordlist):
        tree.add_word(word, (index, word))
    tree.make_automaton()
    return tree
"""
