import tkinter as tk

btn_color = 'orange'
btn_font = 'Arial 20 bold'
btn_width = 3
btn_height = 1

class Calculator:
    def __init__(self):
        self.w = tk.Tk()
        self.w.title('Calculator')
        self.w.config(bg='#1d2f38')
        # Lo siguiente es para que no se modifique el tamaño de la ventana.
        self.w.resizable(0,0)

        
        # Widget creation:
        self.screen = tk.Entry(self.w, font='Arial 20 bold', bg='#1d2f38', fg='white', width=18)
        self.frame = tk.Frame(self.w, bg='#1d2f38', padx=10, pady=10)

        self.btn_clear = tk.Button(self.frame, bg='#ff4400', text='C', font=btn_font, width=10, height=btn_height, command=self.clear_screen)
        self.btn_division = tk.Button(self.frame, bg=btn_color, text='/', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('/'))

        self.btn_7 = tk.Button(self.frame, bg=btn_color, text='7', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('7'))
        self.btn_8 = tk.Button(self.frame, bg=btn_color, text='8', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('8'))
        self.btn_9 = tk.Button(self.frame, bg=btn_color, text='9', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('9'))
        self.btn_multiplication = tk.Button(self.frame, bg=btn_color, text='X', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('*'))
        
        self.btn_4 = tk.Button(self.frame, bg=btn_color, text='4', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('4'))
        self.btn_5 = tk.Button(self.frame, bg=btn_color, text='5', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('5'))
        self.btn_6 = tk.Button(self.frame, bg=btn_color, text='6', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('6'))
        self.btn_difference = tk.Button(self.frame, bg=btn_color, text='-', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('-'))

        self.btn_1 = tk.Button(self.frame, bg=btn_color, text='1', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('1'))
        self.btn_2 = tk.Button(self.frame, bg=btn_color, text='2', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('2'))
        self.btn_3 = tk.Button(self.frame, bg=btn_color, text='3', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('3'))
        self.btn_sum = tk.Button(self.frame, bg=btn_color, text='+', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('+'))
        
        self.btn_negative = tk.Button(self.frame, bg=btn_color, text='+/-', font=btn_font, width=btn_width, height=btn_height, command=self.negative)
        self.btn_0 = tk.Button(self.frame, bg=btn_color, text='0', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('0'))
        self.btn_dot = tk.Button(self.frame, bg=btn_color, text='.', font=btn_font, width=btn_width, height=btn_height, command= lambda: self.press_key('.'))
        self.btn_equals = tk.Button(self.frame, bg=btn_color, text='=', font=btn_font, width=btn_width, height=btn_height, command= self.evaluate_expression)
        
        
        # Widget placing:
        self.screen.pack()
        self.frame.pack()

        self.btn_clear.grid(row=0, column=0, columnspan=3)
        self.btn_division.grid(row=0, column=3)

        self.btn_7.grid(row=1,column=0)
        self.btn_8.grid(row=1,column=1)
        self.btn_9.grid(row=1,column=2)
        self.btn_multiplication.grid(row=1, column=3)

        self.btn_4.grid(row=2,column=0)
        self.btn_5.grid(row=2,column=1)
        self.btn_6.grid(row=2,column=2)
        self.btn_difference.grid(row=2,column=3)

        self.btn_1.grid(row=3,column=0)
        self.btn_2.grid(row=3,column=1)
        self.btn_3.grid(row=3,column=2)
        self.btn_sum.grid(row=3,column=3)

        self.btn_negative.grid(row=4, column=0)
        self.btn_0.grid(row=4,column=1)
        self.btn_dot.grid(row=4, column=2)
        self.btn_equals.grid(row=4,column=3)

        self.w.mainloop()
    
    def press_key(self, num):
        self.screen.insert(tk.END, num)
    
    def clear_screen(self):
        self.screen.delete(0, tk.END)

    def evaluate_expression(self):
        try:
            result = eval(self.screen.get())
            self.screen.delete(0, tk.END)
            self.screen.insert(0, str(result))
        except SyntaxError:
            self.screen.delete(0, tk.END)
            self.screen.insert(0, "Syntax Error")
    
    def negative(self):
        try:
            number = eval(self.screen.get())
            number *= -1
            self.screen.delete(0, tk.END)
            self.screen.insert(0, str(number))
        except SyntaxError:
            self.screen.delete(0, tk.END)
            self.screen.insert(0, 'Invalid syntax')

Calculator()