'''
Created on 3 apr. 2021.

@author: RX-79
'''
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import contents
import recorder
#import matplotlib.pyplot  as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class graph_window(object):
    '''
    classdocs
    '''
    
    test_data =  {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
         'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
        }  
    
    def __init__(self, master_window, activity_list):
        
        record = recorder.Record()
        def check_states():
            for check in check_vars:
                if check_vars[check].get():
                    print(check)
                    record.get_records(check)
                    graph_window.build_graph(self)
        
        self.window = tk.Toplevel(master_window)
        self.window.title("Graph")
        self.main_bg= contents.bgColor
        self.style = ttk.Style()     # Create style     
        self.canvas_height = 300
        self.canvas_width = 350
        
        self.ui_frame = tk.Frame(self.window, 
                                 borderwidth=10)
        self.window.geometry('{}x{}'.format(self.canvas_height, self.canvas_width))
        self.window.configure(background=self.main_bg)
        tk.Label(self.window, text="Your sex:").grid(row=0, sticky=tk.W)
        check_vars = {}
        for index, activity in enumerate(activity_list):
            check_vars[activity] = tk.IntVar()
            tk.Checkbutton(self.window, text=activity, variable=check_vars[activity],
                             bg = contents.bgColor).grid(row=index, sticky=tk.W)
        
        tk.Button(self.window, text='Show', command=check_states).grid(column = 2, row=4, sticky=tk.E, pady=4, padx = 6)
        self.ui_frame.grid()                          #to be shown at start
        

    
    def build_graph(self):
        figure2 = plt.Figure(figsize=(5,4), dpi=50)
        ax2 = figure2.add_subplot(111).bar(list(graph_window.test_data['Year']), 
                 list(graph_window.test_data['Unemployment_Rate']))
        #ax2.set_title('Year Vs. Unemployment Rate')
        line2 = FigureCanvasTkAgg(figure2, self.window)
        line2.get_tk_widget().grid(column = 0, row=15, sticky=tk.E, pady=4, padx = 6)
        #df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
        print(list(graph_window.test_data['Year']))
        plt.plot(list(graph_window.test_data['Year']), 
                 list(graph_window.test_data['Unemployment_Rate']))
        plt.grid(True)