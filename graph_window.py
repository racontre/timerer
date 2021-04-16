'''
Created on 3 apr. 2021.

@author: RX-79
'''
import tkinter as tk
import tkinter.ttk as ttk
import contents
#import matplotlib.pyplot  as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class graph_window(object):
    '''
    classdocs
    '''

    def __init__(self, master_window, activity_list):
        def check_states():
            for state in check_vars.values():
                print(state.get())
        
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
        
        tk.Button(self.window, text='Show', command=check_states).grid(row=4, sticky=tk.W, pady=4)
        self.ui_frame.grid()                          #to be shown at start
        

    '''     
    def build_graph(self):
        figure = plt.Figure(figsize=(6,5), dpi=100)
        ax = figure.add_subplot(111)
        chart_type = FigureCanvasTkAgg(figure, self.window)
        chart_type.get_tk_widget().pack()
        df = df[['First Column','Second Column']].groupby('First Column').sum()
        df.plot(kind='Chart Type such as bar', legend=True, ax=ax)
        .set_title('The Title for your chart')'''