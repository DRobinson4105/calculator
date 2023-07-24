from tkinter import *
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions import solve
from latexConverter import convertToLaTex

matplotlib.use('TkAgg')

# Initial values
global displayAnswer
displayAnswer = False
global lastExpression
lastExpression = ""

# Calculate button
def calculate():
    global lastExpression
    lastExpression = expression
    global displayAnswer
    displayAnswer = True

# Reset button
def reset():
    global displayAnswer
    displayAnswer = False
    entry.delete(0, END)

# Displays given expression in LaTex format and result
def graph():
    # Prevents program from crashing when invalid input is given
	try:
		# Get the entry input
		global expression
		expression = entry.get()
		display = expression

		# If user has changed input
		global displayAnswer
		if expression != lastExpression:
			displayAnswer = False

		# Displaying answer
		if displayAnswer and display != '':
			display = str(solve(lastExpression))

		# Convert expression to latex format
		display = convertToLaTex(display)

		# Only setup expression if expression is not empty
		display = "$"+display+"$" if display != "" else ""

		wx.clear()
		wx.text(0.5, 0.5, display, fontsize = 20, ha='center', va='center')
		canvas.draw()

	except:
		if displayAnswer:
			wx.clear()
			wx.text(0.5, 0.5, "Invalid input", fontsize = 20, ha='center', va='center')
			canvas.draw()

	win.after(100,graph)

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x200")
win.title("Calculator")

# Create a Frame object
frame = Frame(win)
frame.pack()

# Create an Entry widget
var = StringVar()
entry = Entry(frame, width=70, textvariable=var)
entry.pack()

# Add a label widget in the frame
label = Label(frame)
label.pack()

# Calculate and Reset Buttons
calculateB = ttk.Button(win, text="Calculate", command=calculate)
resetB = ttk.Button(win, text="Reset", command=reset)
calculateB.pack()
resetB.pack()

# Define the figure size and plot the figure
fig = matplotlib.figure.Figure(figsize=(7, 1), dpi=100)
wx = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=label)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

# Set the visibility of the Canvas figure
wx.get_xaxis().set_visible(False)
wx.get_yaxis().set_visible(False)

win.after(100,graph)
win.mainloop()