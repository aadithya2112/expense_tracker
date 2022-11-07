import matplotlib.pyplot as plt
import csv
import PySimpleGUI as sg
# 
x = ['Year', 'Month', 'Water', 'Phone', 'Electric', 'Groceries', 'Housing', 'Automotive', 'Tithes', 'Misc']  # this to be categories


def expense_distribution(): 
    y = []
    with open('expense.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')
        # rows1 = [123,213,123,123,213,12,2,213,31,12321]
        # row2 = [123,123,123,123,123,,,1234,3,223]
        for array in list(plots)[1:]:
            array = array[2:]
            for index, item in enumerate(array):
                
                try:
                    if not item == '':    
                        y[index] += int(item)
                except:
                    y.append(int(item))


    plt.bar(x[2:], y, color = 'g', width = 0.8, label = "Expense distribution")
    plt.xlabel('categories')
    plt.ylabel('expenditure')
    plt.title('Expense distribution')
    plt.legend()
    plt.show()

def expense_distribution_year_month(month=None, year=None):
    try:
        y = []
        with open('expense.csv','r') as csvfile:
            plots = csv.reader(csvfile, delimiter = ',')
            # rows1 = [123,213,123,123,213,12,2,213,31,12321]
            # row2 = [123,123,123,123,123,,,1234,3,223]
            for array in list(plots)[1:]:
                # ['2022', '2', '123', '123', '213', '12', '2', '213', '31', '12321']
                # print(int(array[0]) == year)
                # print(int(array[1]) == month)
                if int(array[0]) == year or int(array(1)) == month:
                    array = array[2:]
                    for index, item in enumerate(array):
                        # if index == 1 or index == 0:
                        #     continue
                        try:
                            if not item == '':    
                                y[index] += int(item)
                        except:
                            y.append(int(item))
                    for index, item in enumerate(array):
                        
                        try:
                            if not item == '':    
                                y[index] += int(item)
                        except:
                            y.append(int(item))
        print(len(y))
        print(len(x[2:]))
        plt.bar(x[2:], y, color = 'g', width = 0.8, label = f"Expense distribution(year={year}, month={month}")
        plt.xlabel('categories')
        plt.ylabel('expenditure')
        plt.title('Expense distribution')
        plt.legend()
        plt.show()

    except:
        return False
