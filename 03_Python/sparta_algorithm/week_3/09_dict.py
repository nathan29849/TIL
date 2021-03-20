class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        n = (hash(key)%len(self.items))
        self.items[n] = value
        # return self.items[n]

    def get(self, key):
        n = (hash(key)%len(self.items))
        return self.items[n]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))