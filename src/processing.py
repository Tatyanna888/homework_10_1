def filter_by_state(list_info: list, state: str = "EXECUTED") -> list:
    """Функция фильтрации операций по ключу state"""
    filtered_list = []
    for info_dict in list_info:
        if info_dict["state"] == state:
            filtered_list.append(info_dict)
    return filtered_list

print(filter_by_state([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]))

# def sort_by_date(list_dict: list, date=True: bool) -> list:
#     """Функция сортировки операций по дате"""
# sorted_list = sorted(list_dict, key=lambda d: d("data"), reverse=reverse_list)
#
#     return

