'''
深浅拷贝的探究
'''


class Bus:
    '模拟公交上下车'

    def __init__(self, passengers=None):
        if not passengers:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


import copy
bus1 = Bus(['Alice', 'Bill', 'Clarire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))
bus1.drop('Bill')
print(bus1.passengers, bus2.passengers, bus3.passengers)
print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))
