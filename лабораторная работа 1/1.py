number = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
index=number.index(None)
number[index]=0
number[index]=sum(number)/len(number)
print("Измененный список:", number)
