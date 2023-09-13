# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да   
#     **Вывод:** Парам пам-пам 

def input_phrase()-> str: return input("Что пропел Винни-Пух?: ")

def smash_phrase(phrase: str)-> list: return phrase.split(" ")

def is_it_have_rhythm(phrase_list: list, vowels_list: list)->str:
    list_1 = [0 for x in range(len(phrase_list))]
    for i in range(len(phrase_list)):
        for x in phrase_list[i]:
            if x in vowels_list:
                list_1[i] = list_1[i] + 1
                
    print(list_1)
    for i in range(len(list_1)-1):
        if list_1[i] != list_1[i+1]:
            check = False
            break
        else:
            check = True
    if check:
        return 'Парам пам-пам'
    else: return 'Пам парам'

vowels_list = ['у','е','ы','а','о','э','я','и','ю']  
# print(is_it_have_rhythm(smash_phrase('пара-ра-рам рам-пам-папам па-ра-па-да'),vowels_list))
print(is_it_have_rhythm(smash_phrase(input_phrase()),vowels_list))





