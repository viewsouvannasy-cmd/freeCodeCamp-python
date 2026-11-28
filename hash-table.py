class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, value: str) -> int:
        hash_value = 0

        for i in range(len(value)):
            hash_value += ord(value[i])

        return hash_value

    def add(self, key: str, value: str):
        hash_key = self.hash(key)
        if hash_key not in self.collection:
            self.collection[hash_key] = {key: value}
            return

        self.collection[hash_key][key] = value

    def remove(self, key: str):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]

    def lookup(self, key: str):
        try:
            return self.collection[self.hash(key)][key]
        except KeyError:
            return None


ht = HashTable()

ht.add("dear", "friend")
ht.add("read", "book")
print(ht.collection)
print(ht.lookup("golf"))
