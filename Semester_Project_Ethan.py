
class mergeables:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def check(self):
        print(f"check {self.name}")
        print(self.data)

