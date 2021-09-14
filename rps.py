'''
Matt Myers
09/14/2021
GUI Rock Paper Scissors
test testing 123
'''
# Libraries
import PySimpleGUI as sg
from rps_func import results
import random

#Functions

#GUI
sg.theme('Dark Teal 2')

# *Window.Contents
layout = [[sg.Text("\nRock, Paper, or Scissors?\n\nChoose Wisely!\n")],
          [sg.Button('Rock'), sg.Button('Paper'), sg.Button('Scissors')],
          [sg.Output(size=(30,4), key='-o-')],
          [sg.Text(size=(30,2), key='wins', justification='r')],
          [sg.Button('Quit')]]

# *Window.Create
window = sg.Window('Rock_Paper_Scissors', layout, size=(225,275))

# *Window.Display
while True:
    event, values = window.read()
    comp = random.choice(['Rock','Paper','Scissors'])
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    result,uwin,cwin = results(event,comp)
    
    window['-o-'].update('You choose: ' + event +
                              '\nComputer choose: ' + comp +
                              '\n\n' + result) 
    window['wins'].update('Player: '+ comp + '\nComputer: ' + event)

# *Window.Close
window.close()

#Backend



