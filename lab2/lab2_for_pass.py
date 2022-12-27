import json
from random import randint, choice
from pprint import pprint
  
def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)
def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

class Cocktails:
    def __init__(self):
        self.ml = randint(150, 400)
        self.type = choice(['Mojito', 'Margaret', 'Daiquiri', 'Cosmopolitan', 'Bloody Mary', 'Mulled wine', 'Martini', 'Mimosa', 'Aviation', 'Ruff', 'Stinger', 'Bumbo'])
        self.amount = randint(1, 31)

data = {
    'Cocktails': []
}

for i in range(50):
    data['Cocktails'].append(Cocktails().__dict__)

n_data = read('data_lab2.json')
print(n_data['Cocktails'][49])
g = Cocktails()

g.name = n_data['Cocktails'][4]['type']

print(g.name)

input()