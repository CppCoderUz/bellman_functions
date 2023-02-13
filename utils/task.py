from math import * 


class Task:
    def __init__(self, task: str):
        self.task = task
        self.cleaned_task = str()
        self._cleande_data()
    
    def _is_int(self, text: str):
        numbers = '1234567890'
        return (text in numbers)
    
    def _is_right(self, test_number = 1):
        new_task = self.cleaned_task
        new_task = new_task.replace('x', str(test_number))
        try:
            return eval(new_task)
        except:
            return None
        
    def is_right(self):
        return self._is_right(test_number=1)

    def _cleande_data(self):
        new_str = self.task
        new_str = new_str.replace('^', '**')
        new_str = new_str.replace('x', '(x)')
        new_str = new_str.replace(' ', '')
        new_str += ' '
        new_task = ''
        for i in range(len(new_str)):

            if self._is_int(new_str[i]) and new_str[i+1] == '(':
                new_task += new_str[i] + '*'

            elif self._is_int(new_str[i]) and new_str[i+1] == '(':
                new_task += new_str[i] + '*'

            elif (new_str[i] == ')') and (new_str[i+1] == '('):
                new_task += new_str[i] + '*'
            
            else:
                new_task += new_str[i]
        self.cleaned_task = new_task
    
    def get_value(self, x: int):
        return self._is_right(test_number=x)
        