import random
names=['Ali','Amir','sadia','Ahmad']

selected_name= random.choice(names)
guess_count = len(selected_name)
guessed_list = ['-']*len(selected_name)
while guess_count>0:
    gussed_char = input('Enter a char:\n')
    if gussed_char.isalpha():
        if gussed_char in guessed_list:
            print('you have guessed before,try new chracter')
        else: