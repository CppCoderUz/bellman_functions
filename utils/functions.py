from utils import itr_list


def is_need_indexs(indexs: list, iter_list: itr_list.IterableList, shart:bool):
    s = 0
    for i in range(iter_list.size):
        s += iter_list.list_numbers[i]*indexs[i]
    if shart:
        return (s <= iter_list.max_number)
    return (s == iter_list.max_number)
    

def get_min_or_max_value(iter_list: itr_list.IterableList, task_list: list, indexs: list, shart:bool):
    # ==================================
    ''' 'task_list'ni xatoliklar bor yoki yo'qligiga tekshirish '''
    try:
        for i in task_list:
            if not i.is_right():
                raise Exception
    except Exception:
        return {'rezault': False, 'message': 'Task listda xatolik'}

    # ===================================
    ''' 'indexs'ni begona tipli o'zgaruvchilar bor yoki \
        yo'qligiga tekshirish '''
    try:
        for i in indexs:
            i += 1
    except:
        return {'rezault': False, 'message': 'Indexlar ro\'yxatida \n int bo\'lmagan ma\'lumot bor'}

    # ===================================
    ''' Sikllar sonini cheklash uchun qism dastur '''
    if iter_list.get_max_iteration() > 10_000_000:
        return {'rezault': False, 'message': 'Sikllar soni haddan \n tashqari ko\'p, size = %s' %iter_list.get_max_iteration()}

    len_task_list = len(task_list)
    if not (len_task_list == len(indexs)):
        return {'rezault': False, 'message': 'Funksiyalar va \n indexlar soni teng emas!'}

    if not (len_task_list == iter_list.size):
        return {'rezault': False, 'message': 'Funksiyalar soni kam'}

    _min = +1000000000000000000000000
    _max = -1000000000000000000000000
    min_index_list = ''
    max_index_list = ''


    for _ in range(iter_list.get_max_iteration()):
        if is_need_indexs(indexs=indexs, iter_list=iter_list, shart=shart):
            sum = 0
            for j in range(iter_list.size):
                key = task_list[j].get_value(x=iter_list.list_numbers[j])
                if key == None:
                    return {'rezault': False, 'message': 'Misolni kiritishda xatolik'}
                else:
                    sum += key
            if sum > _max:
                _max = sum
                max_index_list = ' '.join(map(str, iter_list.list_numbers))
                
            if sum < _min:
                _min = sum
                min_index_list = ' '.join(map(str, iter_list.list_numbers))

        iter_list.add()
    
    if _min == 1000000000000000000000000 or _max == -1000000000000000000000000:
        return {
            'rezault': False,
            'message': 'Ushbu shartni qanoatlantiradigan \nbutun musbat sonlar mavjud emas'
        }

    return {
        'min': {
            'value': _min,
            'list': list(map(int, min_index_list.split())),
        },
        'max': {
            'value': _max,
            'list': list(map(int, max_index_list.split())),
        },
        'rezault': True,
        'message': ''
    }
        
    