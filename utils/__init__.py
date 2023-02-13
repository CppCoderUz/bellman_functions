from utils.functions import get_min_or_max_value
from utils.itr_list import IterableList
from utils.task import Task

class Solution:
    def __init__(self, n: int, b:int, index_list: list, task_list: list, shart:bool):
        self._n = n
        self._index_list = index_list
        self._task_list = []
        for _ in task_list:
            self._task_list.append(Task(_))
        self._iterable_list = IterableList(max_number=b, size=n)
        self.shart = shart
    
    def _solve(self):
        return get_min_or_max_value(
            indexs=self._index_list,
            iter_list=self._iterable_list,
            task_list=self._task_list,
            shart=self.shart
        )

    def max_value(self):
        var = self._solve()
        if var['rezault'] == True:
            return var['max']['value']
        else:
            return None    

    def get_max_value_for_indexs(self):
        var = self._solve()
        if var['rezault'] == True:
            return var['max']['list']
        else:
            return None

    def min_value(self):
        var = self._solve()
        if var['rezault'] == True:
            return var['min']['value']
        else:
            return None 
    
    def get_min_value_for_indexs(self):
        var = self._solve()
        if var['rezault'] == True:
            return var['min']['list']
        else:
            return None    
    
    def get_message(self):
        return ('Xatolik mavjud emas' if 
                self._solve()['message'] == '' else self._solve()['message'])
    
    def get_rezault(self):
        return self._solve()['rezault']