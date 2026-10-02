# Программа, считывает содержимое файла,
# добавляет к считанным строкам порядковый
# номер и сохраняет их в таком виде в новом файле

source_file = input('Введите имя файла - источника: ')
result_file = input('С каким именем сохраним файл?: ')

with open(source_file, 'r', encoding='utf-8') as f:
  sourse_text = f.readlines()

str_num = 1
with open(result_file,'a') as f:
  for line in sourse_text:
   f.write(f'{str_num}: {line}')
   str_num +=1
