

''' Listning maxsus ko'rinishli holati '''
class IterableList:
    def __init__(self, max_number: int, size: int):
        self.max_number = max_number
        self.size = size
        adding__list = []
        for _ in range(size):
            adding__list.append(0)
        self.list_numbers = adding__list

    def add(self, number = 1):
        if self.list_sum() == self.max_number*self.size:
            return
            
        if self.list_numbers[self.size - number] == self.max_number:
            self.list_numbers[self.size - number] = 0
            self.add(number=number + 1)
        else:
            self.list_numbers[self.size - number] += 1

    def list_sum(self):
        return sum(self.list_numbers)
    
    def get_max_iteration(self):
        return (self.max_number+1)**(self.size) 