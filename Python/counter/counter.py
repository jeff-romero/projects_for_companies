# Jeffrey Romero
# GitHub: jeff-romero

from os import error
import tkinter as tk
from tkinter.ttk import Combobox, Separator
import json
from os.path import exists
import genstring
from sys import maxsize
genstring.declare_usable_characters('ALPHA', 'NUM')

# GLOBALS
__current_count = 0
__labels = [] # Will hold recipes
__ADD_COLOR = '#81d41a'
__SUB_COLOR = '#ff0000'
__MAX_VAL = 100 # Maximum value to add/subtract
__SCREEN_WIDTH = 1200
__SCREEN_HEIGHT = 600

screen_size = str(__SCREEN_WIDTH) + "x" + str(__SCREEN_HEIGHT)
root = tk.Tk()
root.title('Counter Tool')
root.geometry(screen_size)

main_buttons_frame = tk.Frame(root, bg='grey')
main_buttons_frame.pack(side=tk.LEFT, fill='both')

recipes_frame = tk.Frame(root, bg='grey')
recipes_frame.pack(side=tk.RIGHT, fill='both', expand=True)


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


def add_new_recipe(output=''):
    global __labels
    new_label_frame = tk.Frame(recipes_frame)
    new_label_frame.pack(fill='x')
    __labels.append(new_label_frame)

    new_label = __labels[len(__labels) - 1]

    recipe = tk.Label(new_label, text="New recipe " + genstring.generate_string(), justify=tk.LEFT)
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


__calculator_queue = []


def add(x=0, y=0):
    return x + y


def sub(x=0, y=0):
    return x - y


def multiply(x=0, y=0):
    return x * y


def divide(x=1, y=1):
    return x / y


calculator_frame = tk.Frame(main_buttons_frame, bg='grey')
calculator_frame.pack()

calc_string = tk.StringVar()
calculator_display = tk.Label(calculator_frame, textvariable=calc_string, bg='black', fg='white', width=86, height=4, anchor=tk.E)
calc_string.set('0')
calculator_display.grid(row=0, column=0, columnspan=4)


def clear_calculator_display(calc_display=None):
    if calc_display:
        global __calculator_queue
        __calculator_queue = []
        calc_string.set('0')


# This will only update the display directly and not evaluate any expressions, assuming the parser function calculator_command() has done its job.
def update_calculator_display(calc_display=None, char=''):
    if calc_display:
        curr_display = calc_string.get()
        if char == 'C':
            clear_calculator_display(calc_display)
            return True
        elif curr_display == '0' and char != '.': # Avoids unnecessary zero padding such as 01, 02, ..., 09999
            curr_display = char
        elif (not curr_display.__contains__('.') and char == '.') or char != '.':
            curr_display += char
        calc_string.set(curr_display)
        return True
    return False


def calculate_expression():
    num = 0
    if not num > maxsize or num < -maxsize:
        pass
    pass


def calculator_command(cmd=''):
    print(cmd)
    if cmd.isnumeric() or cmd == 'C' or cmd == '.' or cmd == '/' or cmd == '*' or cmd == '-' or cmd == '+':
        update_calculator_display(calculator_display, cmd)
        return True
    elif cmd == '+/-' or cmd == '%' or cmd == '=':
        # TODO: this
        return True
    print('command ' + cmd + ' not recognized')
    return False


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

sub_drop_down_menu = Combobox(subtract_frame, values=__number_options)
sub_drop_down_menu.set("Select number")
sub_selected_value = tk.Button(subtract_frame, text='Sub', command=lambda:dec(count_label, int(sub_drop_down_menu.get())), bg=__SUB_COLOR, fg='black')

sub_entry = tk.Entry(subtract_frame, width=10)
sub_entered_value = tk.Button(subtract_frame, text='Sub', command=lambda:dec(count_label, int(sub_entry.get())), bg=__SUB_COLOR, fg='black')

sub_entry.pack(side=tk.LEFT)
sub_entered_value.pack(side=tk.LEFT)

