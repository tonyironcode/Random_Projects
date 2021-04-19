from tkinter import *
root = Tk()
root.geometry("450x200")
root.title("Gab's Budget Calculator")
root.config(background="#363636")

# Greeting Label
greeting_label = Label(root, text="Welcome to Gab's Budget Calculator", bg="#363636", fg="#ffffff")
greeting_label.grid(column=1, row=1)

# Monthly Income Label and Entry
income_label = Label(root, text="Monthly Income: ", bg="#363636", fg="#ffffff")
income_label.grid(column=1, row=2)
income_entry = Entry(root, width=30)
income_entry.grid(column=2, row=2)

# Monthly Expense 1
expense1 = Label(root, text="Monthly Expense 1: ", bg="#363636", fg="#ffffff")
expense1.grid(column=1, row=3)
expense1_entry = Entry(root, width=30)
expense1_entry.grid(column=2, row=3)

# Monthly Expense 2
expense2 = Label(root, text="Monthly Expense 2: ", bg="#363636", fg="#ffffff")
expense2.grid(column=1, row=4)
expense2_entry = Entry(root, width=30)
expense2_entry.grid(column=2, row=4)

# Monthly Expense 3
expense3 = Label(root, text="Monthly Expense 3: ", bg="#363636", fg="#ffffff")
expense3.grid(column=1, row=5)
expense3_entry = Entry(root, width=30)
expense3_entry.grid(column=2, row=5)

# Monthly Expense 4
expense4 = Label(root, text="Monthly Expense 4: ", bg="#363636", fg="#ffffff")
expense4.grid(column=1, row=6)
expense4_entry = Entry(root, width=30)
expense4_entry.grid(column=2, row=6)

# Monthly Expense 5
expense5 = Label(root, text="Monthly Expense 5: ", bg="#363636", fg="#ffffff")
expense5.grid(column=1, row=7)
expense5_entry = Entry(root, width=30)
expense5_entry.grid(column=2, row=7)

# Calculate Button
def calculate():
    budget_label = Label(root, text="Monthly Budget: ", bg="#363636", fg="#ffffff")
    budget_label.grid(column=1, row=9)
    budget_label2 = Label(root, text=int(income_entry.get()) - (int(expense1_entry.get()) + int(expense2_entry.get()) + int(expense3_entry.get()) + int(expense4_entry.get()) + \
    int(expense5_entry.get())))
    budget_label2.grid(column=2, row=9)


calculate_button = Button(root, width=15, height=1, text="Calculate", command=calculate)
calculate_button.grid(column=2, row=8)
budget_label = Label(root, text="Monthly Budget: ", bg="#363636", fg="#ffffff")
budget_label.grid(column=1, row=9)

root.mainloop()


