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
            for check in check_vars:
                if check_vars[check].get():
                    print(check)
                    records.append(record.get_records(check))
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
        """ i cant do stacked bars
        sorry......"""
        stack = {'date': [],
                 'duration': []}
        fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
        ax.set(title="Activity Graph")
        for data in checked_data:
            bottom_list = []
            prev_y_data = 0
            print(data['date'])
            print(data['duration'])

            for y_data in data['date']:
                match = False
                #will create entry in bottom list for each
                for j, x_data in enumerate(stack['date']): 
                    
                    if (y_data == x_data):
                        match = True
                        #print('same date found: ', stack['duration'][j], ' at date: ', stack['date'][j])
                        bottom_list.append(stack['duration'][j] + 0.02)
                #print(y_data)
                if ((prev_y_data is not y_data) and not match and stack['date']):          
                    if (prev_y_data == y_data): 
                        #print ("we add 0 here:  prev_y_data: ", prev_y_data,  " y_data: ", y_data) 
                        bottom_list.append(0)
                prev_y_data = y_data
            #print(bottom_list, ' ', data['duration'])
            
            
            if (not bottom_list):
                ax.bar(list(data['date']), list(data['duration']), bottom=0)  
            else:
                ax.bar(list(data['date']), list(data['duration']), bottom=bottom_list)  
            #stack['duration'] = stack['duration'] + data['duration']
            #stack['date'] =  stack['date'] + data['date']
            #Uncomment the above at your own risk for mental stability
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
        
        line2 = FigureCanvasTkAgg(fig, self.window)
        line2.get_tk_widget().grid(column = 0, row=15, sticky=tk.E, pady=4, padx = 6)
        

       
    
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