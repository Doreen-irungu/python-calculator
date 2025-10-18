"""
Basic Calculator with GUI
Author: Doreen Irungu
Description: A simple calculator application with a graphical user interface
Built with Python tkinter
"""

import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator - Doreen Irungu")
        self.window.geometry("400x500")
        self.window.resizable(False, False)
        self.window.configure(bg="#2c3e50")
        
        # Variables to store calculation data
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.result_displayed = False
        
        self.create_widgets()
        
    def create_widgets(self):
        """Create all the calculator widgets"""
        
        # Display frame
        display_frame = tk.Frame(self.window, bg="#2c3e50")
        display_frame.pack(pady=20)
        
        # Result display
        self.display = tk.Entry(
            display_frame,
            font=("Arial", 24, "bold"),
            width=15,
            justify="right",
            bd=0,
            bg="#34495e",
            fg="black",
            state="readonly"
        )
        self.display.pack(ipady=20)
        
        # Update display
        self.update_display()
        
        # Buttons frame
        buttons_frame = tk.Frame(self.window, bg="#2c3e50")
        buttons_frame.pack(pady=10)
        
        # Button configuration
        button_config = {
            "font": ("Arial", 16, "bold"),
            "width": 5,
            "height": 2,
            "bd": 0,
            "cursor": "hand2"
        }
        
        # Row 1: Clear, Delete, Square Root, Divide
        tk.Button(buttons_frame, text="C", bg="#e74c3c", fg="white", 
                 command=self.clear, **button_config).grid(row=0, column=0, padx=2, pady=2)
        tk.Button(buttons_frame, text="⌫", bg="#f39c12", fg="white", 
                 command=self.delete, **button_config).grid(row=0, column=1, padx=2, pady=2)
        tk.Button(buttons_frame, text="√", bg="#9b59b6", fg="white", 
                 command=self.square_root, **button_config).grid(row=0, column=2, padx=2, pady=2)
        tk.Button(buttons_frame, text="÷", bg="#3498db", fg="white", 
                 command=lambda: self.set_operator("/"), **button_config).grid(row=0, column=3, padx=2, pady=2)
        
        # Row 2: 7, 8, 9, Multiply
        tk.Button(buttons_frame, text="7", bg="#7f8c8d", fg="white", 
                 command=lambda: self.add_digit("7"), **button_config).grid(row=1, column=0, padx=2, pady=2)
        tk.Button(buttons_frame, text="8", bg="#7f8c8d", fg="white", 
                 command=lambda: self.add_digit("8"), **button_config).grid(row=1, column=1, padx=2, pady=2)
        tk.Button(buttons_frame, text="9", bg="#7f8c8d", fg="white", 
                 command=lambda: self.add_digit("9"), **button_config).grid(row=1, column=2, padx=2, pady=2)
        tk.Button(buttons_frame, text="×", bg="#3498db", fg="white", 
                 command=lambda: self.set_operator("*"), **button_config).grid(row=1, column=3, padx=2, pady=2)
        
        # Row 3: 4, 5, 6, Subtract
        tk.Button(buttons_frame, text="4", bg="#7f8c8d", fg="white", 
                 command=lambda: self.add_digit("4"), **button_config).grid(row=2, column=0, padx=2, pady=2)
        tk.Button(buttons_frame, text="5", bg="#7f8c8d", fg="white", 
                 command=lambda: self.add_digit("5"), **button_config).grid(row=2, column=1, padx=2, pady=2)
        tk.Button(buttons_frame, text="6", bg="#7f8c8d", fg="white", 
                 command=lambda: self.add_digit("6"), **button_config).grid(row=2, column=2, padx=2, pady=2)
        tk.Button(buttons_frame, text="−", bg="#3498db", fg="white", 
                 command=lambda: self.set_operator("-"), **button_config).grid(row=2, column=3, padx=2, pady=2)
        
        # Row 4: 1, 2, 3, Add
        tk.Button(buttons_frame, text="1", bg="#7f8c8d", fg="white", 
                 command=lambda: self.add_digit("1"), **button_config).grid(row=3, column=0, padx=2, pady=2)
        tk.Button(buttons_frame, text="2", bg="#7f8c8d", fg="white", 
                 command=lambda: self.add_digit("2"), **button_config).grid(row=3, column=1, padx=2, pady=2)
        tk.Button(buttons_frame, text="3", bg="#7f8c8d", fg="white", 
                 command=lambda: self.add_digit("3"), **button_config).grid(row=3, column=2, padx=2, pady=2)
        tk.Button(buttons_frame, text="+", bg="#3498db", fg="white", 
                 command=lambda: self.set_operator("+"), **button_config).grid(row=3, column=3, padx=2, pady=2)
        
        # Row 5: +/-, 0, ., Equals
        tk.Button(buttons_frame, text="±", bg="#95a5a6", fg="white", 
                 command=self.toggle_sign, **button_config).grid(row=4, column=0, padx=2, pady=2)
        tk.Button(buttons_frame, text="0", bg="#7f8c8d", fg="white", 
                 command=lambda: self.add_digit("0"), **button_config).grid(row=4, column=1, padx=2, pady=2)
        tk.Button(buttons_frame, text=".", bg="#95a5a6", fg="white", 
                 command=self.add_decimal, **button_config).grid(row=4, column=2, padx=2, pady=2)
        tk.Button(buttons_frame, text="=", bg="#27ae60", fg="white", 
                 command=self.calculate, **button_config).grid(row=4, column=3, padx=2, pady=2)
        
        # Add keyboard bindings
        self.window.bind('<Key>', self.key_press)
        self.window.focus_set()
        
    def update_display(self):
        """Update the calculator display"""
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current)
        self.display.config(state="readonly")
        
    def add_digit(self, digit):
        """Add a digit to the current number"""
        if self.result_displayed:
            self.current = "0"
            self.result_displayed = False
            
        if self.current == "0":
            self.current = digit
        else:
            self.current += digit
        self.update_display()
        
    def add_decimal(self):
        """Add decimal point"""
        if self.result_displayed:
            self.current = "0"
            self.result_displayed = False
            
        if "." not in self.current:
            self.current += "."
        self.update_display()
        
    def set_operator(self, op):
        """Set the mathematical operator"""
        if self.operator and not self.result_displayed:
            self.calculate()
            
        self.previous = self.current
        self.operator = op
        self.current = "0"
        self.result_displayed = False
        
    def calculate(self):
        """Perform the calculation"""
        if self.operator and self.previous:
            try:
                if self.operator == "+":
                    result = float(self.previous) + float(self.current)
                elif self.operator == "-":
                    result = float(self.previous) - float(self.current)
                elif self.operator == "*":
                    result = float(self.previous) * float(self.current)
                elif self.operator == "/":
                    if float(self.current) == 0:
                        messagebox.showerror("Error", "Cannot divide by zero!")
                        return
                    result = float(self.previous) / float(self.current)
                
                # Format result
                if result.is_integer():
                    self.current = str(int(result))
                else:
                    self.current = str(round(result, 8))
                    
                self.operator = ""
                self.previous = ""
                self.result_displayed = True
                self.update_display()
                
            except ValueError:
                messagebox.showerror("Error", "Invalid calculation!")
                self.clear()
                
    def clear(self):
        """Clear all data"""
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.result_displayed = False
        self.update_display()
        
    def delete(self):
        """Delete last digit"""
        if len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"
        self.update_display()
        
    def toggle_sign(self):
        """Toggle positive/negative sign"""
        if self.current != "0":
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
        self.update_display()
        
    def square_root(self):
        """Calculate square root"""
        try:
            num = float(self.current)
            if num < 0:
                messagebox.showerror("Error", "Cannot calculate square root of negative number!")
                return
            result = math.sqrt(num)
            if result.is_integer():
                self.current = str(int(result))
            else:
                self.current = str(round(result, 8))
            self.result_displayed = True
            self.update_display()
        except ValueError:
            messagebox.showerror("Error", "Invalid number!")
            
    def key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        
        # Numbers
        if key.isdigit():
            self.add_digit(key)
        # Operators
        elif key == "+":
            self.set_operator("+")
        elif key == "-":
            self.set_operator("-")
        elif key == "*":
            self.set_operator("*")
        elif key == "/":
            self.set_operator("/")
        # Special keys
        elif key == ".":
            self.add_decimal()
        elif key == "\r":  # Enter key
            self.calculate()
        elif event.keysym == "BackSpace":
            self.delete()
        elif event.keysym == "Escape":
            self.clear()
            
    def run(self):
        """Start the calculator application"""
        self.window.mainloop()

# Run the calculator
if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()