'''
Created on 3 apr. 2021.

@author: RX-79
'''
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
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
            records=  []
            names = []
            for check in check_vars:
                if check_vars[check].get():
                    print(check)
                    records.append(record.get_records(check))
                    names.append()
            graph_window.build_graph(self, records)
        
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
        

    
    def build_graph(self, checked_data):
        #data things are in datetime.datetime format
        #check if graph already exists
        # Create figure and plot a stem plot with the date
        fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
        ax.set(title="Activity Graph")
        for  data in checked_data:
            ax.bar(list(data['date']), list(data['duration']), bottom=0)  # Baseline and markers on it.
        
        #plt.legend(['NA', 'EU', 'JP', 'Others'], loc='upper left', ncol = 4)
        #ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
        
        #figure2 = plt.Figure(figsize=(6,4), dpi=100)
        #figure1 = plt.Figure(figsize=(6,4), dpi=50)
        #ax2 = figure2.add_subplot().bar(list(data['date']), 
        #     list(data['duration']))
        #ax2.set_label("reatrd")
        #figure2.set_label("nigga")
        #fig, ax = plt.subplots()
        #ax.plot_date(list(data['date']), 
        #         list(data['duration']), fmt = 'd')
        #fig.add_subplot(ax)
        #fig.add_axes([-0.5,0.5,0,1])
        #print(plt.axes())
        #figure2.autofmt_xdate() #https://matplotlib.org/3.3.4/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure.align_xlabels
        
        #ax.set_label("retard")
        #figure2.add_axes([0,0,1,1])
        #print(figure2.gca())
        line2 = FigureCanvasTkAgg(fig, self.window)
        line2.get_tk_widget().grid(column = 0, row=15, sticky=tk.E, pady=4, padx = 6)
        #df2 = df2[['Year','Unemployment_Rate']].groupby('Year').sum()
        

       
    
    def build_canvas(self):
        w = tk.Canvas(self.window, width=200, height=100)
        canvas_height = 100
        bar_width = 15
        scale = 4
        for x,y in enumerate(list(graph_window.test_data['Unemployment_Rate'])):  
            x1 = x + x * bar_width     
            y1 = canvas_height - y*scale     
            x2 = x + x * bar_width + bar_width    
            y2 = canvas_height    
            w.create_rectangle(x1, y1, x2, y2, fill="blue")    
            w.create_text(x1+3, y1, font=("", 6),        text=str(y),anchor='sw' )
        w.grid(column = 0, row=15, sticky=tk.E, pady=4, padx = 6)