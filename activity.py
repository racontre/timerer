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
import logger

class Activity:
    '''This script manages activities' information such as save data and descriptions'''
    scriptpath = os.path.dirname(os.path.realpath(__file__))
    save_path = scriptpath + '\\user_activity.sav'
    
    def note_management(self):
        '''
        This method is to detect if the user already has save data.
        If it doesn't exist, initialise
        '''
        if os.path.isfile(Activity.save_path):
            Activity.load(self, Activity.save_path, self.activityList)
        else:
            if os.path.isfile(Activity.save_path + '.bak'):          
                Activity.load(self, Activity.save_path + '.bak', self.activityList)
            else:
                Activity.write_json(Activity.save_path, contents.activityDefaultDict)

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
        save_dict = Activity.get_json(Activity.save_path)
        save_dict[contents.activityChosen] =   { 'description' : contents.activityDescription,
                                                'recorder' : contents.activityTimer,
                                                'history' : {},
                                               'isDeleted' : False
                                                }
#should be checking if theres any new ones. Otherwise it wont save

        Activity.write_json(Activity.save_path, save_dict)
        #with open(self.scriptpath +'\\user_activity.sav.tmp', 'w') as the_file:
        #    json_object = json.dumps(save_dict, indent = 4)
        #    print(save_dict)
        #    the_file.write(json_object)
        
    
    @staticmethod
    @logger.log
    def get_json(file_path):
        '''Receives the json save data from a file'''
        try:
            with open(file_path, 'r') as the_file:
                json_dict = json.loads(the_file.read())
        except FileNotFoundError:
            '''user_activity.sav was not found. Trying to restore backup...'''
            try:
                with open(file_path + '.bak', 'r') as the_file:
                    json_dict = json.loads(the_file.read())
            except FileNotFoundError:
                '''Failed to restore save'''
                json_dict = contents.activityDefaultDict
        return json_dict
    
    
    @staticmethod
    @logger.log
    def write_json(file_path, input_dictionary):
        '''Converts dictionary to json and writes to a file'''
        with open(file_path + '.tmp', 'w+') as the_file:
            json_object = json.dumps(input_dictionary, indent = 4)
            the_file.write(json_object)
        try:
            os.replace(Activity.save_path, Activity.scriptpath +'\\user_activity.sav.bak')
        except FileNotFoundError:
            '''For some reason I do not understand, the .sav just isn't there
            Perhaps we loaded a backup'''
            pass
        os.replace(file_path + '.tmp', Activity.save_path)

    def load(self, file_path, activity_container):
        '''
        Method goes through each key in the dict
        and adds valid keys to the container
        '''
        save_dict = Activity.get_json(file_path)
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
        contents.activityDescription = data
        text_container.config(state=tk.NORMAL)
        text_container.delete(1.0, tk.END)  # if you want to remove the old data
        text_container.insert(tk.END,contents.activityDescription)
        text_container.config(state=tk.DISABLED)
