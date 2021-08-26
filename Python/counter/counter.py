# Jeffrey Romero
# GitHub: jeff-romero

from os import error
import tkinter as tk
from tkinter.ttk import Combobox, Separator
import json
from os.path import exists
import genstring
genstring.declare_usable_characters('ALPHA', 'NUM')

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 240
screen_size = str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT)
root = tk.Tk()
root.title('Counter Tool')
root.geometry(screen_size)


main_buttons_frame = tk.Frame(root, bg='grey')
main_buttons_frame.pack(side=tk.LEFT, fill='both', expand=True)

recipes_frame = tk.Frame(root, bg='grey')
recipes_frame.pack(side=tk.RIGHT, fill='both', expand=True)

# GLOBALS
__current_count = 0
__labels = [] # Will hold recipes
__ADD_COLOR = '#81d41a'
__SUB_COLOR = '#ff0000'
__MAX_VAL = 100 # Maximum value to add/subtract


def inc(label=None, num_to_inc=1):
    if num_to_inc <= __MAX_VAL:
        global __current_count
        __current_count += num_to_inc
        display = str(__current_count)
        label.config(text=display)
    else:
        print('Chosen value too large! (Required: value <= ' + str(__MAX_VAL) + ')')


def dec(label=None, num_to_dec=1):
    if num_to_dec <= __MAX_VAL:
        global __current_count
        __current_count -= num_to_dec
        display = str(__current_count)
        label.config(text=display)
    else:
        print('Chosen value too large! (Required: value <= ' + str(__MAX_VAL) + ')')


def reset(label=None):
    global __current_count
    __current_count = 0
    display = str(__current_count)
    label.config(text=display)


def create_data_file(data_file=None):
    file_contents = '{\"current_count\" : ' + str(__current_count) + '}'
    f = open(data_file, 'w+')
    f.write(file_contents)
    f.close()


def load_data_file(data_file=None):
    global __current_count, data
    f = open(data_file, 'r')
    data = json.load(f)
    __current_count = data['current_count']
    f.close()


def program_exit():
    global data
    data['current_count'] = __current_count

    f = open(data_file, 'w+')
    f.write(json.dumps(data))
    del data
    f.close()
    exit(0)


def del_button(label_to_del=None):
    if label_to_del:
        global __labels
        label_to_del.destroy()
        __labels.remove(label_to_del)


def add_new_recipe():
    global __labels
    new_label_frame = tk.Frame(recipes_frame)
    new_label_frame.pack(fill='x')
    __labels.append(new_label_frame)

    new_label = __labels[len(__labels) - 1]

    recipe = tk.Label(new_label, text="New recipe " + genstring.generate_string())
    recipe.pack(side=tk.LEFT, fill='y', expand=True)

    delete_recipe = tk.Button(new_label, text='X', bg='red', fg='black', command=lambda:del_button(new_label))
    delete_recipe.pack(side=tk.RIGHT, fill='y')


data_file = './userdata.json'
data = None
if not exists(data_file):
    print('User data file doesn\'t exist. Creating one...')
    create_data_file(data_file)
load_data_file(data_file)


count_label = tk.Label(main_buttons_frame, text=__current_count, height=3, bg='black', fg='white', justify=tk.CENTER, font=75)
count_label.pack(fill='x', expand=True, pady=(0,5))

#
# ADD
#
add_frame = tk.Frame(main_buttons_frame)
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
add_selected_value = tk.Button(add_frame, text='Add', command=lambda:inc(count_label, int(add_drop_down_menu.get())), bg=__ADD_COLOR, fg='black')

add_entry = tk.Entry(add_frame, width=10)
add_entered_value = tk.Button(add_frame, text='Add', command=lambda:inc(count_label, int(add_entry.get())), bg=__ADD_COLOR, fg='black')

add_entry.pack(side=tk.LEFT)
add_entered_value.pack(side=tk.LEFT)

add_selected_value.pack(side=tk.RIGHT)
add_drop_down_menu.pack(side=tk.RIGHT)


#
# SUBTRACT
#
subtract_frame = tk.Frame(main_buttons_frame)
subtract_frame.pack(fill='x', expand=True, pady=(5, 0))

sub_drop_down_menu = Combobox(add_frame, values=__number_options)
sub_drop_down_menu.set("Select number")
sub_selected_value = tk.Button(add_frame, text='Sub', command=lambda:dec(count_label, int(sub_drop_down_menu.get())), bg=__SUB_COLOR, fg='black')

sub_entry = tk.Entry(add_frame, width=10)
sub_entered_value = tk.Button(add_frame, text='Sub', command=lambda:dec(count_label, int(sub_entry.get())), bg=__SUB_COLOR, fg='black')

sub_entry.pack(side=tk.LEFT)
sub_entered_value.pack(side=tk.LEFT)

sub_selected_value.pack(side=tk.RIGHT)
sub_drop_down_menu.pack(side=tk.RIGHT)

add_new_recipe_button = tk.Button(recipes_frame, text='Add new recipe', command=add_new_recipe)
add_new_recipe_button.pack(side=tk.TOP)

# root.minsize(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
root.protocol('WM_DELETE_WINDOW', program_exit)
root.resizable(True, True)
root.mainloop()
