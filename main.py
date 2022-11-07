import PySimpleGUI as sg
import csv_handler
import os
import platform
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import graph

# Helper function
matplotlib.use("TkAgg")
def draw_sample_figure(canvas, figure):
    '''Create the sample figure on the GUI's front page'''
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg



layout = [
    [sg.Text('Please enter the year and month as numbers')], 
    [sg.Text('Year', size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text('Month', size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text('Please fill out at least one of the relevant expense data fields below (default is 0)')],
    [sg.Text('Water', size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text('Phone', size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text('Electric', size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text('Groceries', size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text('Housing', size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text('Automotive', size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text('Tithes', size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Text('Misc', size=(15, 1)), sg.InputText(do_not_clear=False)],
    [sg.Submit(), sg.Button('View Data'), sg.Cancel()],
    [sg.Text('Graphs'),sg.Button('All')],
    [sg.Text('if you want to view a specific month, please enter the year and month')],
    [sg.Text('Graphs by Year'),sg.Button('Year'), sg.InputText(do_not_clear=False)],
    [sg.Text('Graphs by Month'),sg.Button('Month'), sg.InputText(do_not_clear=False)],
        ]
keyList = ['Year', 'Month', 'Water', 'Phone', 'Electric', 'Groceries', 'Housing', 'Automotive', 'Tithes', 'Misc', 'Total']

window = sg.Window('Expense Tracker', layout)

while True:
    event, values = window.read() 
    b = list(values.values())[:-2]
    year_month = list(values.values())[-2:]
    if event == sg.WIN_CLOSED:
        break



    # if any field is filled out, then the data is added to the database
    if any(b) or event == "Submit":
        temp = True
        # if date or month is not filled, then the data is not added to the database
        if True:
            for i in range(2, 11):
                # i = int(i)
                # if not (abs(values[i]) == values[i] and (isinstance(values[i], int) or isinstance(values[i], float))):
                #     sg.popup('Please enter a year and a month.', title='ERROR')
                #     break
                if values[i].isdigit() or values[i] == '':
                    continue
                else:
                    sg.popup('Not a valid input.', title='ERROR')
                    temp = False
                    break
                # if not (values[i].isdigit() and values[i]) != '':
                #     sg.popup('Not a valid input.', title='ERROR')
                #     temp = False
                #     break

        if (values[0] == '' or values[1] == '') and values[1] in range(1, 13): 
            sg.popup('Please enter a year and a month.', title='ERROR')
            temp = False
        if temp:
            csv_handler.add_record(b)

        
    if event == "View Data":
        csv_handler.view_records()
        # ideally open expense.csv in a spreadsheet program
        
        # This is for opening in a spreadsheet program
        if not platform.system() in ("Linux", "Windows"):
            os.system("open expense.csv")
        else:
            sg.popup("Please open expense.csv in a spreadsheet program and edit it there.")
    
    if event == 'Cancel':
        event = sg.popup_yes_no('Are you sure you want to clear all expense data?', title='WARNING')
        if event == 'Yes':
            # clear all data entered in the fields
            for item in keyList:
                window[item].update('')

    if event == "All":
        graph.expense_distribution()
    
    if event == "Month" or event == "Year":
        if year_month[0] == '' or year_month[1] == '':
            sg.popup('Please enter a year and a month.', title='ERROR')
        elif not(year_month[1].isdigit() or year_month[0].digit()):
            sg.popup('Not a valid input.', title='ERROR')

        else:
            graph.expense_distribution_year_month(int(year_month[1]), int(year_month[0]))
