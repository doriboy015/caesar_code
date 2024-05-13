def counts(strok): #функция для подсчета символов в строке без учета спец. символов
    countik = 0
    if strok.isalpha(): #если строка только из букв, то передаем длину строки
        countik = len(strok)
    else:
        for j in range(len(strok)):
            if strok[j] in alf_up or strok[j] in alf_down:  #если символ есть в алфавите верхнего или нижнего регистра, то
                countik += 1
    return countik


stroka = input()
mass = stroka.split()   #разбиваем строку на подстроки, разделенные запятыми
mass_count = []         #массив для учета длин подстрок
vivod = ''              #итоговая строка

alf_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'   #алфавит верхнего регистра
alf_down = 'abcdefghijklmnopqrstuvwxyz' #алфавит нижнего регистра

for i in range(len(mass)):
    mass_count.append(counts(mass[i]))  #заполняем массив длин подстрок через функцию с перебором подстрок

for i in range(len(mass)):  #цикл для перебора подстрок
    for k in range(len(mass[i])):   #цикл для перебора символов в подстроках
        if mass[i][k] in alf_up:    #если символ есть в верхнем алфавите, то
            vivod += alf_up[(alf_up.find(mass[i][k]) + mass_count[i]) % 26] #к итоговой строке прибавляем символ, который ищем в алфавите и его индекс плюс длина подстроки по индексу подстроки
        elif mass[i][k] in alf_down:
            vivod += alf_down[(alf_down.find(mass[i][k]) + mass_count[i]) % 26]
        else:
            vivod+= mass[i][k]
    if i != len(mass)-1:    #если последняя итерация цикла, то пробел не добавляем
        vivod += ' '

print(vivod)