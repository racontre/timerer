'''
Created on 17 feb 2020 y.

@author: RX-79
todo: rename all to snake style
'''

introSeen = False

introStr = """ Urgent: create file on activity creation! Hello! This program is designed to help you keep track of your activities!
    Create your own activity in the field to the left!
    Things to do:
    1) Link creation
    2) A more elaborate save system a) remember chosen activities 
    3) Calendar"""

TitleNom = "Timerer!"
placeholderNom = "placeholdere"
activityNom = "Activity: "
activityAddNom = "Add New Activity: "
activity_add_warning = "Do not use the following characters: <>`[]{}"
activity_add_warning_title = "Illegal String"
activityListNom = "Activity List"
activitySummaryTodayNom = "Activitied for today: "
activitySummaryCounter = "<none>"

activityChoiceBtn = "Choose"
activityDescription = "Enter your description..."
activityDeleteBtn = "Del"
activityGraphBtn = "Graph"
activityAddBtn = "+"

activityDefaultDict =  { 'Test Activity':{ 'description' : 'This is a test Activity!',
                        'recorder' : '0:1:34',
                        'history' : {},
                        'isDeleted' : False
                        }
                        }

activityChosen = "<none>" #should be reset if activity is deleted
activityIsDeleted = False
activityListNoteEntry = "waadwdadwawadawawafaefasfsdfdsfdsoijcxjvpxckvpssjgopiewhofehwfoewhoegfihhUUU"
activityTimer = "<none>"

activityEditBtn = "Edit"
activitySaveBtn = "Save"

bgColor = "#cfe0fa"

calendarNom = "Calendar"

fileHasEnded = False

timerNom = "Timer"
timerActive = False
timerPauseBtn = "Stop"
timerRestartBtn = "Restart"
timerCounterNom = "0 : 0 : 0"
timerSavePrompt = "Save the time for today?"

illegalStr = ['','   ','\n']
illegalChar = '<>/{}[\]~`'