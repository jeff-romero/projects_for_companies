#GitHub: jeff-romero

import settings
import modules

class Tkcalculator:
    def __init__(self, calculator_frame):
        self.expression = []
        self.currentnum = '0'
        self.expression_was_evaluated = False
        self.display_value = modules.tk.StringVar()
        self.display_value.set(self.currentnum)
        self.display = modules.tk.Label(calculator_frame, textvariable=self.display_value, bg='black', fg='white', width=86, height=4, anchor=modules.tk.E)
        self.display.grid(row=0, column=0, columnspan=4)
        self.clear = modules.tk.Button(calculator_frame, text='C', command=lambda:self.calculator_command('C'), bg='black', fg='white', width=20, height=4)
        self.clear.grid(row=1, column=0)
        self.flip_sign = modules.tk.Button(calculator_frame, text='+/-', command=lambda:self.calculator_command('+/-'), bg='black', fg='white', width=20, height=4)
        self.flip_sign.grid(row=1, column=1)
        self.percent = modules.tk.Button(calculator_frame, text='%', command=lambda:self.calculator_command('%'), bg='black', fg='white', width=20, height=4)
        self.percent.grid(row=1, column=2)
        self.divide = modules.tk.Button(calculator_frame, text='/', command=lambda:self.calculator_command('/'), bg='black', fg='white', width=20, height=4)
        self.divide.grid(row=1, column=3)
        self.seven = modules.tk.Button(calculator_frame, text='7', command=lambda:self.calculator_command('7'), bg='black', fg='white', width=20, height=4)
        self.seven.grid(row=2, column=0)
        self.eight = modules.tk.Button(calculator_frame, text='8', command=lambda:self.calculator_command('8'), bg='black', fg='white', width=20, height=4)
        self.eight.grid(row=2, column=1)
        self.nine = modules.tk.Button(calculator_frame, text='9', command=lambda:self.calculator_command('9'), bg='black', fg='white', width=20, height=4)
        self.nine.grid(row=2, column=2)
        self.multiply = modules.tk.Button(calculator_frame, text='*', command=lambda:self.calculator_command('*'), bg='black', fg='white', width=20, height=4)
        self.multiply.grid(row=2, column=3)
        self.four = modules.tk.Button(calculator_frame, text='4', command=lambda:self.calculator_command('4'), bg='black', fg='white', width=20, height=4)
        self.four.grid(row=3, column=0)
        self.five = modules.tk.Button(calculator_frame, text='5', command=lambda:self.calculator_command('5'), bg='black', fg='white', width=20, height=4)
        self.five.grid(row=3, column=1)
        self.six = modules.tk.Button(calculator_frame, text='6', command=lambda:self.calculator_command('6'), bg='black', fg='white', width=20, height=4)
        self.six.grid(row=3, column=2)
        self.minus = modules.tk.Button(calculator_frame, text='-', command=lambda:self.calculator_command('-'), bg='black', fg='white', width=20, height=4)
        self.minus.grid(row=3, column=3)
        self.one = modules.tk.Button(calculator_frame, text='1', command=lambda:self.calculator_command('1'), bg='black', fg='white', width=20, height=4)
        self.one.grid(row=4, column=0)
        self.two = modules.tk.Button(calculator_frame, text='2', command=lambda:self.calculator_command('2'), bg='black', fg='white', width=20, height=4)
        self.two.grid(row=4, column=1)
        self.three = modules.tk.Button(calculator_frame, text='3', command=lambda:self.calculator_command('3'), bg='black', fg='white', width=20, height=4)
        self.three.grid(row=4, column=2)
        self.plus = modules.tk.Button(calculator_frame, text='+', command=lambda:self.calculator_command('+'), bg='black', fg='white', width=20, height=4)
        self.plus.grid(row=4, column=3)
        self.zero = modules.tk.Button(calculator_frame, text='0', command=lambda:self.calculator_command('0'), bg='black', fg='white', width=42, height=4)
        self.zero.grid(row=5, column=0, columnspan=2)
        self.point = modules.tk.Button(calculator_frame, text='.', command=lambda:self.calculator_command('.'), bg='black', fg='white', width=20, height=4)
        self.point.grid(row=5, column=2)
        self.equal = modules.tk.Button(calculator_frame, text='=', command=lambda:self.calculator_command('='), bg='black', fg='white', width=20, height=4)
        self.equal.grid(row=5, column=3)

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

    def isfloat(self, x):
        try:
            float(x)
            return True
        except:
            return False

    def reset_calculator(self):
        self.expression = []
        self.currentnum = '0'
        self.display_value.set(self.currentnum)
        return True

    def update_display(self, char_to_add=''):
        if len(char_to_add) > 0:

            curr_display_value = self.display_value.get()

            if self.isfloat(char_to_add): # All natural numbers such as 1, 2, 3, 45, 678, 9101112, ...
                print('update_display(): char ' + char_to_add + ' is a float')
                if curr_display_value == '0': # Avoids unnecessary zero padding such as 01, 02, ..., 09999
                    self.display_value.set(char_to_add)
                    self.currentnum = char_to_add
                else:
                    curr_display_value += char_to_add
                    self.currentnum += char_to_add
                    self.display_value.set(curr_display_value)
                print('update_display(): display value is ' + self.display_value.get() + '\nupdate_display(): currentnum is ' + self.currentnum)
                return True
            else: # Can be . or an operator (-, +, /, *)
                if char_to_add == '.':
                    print('update_display(): char ' + char_to_add + ' is .' + '\nupdate_display(): currentnum is ' + self.currentnum)
                    if len(self.expression) > 0:
                        print('update_display(): ' + str(self.expression[len(self.expression) - 1]))

                    if len(self.currentnum) > 0:
                        if not self.currentnum.__contains__('.'):
                            self.currentnum += char_to_add
                        elif len(self.expression) > 0 and self.currentnum.__contains__('.'):
                            newcurrentnum = self.expression.pop(len(self.expression) - 1)
                            print('update_display(): removed ' + newcurrentnum + ' from the expression')
                            if newcurrentnum.__contains__('.0'): # Cut ".0" from the end of the result if present
                                newcurrentnum = newcurrentnum.split('.')[0]
                            newcurrentnum += '.' # I should fix this, doesn't look right
                            print('update_display(): new current num is ' + newcurrentnum)
                            self.currentnum = newcurrentnum
                        else:
                            # Number cannot have more than one decimal (Ex: 1.2.3.4.5 OR ...1.2.3)
                            print('update_display(): Number cannot have more than one decimal')
                            return False
                elif char_to_add == '-' or char_to_add == '+' or char_to_add == '/' or char_to_add == '/' or char_to_add == '*':
                    print('update_display(): char ' + str(char_to_add) + ' is an operator\nupdate_display(): currentnum is ' + self.currentnum + ' with a length of ' + str(len(self.currentnum)))
                    # Since char is an operand, it can't be appended to the current number string, so add the current number string to the calculator queue and empty it.
                    if len(self.currentnum) > 0:
                        self.expression.append(self.currentnum)
                    self.currentnum = ''
                    self.expression.append(char_to_add)
                else:
                    print('update_display(): char ' + str(char_to_add) + ' not recognized')
                    return False
                curr_display_value += char_to_add
                self.display_value.set(curr_display_value)
            print('update_display(): current num -> ' + self.currentnum + '\nupdate_display(): Expression now looks like -> ' + str(self.expression))
            return True
        return False

    def evaluate_expression(self, exp):
        print('evaluate_expression(): ' + str(exp))
        if len(exp) >= 3:
            left_operand, operator, right_operand = float(exp.pop(0)), exp.pop(0), float(exp.pop(0))
            print(str(left_operand) + ' ' + operator + ' ' + str(right_operand))
            if operator == '+':
                result = self.add(left_operand, right_operand)
            elif operator == '-':
                result = self.sub(left_operand, right_operand)
            elif operator == '*':
                result = self.mul(left_operand, right_operand)
            elif operator == '/':
                result = self.div(left_operand, right_operand)
            result = str(result)
            exp.insert(0, result)
            return self.evaluate_expression(exp)
        return exp[0]

    def calculator_command(self, char=''):
        # if self.expression_was_evaluated: # Kept separate from CLEAR/'C'
        #     self.reset_calculator()
        #     self.expression_was_evaluated = False
        print('calculator_command(): Character ' + char + ' was entered\ncalculator_command(): currentnum is ' + self.currentnum)
        if char == 'C':
            self.reset_calculator()
        elif char.isnumeric() or char == '.' or char == '/' or char == '*' or char == '-' or char == '+':
            print('calculator_command(): Entering update calc display')
            self.update_display(char_to_add=char)
            return True
        elif (char == '+/-' or char == '%') and self.isfloat(self.currentnum):
            result = 0.0

            if char == '+/-':
                if self.currentnum.__contains__('.'):
                    result = float(self.currentnum) * -1.0
                else:
                    result = int(self.currentnum) * -1
            elif char == '%':
                result = float(self.currentnum) * .01

            result = str(result)

            display = ''
            for i in self.expression: # Number may not be the first in the expression, so clear display then set as entire expression
                display += i
            display += result
            self.display_value.set(display)

            self.currentnum = result
            print('calculator_command(): Expression after evaluation -> ' + str(self.expression))
            return True
        elif char == '=':
            print('calculator_command(): Going to evaluate the expression (=): ' + str(self.expression))
            if self.display_value.get() != '0' and len(self.expression) >= 2 and len(self.currentnum) > 0:
                print('calculator_command(): Appending ' + self.currentnum + ' to the expression')
                self.expression.append(self.currentnum) # Append the operand after the operator (Example: Expression looks like this after this line is executed: ['1', '+', '2'])
                print('calculator_command(): Expression now looks like -> ' + str(self.expression))

                result = str(self.evaluate_expression(self.expression))
                
                if self.currentnum != result:
                    if result.__contains__('.0'): # Cut ".0" from the end of the result if present
                        result = result.split('.0')[0]
                    self.currentnum = result
                    self.display_value.set(result)
                    self.expression = []
                    self.expression_was_evaluated = True
                    print('calculator_command(): Evaluation result -> ' + result + ' ... Expression now looks like -> ' + str(self.expression) + '\n\n')
                return True
            return False
        else:
            print('calculator_command(): Command ' + char + ' not recognized')
            return False
