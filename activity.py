'''
Created in march. 2021 y.

@author: RX-79
'''
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk
import json
import os
import contents


class Activity:
    '''This script manages activities' information such as save data and descriptions'''
    scriptpath = os.path.dirname(os.path.realpath(__file__))

    def note_management(self):
        '''
        This method is to detect if the user already has save data.
        If it doesn't exist, initialise
        '''
        if os.path.isfile(Activity.scriptpath + '\\user_activity.sav'):
            print ("File exist") #load
        else:
            #init save file
            with open(Activity.scriptpath + '\\user_activity.sav', 'w+') as the_file:
                dictionary = {
                    'Test Activity': {
                        'description': 'This is a test Activity!',
                        'timer': '0:1:34'
                    }
                }
                json_object = json.dumps(dictionary, indent = 4)
                the_file.write(json_object)

    def edit_description(self, text_container):
        '''Method allows to edit the text container'''
        text_container.config(state=tk.NORMAL)

    def save(self, text_container):
        '''
        Method saves data to a file for future use. There's a backup &
        a temp file for safe saving.
        '''
        #self.noteTxt.config(state = tk.DISABLED)
        contents.ActivityDescription = text_container.get("1.0",tk.END)
        with open(Activity.scriptpath +'\\user_activity.sav', 'r') as the_file:
            save_dict = json.loads(the_file.read())
            save_dict[contents.activityChosen] =   { 'description' : contents.activityDescription,
                                                'timer' : contents.activityTimer,
                                                'history' : {},
                                               'isDeleted' : False
                                                }
#should be checking if theres any new ones. Otherwise it wont save
        with open(Activity.scriptpath +'\\user_activity.sav.tmp', 'w') as the_file:
            json_object = json.dumps(save_dict, indent = 4)
            print(save_dict)
            the_file.write(json_object)
        os.replace(Activity.scriptpath +'\\user_activity.sav', Activity.scriptpath
                   +'\\user_activity.sav.bak')
        os.replace(Activity.scriptpath +'\\user_activity.sav.tmp', Activity.scriptpath
                   +'\\user_activity.sav')


    def load(self, activity_container):
        '''
        Method goes through each key in the dict
        and adds valid keys to the container
        '''
        with open(Activity.scriptpath +'\\user_activity.sav', 'r') as the_file:
            save_dict = json.loads(the_file.read())
            for key in save_dict:
                try:
                    if not save_dict[key]['isDeleted']:
                        print(key)
                        activity_container.insert(tk.END, key)
                except KeyError:
                    print(key, ' causes the KeyError exception. Its isDeleted ', save_dict[key])

    def cancel_edit(self, text_container):
        '''
        Meant to be called whenever we want to roll back
        our edit to a previous version
        (for example when you do not wish to save)
        '''
        text_container.config(state = tk.DISABLED)
        path = Activity.scriptpath + "\\data\\" + contents.activityChosen + "Note"
        try:
            file = open(path, 'r')
            cancel = file.read()
        except IOError:
            cancel = ''
            text_container.delete(1.0, tk.END)
            Activity.replace_text(self, cancel, text_container)
        #self.noteTxt.config(text = cancel)

    def replace_text(self, text, text_container):
        '''
        Meant to be called whenever we need to reset
        text_container value
        (for example when you do not wish to save)
        '''
        text_container.delete(1.0, tk.END)
        text_container.insert(1.0, text)

    def update_description(self, text_container):
        '''
        Called whenever you change the selected activity.
        The activity description will change based on your selection
        '''
        try:
            file = open(os.path.dirname(os.path.realpath(__file__)) + "\\data\\"
                        + contents.activityChosen + "Note","r")
            data = file.read()
        except FileNotFoundError:
            data = ''
        print(data)
        contents.activityDescription = data
        text_container.config(state=tk.NORMAL)
        text_container.delete(1.0, tk.END)  # if you want to remove the old data
        text_container.insert(tk.END,contents.activityDescription)
        text_container.config(state=tk.DISABLED)
