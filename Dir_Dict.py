import os

class DirDict():
    def __init__(self, path):
        if os.path.exists(path):
            self.path = path
        else:
            raise NameError("Неверный путь!")

    def __getitem__(self, item):
        if item in os.listdir(self.path):
            path = self.path + "/" + item
            with open(item, 'r') as f:
                return f.read()
        raise IndexError('Неверный ключ', item)

    def __setitem__(self, key, value):
        path = self.path + '/' + key
        if not os.path.exists(path):
            os.makedirs(path)
        with open(key, 'w') as f:
            f.write(value)

    def __len__(self):
        return len(os.listdir(self.path))

d = DirDict('/tmp')
d['lang'] = 'Pytho'