sub_selected_value.pack(side=tk.RIGHT)
sub_drop_down_menu.pack(side=tk.RIGHT)

vertical_window_separator = Separator(root, orient='vertical')
vertical_window_separator.pack(fill='y')


# for i in range(9, -1, -1):
#     num = tk.Button(calculator_frame, text=str(i), command=print(str(i)), bg='black', fg='white')
#     num.grid()

clear = tk.Button(calculator_frame, text='C', command=lambda:calculator_command('C'), bg='black', fg='white', width=20, height=4)
clear.grid(row=1, column=0)
flip_sign = tk.Button(calculator_frame, text='+/-', command=lambda:calculator_command('+/-'), bg='black', fg='white', width=20, height=4)
flip_sign.grid(row=1, column=1)
percent = tk.Button(calculator_frame, text='%', command=lambda:calculator_command('%'), bg='black', fg='white', width=20, height=4)
percent.grid(row=1, column=2)
divide = tk.Button(calculator_frame, text='/', command=lambda:calculator_command('/'), bg='black', fg='white', width=20, height=4)
divide.grid(row=1, column=3)
seven = tk.Button(calculator_frame, text='7', command=lambda:calculator_command('7'), bg='black', fg='white', width=20, height=4)
seven.grid(row=2, column=0)
eight = tk.Button(calculator_frame, text='8', command=lambda:calculator_command('8'), bg='black', fg='white', width=20, height=4)
eight.grid(row=2, column=1)
nine = tk.Button(calculator_frame, text='9', command=lambda:calculator_command('9'), bg='black', fg='white', width=20, height=4)
nine.grid(row=2, column=2)
multiply = tk.Button(calculator_frame, text='*', command=lambda:calculator_command('*'), bg='black', fg='white', width=20, height=4)
multiply.grid(row=2, column=3)
four = tk.Button(calculator_frame, text='4', command=lambda:calculator_command('4'), bg='black', fg='white', width=20, height=4)
four.grid(row=3, column=0)
five = tk.Button(calculator_frame, text='5', command=lambda:calculator_command('5'), bg='black', fg='white', width=20, height=4)
five.grid(row=3, column=1)
six = tk.Button(calculator_frame, text='6', command=lambda:calculator_command('6'), bg='black', fg='white', width=20, height=4)
six.grid(row=3, column=2)
minus = tk.Button(calculator_frame, text='-', command=lambda:calculator_command('-'), bg='black', fg='white', width=20, height=4)
minus.grid(row=3, column=3)
one = tk.Button(calculator_frame, text='1', command=lambda:calculator_command('1'), bg='black', fg='white', width=20, height=4)
one.grid(row=4, column=0)
two = tk.Button(calculator_frame, text='2', command=lambda:calculator_command('2'), bg='black', fg='white', width=20, height=4)
two.grid(row=4, column=1)
three = tk.Button(calculator_frame, text='3', command=lambda:calculator_command('3'), bg='black', fg='white', width=20, height=4)
three.grid(row=4, column=2)
plus = tk.Button(calculator_frame, text='+', command=lambda:calculator_command('+'), bg='black', fg='white', width=20, height=4)
plus.grid(row=4, column=3)
zero = tk.Button(calculator_frame, text='0', command=lambda:calculator_command('0'), bg='black', fg='white', width=42, height=4)
zero.grid(row=5, column=0, columnspan=2)
point = tk.Button(calculator_frame, text='.', command=lambda:calculator_command('.'), bg='black', fg='white', width=20, height=4)
point.grid(row=5, column=2)
equal = tk.Button(calculator_frame, text='=', command=lambda:calculator_command('='), bg='black', fg='white', width=20, height=4)
equal.grid(row=5, column=3)

add_new_recipe_button = tk.Button(recipes_frame, text='Add new recipe', command=add_new_recipe)
add_new_recipe_button.pack(side=tk.TOP)

# root.minsize(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
root.protocol('WM_DELETE_WINDOW', program_exit)
root.resizable(True, True)
root.mainloop()
