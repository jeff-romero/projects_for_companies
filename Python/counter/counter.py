# Jeffrey Romero
# GitHub: jeff-romero

from os import error
# import tkinter as tk
from tkinter.ttk import Combobox, Separator
import json
from os.path import exists
import genstring
from sys import maxsize
genstring.declare_usable_characters('ALPHA', 'NUM')

import settings
import modules
import tkcalculator

__labels = [] # Will hold recipes
__current_count = 0


screen_size = str(settings.SCREEN_WIDTH) + "x" + str(settings.SCREEN_HEIGHT)
root = modules.tk.Tk()
root.title('Counter Tool')
root.geometry(screen_size)

main_buttons_frame = modules.tk.Frame(root, bg='grey')
main_buttons_frame.pack(side=modules.tk.LEFT, fill='both')

recipes_frame = modules.tk.Frame(root, bg='grey')
recipes_frame.pack(side=modules.tk.RIGHT, fill='both', expand=True)

# TODO: Put functions in their own modules, then import those modules

# COUNTER
def inc(label, num):
    if label and num <= settings.max_num:
        global __current_count
        __current_count += num
        label.config(text=str(__current_count))
    else:
        print('inc(): Chosen value too large! (Required: value <= ' + str(settings.max_num) + ')')

# COUNTER
def dec(label, num):
    if label and num <= settings.max_num:
        global __current_count
        __current_count -= num
        label.config(text=str(__current_count))
    else:
        print('dec(): Chosen value too large! (Required: value <= ' + str(settings.max_num) + ')')

# COUNTER
def reset_counter_label(label=None):
    if label:
        global __current_count
        __current_count = 0
        label.config(text=str(__current_count))
    else:
        print('reset(): Invalid label provided to function.')

# COUNTER
def create_data_file(data_file=None):
    file_contents = '{\"current_count\" : ' + str(__current_count) + '}'
    f = open(data_file, 'w+')
    f.write(file_contents)
    f.close()

# COUNTER
def load_data_file(data_file=None):
    global __current_count, data
    f = open(data_file, 'r')
    data = json.load(f)
    __current_count = data['current_count']
    f.close()

# MAIN
# Save user data by writing it to a file then exit program.
def program_exit():
    global __current_count, data
    data['current_count'] = __current_count
    f = open(data_file, 'w+')
    f.write(json.dumps(data))
    del data
    f.close()
    exit(0)

# COUNTER
def del_button(label_to_del=None):
    if label_to_del:
        global __labels
        label_to_del.destroy()
        __labels.remove(label_to_del)

# COUNTER
def add_new_recipe(output=''):
    global __labels
    new_label_frame = modules.tk.Frame(recipes_frame)
    new_label_frame.pack(fill='x')
    __labels.append(new_label_frame)

    new_label = __labels[len(__labels) - 1]

    recipe = modules.tk.Label(new_label, text="New recipe " + genstring.generate_string(), justify=modules.tk.LEFT)
    recipe.pack(side=modules.tk.LEFT, fill='y', expand=True)

    delete_recipe = modules.tk.Button(new_label, text='X', bg='red', fg='black', command=lambda:del_button(new_label))
    delete_recipe.pack(side=modules.tk.RIGHT, fill='y')


data_file = './userdata.json'
data = None
if not exists(data_file):
    print('User data file doesn\'t exist. Creating one...')
    create_data_file(data_file)
load_data_file(data_file)


count_label = modules.tk.Label(main_buttons_frame, text=__current_count, height=3, bg='black', fg='white', justify=modules.tk.CENTER, font=75)
count_label.pack(fill='x', expand=True)
reset_count_label = modules.tk.Button(main_buttons_frame, text='RESET COUNTER', bg='red', fg='black', command=lambda:reset_counter_label(count_label))
reset_count_label.pack(pady=(0,5))

#
# COUNTER - ADD
#
add_frame = modules.tk.Frame(main_buttons_frame)
add_frame.pack(fill='x', expand=True, pady=(0, 5))

__number_options = [
    1,
    2,
    5,
    10,
    15,
    20
]

add_drop_down_menu = Combobox(add_frame, values=__number_options)
add_drop_down_menu.set("Select number")
add_selected_value = modules.tk.Button(add_frame, text='Add', command=lambda:inc(count_label, int(add_drop_down_menu.get())), bg=settings.add_color, fg='black')

add_entry = modules.tk.Entry(add_frame, width=10)
add_entered_value = modules.tk.Button(add_frame, text='Add', command=lambda:inc(count_label, int(add_entry.get())), bg=settings.add_color, fg='black')

add_entry.pack(side=modules.tk.LEFT)
add_entered_value.pack(side=modules.tk.LEFT)

add_selected_value.pack(side=modules.tk.RIGHT)
add_drop_down_menu.pack(side=modules.tk.RIGHT)


#
# COUNTER - SUBTRACT
#
subtract_frame = modules.tk.Frame(main_buttons_frame)
subtract_frame.pack(fill='x', expand=True, pady=(5, 0))

sub_drop_down_menu = Combobox(subtract_frame, values=__number_options)
sub_drop_down_menu.set("Select number")
sub_selected_value = modules.tk.Button(subtract_frame, text='Sub', command=lambda:dec(count_label, int(sub_drop_down_menu.get())), bg=settings.sub_color, fg='black')

sub_entry = modules.tk.Entry(subtract_frame, width=10)
sub_entered_value = modules.tk.Button(subtract_frame, text='Sub', command=lambda:dec(count_label, int(sub_entry.get())), bg=settings.sub_color, fg='black')

sub_entry.pack(side=modules.tk.LEFT)
sub_entered_value.pack(side=modules.tk.LEFT)

sub_selected_value.pack(side=modules.tk.RIGHT)
sub_drop_down_menu.pack(side=modules.tk.RIGHT)

vertical_window_separator = Separator(root, orient='vertical')
vertical_window_separator.pack(fill='y')

# CALC HERE ?
calc_frame = modules.tk.Frame(main_buttons_frame, bg='grey')
calc_frame.pack()

calculator = tkcalculator.Tkcalculator(calc_frame)

add_new_recipe_button = modules.tk.Button(recipes_frame, text='Add new recipe', command=add_new_recipe)
add_new_recipe_button.pack(side=modules.tk.TOP)

# root.minsize(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
root.protocol('WM_DELETE_WINDOW', program_exit)
root.resizable(True, True)
root.mainloop()
