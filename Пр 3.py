lst = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3,11, 'Привіт', 'Анаконда']


def def_lst_unique(lst):
    lst_unique = []
    lst_append = []
    for a in lst:
        if type(a) == str:
            a_lower = a.lower()
            lst_append.append(a_lower)
        else:
            lst_append.append(a)
    lst_in_set = set()
    for item in lst_append :
     if item  not in lst_in_set:
         lst_unique.append(item)
         lst_in_set.add(item)

    return lst_unique and lst_in_set


def def_lst_sort(lst):

    lst_str = []
    lst_int = []

    lst_sort = r.copy()
    for k in lst_sort:
        if type(k) == int:
            lst_int.append(k)
        elif type(k) == str:
            lst_str.append(k)

    lst_str.sort()
    lst_int.sort()

    return lst_int + lst_str


r =  def_lst_unique(lst)
sorted_list = def_lst_sort(r)


print(sorted_list)