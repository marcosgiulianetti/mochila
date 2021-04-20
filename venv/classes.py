class Pilha:
    def __init__(self):
        self.items = []

    def IsEmpty(self):
        return self.items == []

    def Push(self, item):
        self.items.insert(0,item)

    def Pop(self):
        return self.items.pop(0)

    def Peek(self):
        return self.items[0]

    def Size(self):
        return len(self.items)