def find_common_participants(str_1, str_2, sep=','):
    s1 = str_1.split(sep)
    s2 = str_2.split(sep)
    intersection = set(s2).intersection(s1)
    return sorted(intersection)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants (participants_first_group, participants_second_group, '|')
print("Общие участники:", common_participants)