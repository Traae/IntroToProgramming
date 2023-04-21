# Project Name: Date Night Calculator
# CS 1181
# Traae Bloxham
# 11/14/2019
# Brandon Carpenter
# Description - A project that I can only assume would be easier with classes



# import the tks, create my widow and title it.
import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Date Night Calculator")

# creat a bunch of global variables to use in my buttons
# I originally had a lot more absrtaction, but I had to scrap it
# I chose to still use these because I hadn't used them before
global travel_cost
travel_cost = tk.IntVar() # each of these that is a button variable is intitialized as such here
global entertaiment_cost
entertaiment_cost = tk.IntVar()
global dinner_cost
dinner_cost = tk.IntVar()
global taxes_entry
taxes_entry = tk.StringVar()
global tips_percent
tips_percent = tk.IntVar()
global date_total
date_total = 00.00


def calculate_cost():
    global travel_cost
    global entertaiment_cost
    global dinner_cost
    global taxes_entry
    global tips_percent
    global date_total
    travel = travel_cost.get()
    entertaiment = entertaiment_cost.get()
    dinner = dinner_cost.get()
    taxes = taxes_entry.get()
    tips = tips_percent.get()
    taxes = (float(taxes) / 100) + 1
    travel = travel * taxes
    entertaiment = entertaiment * taxes
    tips = (float(tips) / 100) * dinner
    dinner = dinner * taxes
    date_total = round((travel + entertaiment + dinner + taxes + tips), 2)
    total_display["text"] = "$" + str(date_total)



# This will cover the travel section. first set up the frame. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
travelbuttons = ttk.LabelFrame(window, text="Travel", relief=tk.RIDGE, padding=5)
travelbuttons.grid(row=1, column=1)
# TRB~ - travel radio button + name
# travel_cost = tk.IntVar()
TRBcar = ttk.Radiobutton(travelbuttons, text="Car ($5)", variable=travel_cost, value=5)
TRBcar.grid(row=1, column=1, sticky=tk.W)
TRBbus = ttk.Radiobutton(travelbuttons, text="Bus ($1)", variable=travel_cost, value=1)
TRBbus.grid(row=2, column=1, sticky=tk.W)
TRBuber = ttk.Radiobutton(travelbuttons, text="Uber ($30)", variable=travel_cost, value=30)
TRBuber.grid(row=3, column=1, sticky=tk.W)
TRBlimo = ttk.Radiobutton(travelbuttons, text="Limo ($100)", variable=travel_cost, value=100)
TRBlimo.grid(row=4, column=1, sticky=tk.W)


# This will cover the entertainment section. first set up the frame.  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
entertainmentButtons = ttk.LabelFrame(window, text="Entertainment", relief=tk.RIDGE, padding=5)
entertainmentButtons.grid(row=2, column=1)
# erb- entertainment radio buttons  plus name
# entertaiment_cost = tk.IntVar()
erb_walk = ttk.Radiobutton(entertainmentButtons, text="Walk ($0)", variable=entertaiment_cost, value=0)
erb_walk.grid(row=1, column=1, sticky=tk.W)
erb_minigolf = ttk.Radiobutton(entertainmentButtons, text="Mini Golf ($10)", variable=entertaiment_cost, value=10)
erb_minigolf.grid(row=2, column=1, sticky=tk.W)
erb_movie = ttk.Radiobutton(entertainmentButtons, text="Movie ($26)", variable=entertaiment_cost, value=26)
erb_movie.grid(row=3, column=1, sticky=tk.W)


# This will cover the dinne section. first set up the frame. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``````````
DindinButtons = ttk.LabelFrame(window, text="Dinner", relief=tk.RIDGE, padding=5)
DindinButtons.grid(row=1, column=2)
# drb- entertainment radio buttons  plus name
erb_walk = ttk.Radiobutton(DindinButtons, text="Fast Food ($20)", variable=dinner_cost, value=20)
erb_walk.grid(row=1, column=1, sticky=tk.W)
erb_minigolf = ttk.Radiobutton(DindinButtons, text="Home Made ($15)", variable=dinner_cost, value=15)
erb_minigolf.grid(row=2, column=1, sticky=tk.W)
erb_movie = ttk.Radiobutton(DindinButtons, text="Restaurant ($30)", variable=dinner_cost, value=30)
erb_movie.grid(row=3, column=1, sticky=tk.W)

# Taxes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
taxesframe = ttk.LabelFrame(window, text="Taxes in %")
taxesframe.grid(row=3, column=1)
taxes_entry = ttk.Entry(taxesframe, width=10)
taxes_entry.grid(row=1, column=1)
taxes_entry.insert(tk.END, 0)

# TIPS ~~~~~~~~~~~~~~~~~~~~~~
tips_frame = ttk.LabelFrame(window, text="Tips in %")
tips_frame.grid(row=2, column=2)
tips_scale = tk.Scale(tips_frame, from_=0, to=30, width=10, length=90, variable=tips_percent, orient=tk.HORIZONTAL)
tips_scale.grid(row=1, column=1)





# travel_buttons()
# entertainment_buttons()
# dinner_buttons()
# get_taxes()
# get_tips()

totalframe = ttk.LabelFrame(window, text="Total")
totalframe.grid(row=7, column=2)
total_display = tk.Label(totalframe)
total_display.grid(row=1, column=1)
calculation_station = tk.Button(totalframe, text="Calculate Cost", command=calculate_cost)
calculation_station.grid(row=2, column=1)


window.mainloop()


# end program