'''
.

@author: RX-79
'''
from activity import Activity
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import tkinter.ttk as ttk
import contents
from datetime import datetime as dt
try:
    import tkinter.messagebox as mbox
except ImportError:
    import TkMessageBox as mbox
import os
import json  
from graph_window import graph_window

class user_interface_handler:

    frame_height = 600
    frame_width = 800
    
    def __init__(self, window):
            #Reference to the window in main
        self.window = window
        
            #OPTIONS&VARS
        window.title("Activity Timer!")
        self.main_bg= contents.bgColor
        self.opt_bgcolor = "red"
        self.style = ttk.Style()     # Create style
        self.style.configure("Blue.TFrame", background="blue") # Set bg color      
        self.canvas_height = 900
        self.canvas_width = 950
        self.timer = 0
              
            # CONTAINER FOR ALL THE FRAMES
        #self.content = ttk.Frame(self.window, padding=(3,3,12,12))
        #self.content.grid()
              
            # THE FRAMES
        self.ui_frame = tk.Frame(self.window, 
                                 borderwidth=10)    #basic
        self.ui_frame.configure(background=self.main_bg)
        self.ui_frame.grid()                          #to be shown at start    
        self.render_ui_frames()
        self.noteTxt.delete("1.0", "end")  


    def render_ui_frames(self):
        # Render all UI frames, set up dimensions and positions

        self.c_scrollbar = tk.Scrollbar(self.window)
        
        self.activityAnnounce = tk.Label(self.ui_frame, text = contents.activityNom + contents.activityChosen, bg = contents.bgColor)
        self.activityAnnounce.grid(column = 1, row = 1,  sticky=tk.W, pady=10, padx=10)
        
        self.timerRunner = tk.Button(self.ui_frame, text = contents.timerNom, command =  lambda: user_interface_handler.record_manage(self))
        self.timerRunner.grid(column = 1, row = 2,  sticky=tk.W, pady=2, padx=10)
        
        self.activitySummary = tk.Label(self.ui_frame, text = contents.activitySummaryTodayNom + contents.activitySummaryCounter, bg = contents.bgColor)
        self.activitySummary.grid(column = 9, row = 3,  sticky=tk.W, pady=2, padx=10)
        
        self.timerAnnounce = tk.Label(self.ui_frame, text = contents.timerCounterNom,  bg = contents.bgColor)
        self.timerAnnounce.grid(column = 1, row = 3, pady=2, padx=10, sticky=tk.W)
        
        additionAnnounce = tk.Label(self.ui_frame, text = contents.activityAddNom,  bg = contents.bgColor)
        additionAnnounce.grid (column = 1, row = 7,  sticky=tk.W, pady=5, padx=10)
        
        entryStr = tk.StringVar()
        user_interface_handler.entry_limit(self, entryStr, 20)
        
        self.additionEntry = tk.Entry(self.ui_frame, width=18,  textvariable=entryStr)
        self.additionEntry.grid(column = 1, row = 8,columnspan = 3, sticky=tk.W,  padx=10)

        choiceButton = tk.Button (self.ui_frame, text = contents.activityChoiceBtn, command = lambda: user_interface_handler.choose_item(self))
        choiceButton.grid(column = 6, row = 8, sticky=tk.E, pady=10, padx=10)
        
        deletionButton = tk.Button(self.ui_frame, text = contents.activityDeleteBtn, command = lambda: user_interface_handler.rem_item(self)) ##
        deletionButton.grid(column = 8, row = 8, sticky=tk.E, pady=10, padx=10)
        
        editButton = tk.Button (self.ui_frame, text = contents.activityEditBtn, command = lambda: Activity.edit_description(self, self.noteTxt)) #add command
        editButton.grid (column = 9, row = 8, sticky=tk.W, pady=10, padx=10)
        
        saveButton = tk.Button (self.ui_frame, text = contents.activitySaveBtn, command = lambda: Activity.save(self, self.noteTxt))
        saveButton.grid (column = 10, row = 8, sticky = tk.W, pady = 10, padx = 10)
        
        graphButton = tk.Button (self.ui_frame, text = contents.activityGraphBtn, command = lambda: user_interface_handler.create_graph(self))
        graphButton.grid (column = 10, row = 1, sticky = tk.W, pady = 10, padx = 10)
        
        noteScrollbar = tk.Scrollbar()
        noteScrollbar.grid(column=6, row=0)
        
        self.noteTxt = tk.Text(self.ui_frame, wrap=tk.WORD, width=25, height=5, bg = contents.bgColor)
        self.noteTxt.config(yscrollcommand=noteScrollbar.set)
        noteScrollbar.config(command=self.noteTxt.yview)
        self.noteTxt.grid(column = 9, row = 4, columnspan = 4, rowspan = 4, sticky=tk.E, padx=10)
        self.noteTxt.insert(tk.END, contents.introStr)
        self.noteTxt.config(state=tk.DISABLED)
        
        self.activityList = tk.Listbox(self.ui_frame)#
        self.activityList.grid(column = 5, row = 1, columnspan = 4, rowspan = 7, sticky=tk.E, pady=10, padx=10)
        self.activityList.bind('<Double-1>', lambda x: user_interface_handler.choose_item(self))
        Activity.note_management(self)
        Activity.load(self, self.activityList)
        self.activityList.config(width=20)

        additionButton = tk.Button(self.ui_frame, text = contents.activityAddBtn, command = lambda: user_interface_handler.add_item(self, self.additionEntry.get()))
        additionButton.grid(column = 4, row = 8, sticky=tk.W, pady=10, padx=10)
        #user_interface.text_interaction(self)
        #self.introduction()
    
    def introduction(self):
        l1 = ttk.Label(self.intro_frame, text="within self.ui_frame")
        l1.grid(column=1,row=1)
        lbl = tk.Label(self.intro_frame, text=contents.introStr, bg='#689db3', font=("Arial Bold", 14))
        lbl.grid(column=4, row=10)

