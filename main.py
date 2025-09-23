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
            for idx, char in enumerate(selected_name):
                if char == gussed_char:
                    guessed_list[idx]=gussed_char
            current_guess=' '.join(guessed_list)
            print(f'perfect=>{current_guess}')
            if not'_' in guessed_list:
                print('you won!')
                break