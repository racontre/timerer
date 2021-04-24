'''
Created on 17 feb. 2020 y.

@author: RX-79
'''
import tkinter as tk
from user_interface_handler import user_interface_handler
import logger

window = tk.Tk()
logger.logging.debug('test')
user_interface = user_interface_handler(window)
window.mainloop()