########################################################################################  List things  
    def add_item(self, item_name):
        list2files = self.activityList.get(0, tk.END)
        if self.additionEntry.get() not in list2files:
            if not all('' == s or s.isspace() for s in self.additionEntry.get()):
                self.activityList.insert(tk.END, item_name)
                with open(Activity.scriptpath +'\\user_activity.sav', 'r') as the_file:
                    save_dict = json.loads(the_file.read()) #try-excepts
                    save_dict[item_name] = {'description' : 'Add a description',
                                                'timer' : '',
                                                'history' : {},
                                               'isDeleted' : False}
                with open(Activity.scriptpath +'\\user_activity.sav', 'w') as the_file:
                    json_object = json.dumps(save_dict, indent = 4)
                    print(save_dict)
                    the_file.write(json_object)
        #try add file
        #manage creating a file for new activity! fields such as: days designated, amount of time, etc
        
    def choose_item(self):
        contents.activityChosen = self.activityList.get(self.activityList.curselection())  
        user_interface_handler.load_sections_time(self)
        self.activityAnnounce.config(text = contents.activityNom + contents.activityChosen)
        Activity.cancel_edit(self, self.noteTxt)
        Activity.update_description(self, self.noteTxt)

    def rem_item(self):    
        selected = list(self.activityList.curselection())
   
        for select in selected:
            with open(Activity.scriptpath +'\\user_activity.sav', 'r') as the_file:
                save_dict = json.loads(the_file.read()) #try-excepts
                save_dict[self.activityList.get(self.activityList.curselection())]['isDeleted'] = True
            with open(Activity.scriptpath +'\\user_activity.sav', 'w') as the_file:
                json_object = json.dumps(save_dict, indent = 4)
                print(save_dict)
                the_file.write(json_object)
            if contents.activityChosen in self.activityList.get(0, tk.END):       #seems to work now 
                if mbox.askyesno("Delete", "Delete the activity?"):                                     #but maybe i should show the prompt regardless
                    self.activityList.delete(select) 
                    contents.activityChosen = ''  
                    self.activityAnnounce.config(text = contents.activityNom + contents.activityChosen)
            else:
                self.activityList.delete(select)   
            
        #check for illegal arguments?
        
    def entry_limit(self, str_var,length):  #so that an activity's name isnt too long 
        def callback_str(str_var):          #(dont know how else to deal with it)
            c = str_var.get()[0:length]     #besides this solves most other problems so whatever
            str_var.set(c)
        str_var.trace("w", lambda name, index, mode, str_var=str_var: callback_str(str_var)) #no idea
