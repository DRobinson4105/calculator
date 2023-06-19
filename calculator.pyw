# Import required libraries
from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions import *
from latexConverter import *

matplotlib.use('TkAgg')

displayAnswer = False

def calculate():
    global displayAnswer
    displayAnswer = True

def reset():
    global displayAnswer
    displayAnswer = False
    entry.delete(0, END)

# Displays given expression in LaTex format and result
def graph():
    # Prevents program from crashing when invalid input is given
	try:
		# Get the entry input
		expression = entry.get()

		# Displaying expression
		if not displayAnswer:
			global lastExpression
			lastExpression = expression

		# Displaying answer
		else:
			expression = str(solve(lastExpression))

		# Convert expression to latex format
		expression = convertToLaTex(expression)

		# Only setup expression if expression is not empty
		expression = "$"+expression+"$" if expression != "" else ""

		# Clear any previous text from the figure
		wx.clear()
		wx.text(0.5, 0.5, expression, fontsize = 20, ha='center', va='center')
		canvas.draw()

	except: pass

	win.after(100,graph)

# Create an instance of tkinter frame
win = Tk()
win.geometry("700x350")
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