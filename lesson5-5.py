'''
    Создать (программно) текстовый файл, записать в него программно
    набор чисел, разделенных пробелами. Программа должна
    подсчитывать сумму чисел в файле и выводить ее на экран.
'''
with open('file5.txt', 'r') as number:
         number = input()
         summa = sum(map(int, number.split()))
         print(summa)




