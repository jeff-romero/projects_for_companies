# Jeffrey Romero
# GitHub: jeff-romero

import tkinter as tk
from tkinter import ttk
import json
from os.path import exists
import genstring
genstring.declare_usable_characters('ALPHA', 'NUM')

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 240
screen_size = str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT)
# canvas = tk.Canvas(root, height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
root = tk.Tk()
root.title('Counter Tool')
root.geometry(screen_size)


main_buttons_canvas = tk.Canvas(root, bd=0, bg='green', height=SCREEN_HEIGHT, width=360)
main_buttons_canvas.pack(side=tk.LEFT, fill='both', expand=True)
recipe_canvas = tk.Canvas(root, bd=0, bg='red', height=SCREEN_HEIGHT, width=360)
recipe_canvas.pack(side=tk.RIGHT, fill='both', expand=True)


# GLOBALS
current_count = 0
labels = [] # Will hold recipes


def inc(label=None, num_to_inc=1):
    global current_count
    current_count += num_to_inc
    display = str(current_count)
    label.config(text=display)


def dec(label=None, num_to_dec=1):
    global current_count
    current_count -= num_to_dec
    display = str(current_count)
    label.config(text=display)


def reset(label=None):
    global current_count
    current_count = 0
    display = str(current_count)
    label.config(text=display)


def create_data_file(data_file=None):
    file_contents = '{\"current_count\" : ' + str(current_count) + '}'
    f = open(data_file, 'w+')
    f.write(file_contents)
    f.close()


def load_data_file(data_file=None):
    global current_count, data
    f = open(data_file, 'r')
    data = json.load(f)
    current_count = data['current_count']
    f.close()


def program_exit():
    global data
    data['current_count'] = current_count

    f = open(data_file, 'w+')
    f.write(json.dumps(data))
    del data
    f.close()
    exit(0)


def shift_array_after_del(arr=[]):
    if len(arr) > 1:
        for widget in arr:
            if (widget == None):
                print('asd')
            print(widget)
        print()


def del_button(label_to_del=None):
    if label_to_del:
        global labels
        label_to_del.destroy()
        # del label_to_del
        labels.remove(label_to_del)
        shift_array_after_del(labels)


def add_new_recipe():
    global labels
    # for i in labels:
    #     print(i)
    # print()
    new_label = tk.Frame(recipe_canvas)
    new_label.grid(row=len(labels) + 1, column=0)
    labels.append(new_label)

    last_label_in_list = labels[len(labels) - 1]
    print('last label: ' + str(last_label_in_list))

    labeltext = tk.StringVar()
    recipe = tk.Label(last_label_in_list, textvariable=labeltext, anchor=tk.W)
    labeltext.set("New recipe " + genstring.generate_string().ljust(10, ' '))
    # labeltext = "New recipe " + genstring.generate_string()
    recipe.grid(row=0, column=0)

    delete_recipe = tk.Button(last_label_in_list, text='X', bg='red', fg='black', command=lambda:del_button(last_label_in_list), anchor=tk.E)
    delete_recipe.grid(row=0, column=1)


data_file = './userdata.json'
data = None
if not exists(data_file):
    print('User data file doesn\'t exist. Creating one...')
    create_data_file(data_file)
load_data_file(data_file)


count_label = tk.Label(main_buttons_canvas, text=current_count, height=5, width=10, bg='black', fg='white', justify=tk.CENTER)
count_label.grid(row=0, pady=(0,20), columnspan=6)

#
# ADD
#
inc_1 = tk.Button(main_buttons_canvas, text='+1', command=lambda:inc(count_label, 1), width=5, bg='black', fg='white')
inc_1.grid(row=1, column=0, padx=5, pady=(5,2)) # Must be on its own line, can't be compounded with the one above

inc_2 = tk.Button(main_buttons_canvas, text='+2', command=lambda:inc(count_label, 2), width=5, bg='black', fg='white')
inc_2.grid(row=1, column=1, padx=5, pady=(5,2))

inc_5 = tk.Button(main_buttons_canvas, text='+5', command=lambda:inc(count_label, 5), width=5, bg='black', fg='white')
inc_5.grid(row=1, column=2, padx=5, pady=(5,2))

inc_10 = tk.Button(main_buttons_canvas, text='+10', command=lambda:inc(count_label, 10), width=5, bg='black', fg='white')
inc_10.grid(row=1, column=3, padx=5, pady=(5,2))

inc_15 = tk.Button(main_buttons_canvas, text='+15', command=lambda:inc(count_label, 15), width=5, bg='black', fg='white')
inc_15.grid(row=1, column=4, padx=5, pady=(5,2))

inc_20 = tk.Button(main_buttons_canvas, text='+20', command=lambda:inc(count_label, 20), width=5, bg='black', fg='white')
inc_20.grid(row=1, column=5, padx=5, pady=(5,2))

#
# SUBTRACT
#
dec_1 = tk.Button(main_buttons_canvas, text='-1', command=lambda:dec(count_label, 1), width=5, bg='black', fg='white')
dec_1.grid(row=2, column=0, padx=5, pady=(2,5))

dec_2 = tk.Button(main_buttons_canvas, text='-2', command=lambda:dec(count_label, 2), width=5, bg='black', fg='white')
dec_2.grid(row=2, column=1, padx=5, pady=(2,5))

dec_5 = tk.Button(main_buttons_canvas, text='-5', command=lambda:dec(count_label, 5), width=5, bg='black', fg='white')
dec_5.grid(row=2, column=2, padx=5, pady=(2,5))

dec_10 = tk.Button(main_buttons_canvas, text='-10', command=lambda:dec(count_label, 10), width=5, bg='black', fg='white')
dec_10.grid(row=2, column=3, padx=5, pady=(2,5))

dec_15 = tk.Button(main_buttons_canvas, text='-15', command=lambda:dec(count_label, 15), width=5, bg='black', fg='white')
dec_15.grid(row=2, column=4, padx=5, pady=(2,5))

dec_20 = tk.Button(main_buttons_canvas, text='-20', command=lambda:dec(count_label, 20), width=5, bg='black', fg='white')
dec_20.grid(row=2, column=5, padx=5, pady=(2,5))

reset_button = tk.Button(main_buttons_canvas, text='RESET', command=lambda:reset(count_label), bg='red', fg='black')
reset_button.grid(row=2, pady=(60,0), columnspan=6)

# separator = ttk.Separator(recipe_canvas, orient='horizontal')
# separator.place(relx=0, rely=0.5, relwidth=1, relheight=0.2)

add_new_recipe_button = tk.Button(recipe_canvas, text='Add new recipe', command=add_new_recipe)
add_new_recipe_button.grid(row=0, column=0)

# root.minsize(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
root.protocol('WM_DELETE_WINDOW', program_exit)
root.resizable(True, True)
root.mainloop()
