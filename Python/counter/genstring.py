# Jeffrey Romero
# GitHub: jeff-romero

from random import randint

LEN_DEFAULT = 10
ALPHA = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
NUM = '1234567890'
SPECIAL = '!@#$%^&*()'
__usable_chars = ALPHA + NUM + SPECIAL

def declare_usable_characters(*char_sets):
    global __usable_chars
    __usable_chars = ''
    for char_set in char_sets:
        if char_set == 'ALPHA':
            __usable_chars += ALPHA
        elif char_set == 'NUM':
            __usable_chars += NUM
        elif char_set == 'SPECIAL':
            __usable_chars += SPECIAL

def generate_string(length=LEN_DEFAULT):
    generated_string = ''
    for i in range(length):
        generated_string += __usable_chars[randint(0, len(__usable_chars) - 1)]
    return generated_string

# class Genstr():
#     def __init__(self, length=7, ):
#         self.length = length
#         self.usable_chars = ''
    
    # def declare_usable_characters(self, *char_sets):
    #     global ALPHA, NUM, SPECIAL
    #     for char_set in char_sets:
    #         if char_set == 'ALPHA':
    #             self.usable_chars += ALPHA
    #         elif char_set == 'NUM':
    #             self.usable_chars += NUM
    #         elif char_set == 'SPECIAL':
    #             self.usable_chars += SPECIAL




