# Ввод строки
str_text = input("Введите предложение: ")
count = 0
new_string = ""
for char in str_text:
    if char == "а":
        str_text.count('а') #Считаем количество символов
    else:
        new_string += char
print("Полученная строка:", new_string.translate({ord(i): None for i in 'а'})) #Удаляем из строки символ "a" и выводим результат
print(f"Количество заменённых символов:{str_text.count('а')}") #Считаем количество удалённых символов