###################################################################################

####################################################################################  Timer things           

    def record_manage(self):
        if (contents.timerActive):
            contents.timerActive = False
            self.timerRunner.config(text = contents.timerNom)
            if self.handleTimer:
                self.window.after_cancel(self.handleTimer)
                self.handleTimer = None
                if contents.activityChosen in self.activityList.get(0, tk.END):
                    user_interface_handler.timer_save(self)
                    user_interface_handler.load_sections_time(self)
        else:   
            self.start = dt.now() #is this ok?
            contents.timerActive = True
            self.timerRunner.config(text = contents.timerPauseBtn)
            
            user_interface_handler.update_clock(self)
        # now make a choice to PAUSE or to RESTART! and save result

    def update_clock(self):                                 ##i messed up really hard here wtf
        self.timerOutput = dt.now() - self.start            ##should probably rewrite sometime
        self.secOutput = int (self.timerOutput.total_seconds()) 
        self.hoursOutput = (self.secOutput // 3600)
        self.minutesOutput = (self.secOutput % 3600) //60
        self.secOutput = self.secOutput - self.hoursOutput*3600 - self.minutesOutput * 60
        #print(self.hoursOutput, ':', self.minutesOutput, ':', self.secOutput)
        self.timerAnnounce.config(text = ( self.hoursOutput,':',  self.minutesOutput,':', self.secOutput))
        self.handleTimer = self.window.after(1000, self.update_clock)
        
    def timer_save(self):               #make into a prompt 
        if mbox.askyesno("Save", "Save the timer?"):
            date_time_str = dt.now()
            date_time_ymd = dt.strptime(str(date_time_str), '%Y-%m-%d %H:%M:%S.%f')
            date_time_ymd = date_time_ymd.strftime('%d/%m/%Y %H:%M:%S')
            path = os.path.dirname(os.path.realpath(__file__)) + "\\data\\" + contents.activityChosen
            file = open(path,"a")
            file.write(date_time_ymd + ',' + contents.activityChosen + ',' + ( str(self.hoursOutput) + ':' +  str(self.minutesOutput) + ':' + str(self.secOutput))+'\n')
        
            #works now save it but lags a bit
    def load_sections_time(self):   #i worked hard on this so you could witness the worst code ever
        if contents.activityChosen in self.activityList.get(0, tk.END):
            try: 
                with open(os.path.dirname(os.path.realpath(__file__))+"\\data\\" + contents.activityChosen , 'r') as infile:
                    totalTime = 0
                    for line in infile:
                        #line = infile.readline()
                        line = line.rstrip().split(',')
                        lineTime = line[2].split(':')
                        lineDate = line[0].split(' ')[0]
                        timeforLine = int(lineTime[2]) + int(lineTime[1]) * 60 + int(lineTime[0]) * 3600
                        if dt.now().strftime('%d/%m/%Y') == lineDate:
                            totalTime = totalTime + timeforLine
                        totalTimeHours = totalTime // 3600                          #need to code a separate 
                        totalTimeMinutes = (totalTime - totalTimeHours * 3600) // 60#function for conversion
                        totalTimeSeconds = totalTime - totalTimeHours * 3600 - totalTimeMinutes * 60
                    #print(totalTimeHours, ':', totalTimeMinutes, ':', totalTimeSeconds)
                    self.activitySummary.config(text = contents.activitySummaryTodayNom + str(totalTimeHours) + ' : ' + str(totalTimeMinutes) + ' : ' + str(totalTimeSeconds))
                    contents.activityTimer = str(totalTimeHours) + ' : ' + str(totalTimeMinutes) + ' : ' + str(totalTimeSeconds)
                    #dont forget to check the date tho
            except FileNotFoundError:
                contents.activityTimer = "no file"
                self.activitySummary.config(text = contents.activitySummaryTodayNom + "no file")
    

    def create_graph(self):
        list2files = self.activityList.get(0, tk.END)
        graph_instance = graph_window(self.window, list2files)
########################################################################################

########################################################################################  Note things       
