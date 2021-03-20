class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))
    
    def get(self, key): # key에 따라 값이 달라지기 때문
        for k, v in self.items:
            if key == k:
                return v

class LinkedDcit:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        self.items[index].get(key)

