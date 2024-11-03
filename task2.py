def find_common_participants(str1, str2, sep = ','):
    list1 = str1.split(sep)
    list2 = str2.split(sep)
    res_list = []

    for first_iter in list1:
        for second_iter in list2:
            if first_iter == second_iter:
                res_list.append(first_iter)

    sorted_list = sorted(res_list)
    return sorted_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))