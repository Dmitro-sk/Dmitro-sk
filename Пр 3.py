lst = [1,2,3,4,5,6,3,4,5,7,6,5,4,3,4,5,4,3,11, 'Привіт', 'Анаконда']#список який містить числа і рядки


def def_lst_unique(lst):
    lst_unique = [] #створює список для збереження унікальних значень.
    lst_append = [] #використовується для перетворення всіх рядків у нижній регістр.
    for a in lst:
        if type(a) == str:
            a_lower = a.lower()
            lst_append.append(a_lower)
        else:
            lst_append.append(a) # цикл що проходить по всіх елементах вхідного списку lst
    lst_in_set = set()
    for item in lst_append :
     if item  not in lst_in_set:
         lst_unique.append(item)
         lst_in_set.add(item) #створює множину і додає унікальні значення 

    return lst_unique and lst_in_set#повертає значення множини


def def_lst_sort(lst):

    lst_str = [] #список для рядків
    lst_int = [] #список для чисел

    lst_sort = r.copy()
    for k in lst_sort:
        if type(k) == int:
            lst_int.append(k)
        elif type(k) == str:
            lst_str.append(k)#копіює список та розприділяє елементи по типам

    lst_str.sort()
    lst_int.sort()

    return lst_int + lst_str#сортує рядки , числа і об'єднює


r =  def_lst_unique(lst) #містить результат
sorted_list = def_lst_sort(r) # відсортований результат


print(sorted_list)
