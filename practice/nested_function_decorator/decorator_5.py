# Реалізуйте функцію, яка перетворює рядок на ініціали (перші літери кожного слова). Використайте вкладену функцію для розбиття рядка на окремі слова та отримання першої літери кожного слова.
# Maxim 
# def split_str(your_string):
#     for item in your_string.split(" "):
#         print(f"The first letter of the word '{item}', is '{item[0]}'.")


# split_str("hello my name is max")



#my
def initialization(func):
    def get_initial(word):
        new_word = word[0].upper()
        return new_word
    
    words = func.split()
    initials = []
    for word in words:
        initials.append(get_initial(word))
    initials_string = "".join(initials)
    return initials_string  

words_1 = "my name is kira"
result = initialization(words_1)
print(result)  





