import string


s = 'You are lready under my genjutsu sensei'
s3 = 'you are lready under my genjutsu teacher'
sub_t = "ou"
s1 = '1 3 5 6 2 4 7'
s2 = 'ABC'
my_str = 'Tsukuyomi genjutsu'
tab = '1\t3\n3\t5'
B ='Sharingan'
N = 'SauS'
a = '97'
b = '23'
s4 = '7,8,6,5'
my_strr = '12'
number =  "-290"
strit = "cat"
width = 6
fillchar = '*'
if __name__ == '__main__':
   print(s.find(sub_t, 1, 5))  # Поиск подстроки в строке. Возвращает номер первого вхождения или -1 слева на право
   print(s.rfind(sub_t, 1, 5))  # Поиск подстроки в строке. Возвращает номер последнего вхождения или -1 справо на лево
   print(s.index(sub_t, 1, 5))  # Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
   print(s.index(sub_t, 1, 5))  # Поиск подстроки в строке. Возвращает номер последнего вхождения или |вызывает ValueError
   print(my_str.replace("tsukuyomi genjutsu", "Tsukuyomi Genjutsu Sharingan",)) #Замена шаблона на замену. maxcount ограничивает количество замен old - старая подстрока, которую нужно заменить.
#new - новая подстрока, которая заменит старую подстроку
#count - сколько раз вы хотите заменить старую подстроку новой подстрокой. ( Необязательно )
   print('1,3,5,6,2,4,7'.split(',',maxsplit=7))  # Разбиение строки по разделителю
   print('1231'.isdigit())  # Состоит ли строка из цифр
   print(s2.isalpha())  # Состоит ли строка из букв
   print('asd13'.isalnum()) # Состоит ли строка из цифр или букв
   print(s3.islower())  # Состоит ли строка из символов в нижнем регистре
   print(s2.isupper())  # Состоит ли строка из символов в верхнем регистре
   print("\t".isspace())  # Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'), "новая строка" ('\n'), "перевод каретки" ('\r'), "горизонтальная табуляция" ('\t') и "вертикальная табуляция" ('\v'))
   print("Учитель Вы Уже Под Моим Гендзюцу".istitle())  # Начинаются ли слова в строке с заглавной буквы
   print("Ты уже под моим гендзюцу".upper())  # Преобразование строки к верхнему регистру
   print(" ТЫ УЖЕ В ИЛЛЮЗИИ".lower())
   print(B.startswith('Sharingan'))  # Начинается ли строка S с шаблона str
   print(N.endswith('SauS'))  # Заканчивается ли строка S шаблоном str
   print(s.join(s3)) # Сборка строки из списка с разделителем S
   print(ord('a'))  # Символ в его код ASCII
   print(chr(97))  # Код ASCII в символ
   print(s3.capitalize())  # Переводит первый символ строки в верхний регистр, а все остальные в нижний
   print('1'.center(3, 'w'))  # Возвращает отцентрованную строку, по краям которой стоит символ fill (пробел по умолчанию)
   print(s.count('sub_t', 0, 2))  # Возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию)
   print(tab.expandtabs(5))  # Возвращает копию строки, в которой все символы табуляции заменяются одним или несколькими пробелами, в зависимости от текущего столбца. Если TabSize не указан, размер табуляции полагается равным 8 пробелам
   print(N.lstrip('Su'))  # Удаление пробельных символов в начале строки
   print('Sharingan'.rstrip('nag'))  # Удаление пробельных символов в конце строки
   print('Tsukuyomi'.strip('Tsk\nim\toy')) # Удаление пробельных символов в начале и в конце строки
   print('12'.partition('.'))  # Возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий саму строку, а затем две пустых строки
   print('12'.rpartition('.'))  # Возвращает кортеж, содержащий часть перед последним шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий две пустых строки, а затем саму строку
   print('Учитель ПОДгендзюцу!'.swapcase())  # Переводит символы нижнего регистра в верхний, а верхнего – в нижний
   print('тичер под гензой!'.title())  # Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
   print(number.zfill(8))  # Делает длину строки не меньшей width, по необходимости заполняя первые символы нулями
   print(strit.ljust(width,fillchar))  #Делает длину строки не меньшей width, по необходимости заполняя последние символы символом fillchar
   print(strit.rjust(width,fillchar))  # Делает длину строки не меньшей width, по необходимости заполняя первые символы символом fillchar
   print('hello, {}!'.format('Uchiha Madarada')) # Если для подстановки требуется только один аргумент, то значение - сам аргумент:
   print("{}, {}, {}".format('i','m','n'))  # А если несколько, то значениями будут являться все аргументы со строками подстановки (обычных или именованных):









