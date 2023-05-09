# Пользователь вводит с клавиатуры строку, слово для
# поиска, слово для замены. Произведите в строке замену
# одного слова на другое. Полученную строку отобразите
# на экране.

line= 'dayBeautifullydayday '
count= line.count ('day')
line1= line.replace('day','night', 3)
print(count)
print(line1)