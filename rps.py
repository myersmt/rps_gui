'''
Matt Myers
09/14/2021
GUI Rock Paper Scissors
The rock paper scissors game is an age old tradition
on who gets to do something first.
'''
# Libraries
import PySimpleGUI as sg
from rps_func import results
import random

#GUI
sg.theme('Dark Teal 2')

# Setup
uwin=cwin=0

# *Window.Contents
font_header=('helvetica', 12, 'bold',)
font_sub=('helvetica',8)
layout = [[sg.Text("\nRock, Paper, or Scissors?",font=font_header)],
          [sg.Text("Choose Wisely!\n",font=font_sub)],
          [sg.Button('Rock'), sg.Button('Paper'), sg.Button('Scissors')],
          [sg.Output(size=(30,4), key='-o-')],
          [sg.Text('Player: {}\nComputer: {}'.format(uwin,cwin),size=(30,2), key='wins', justification='r')],
          [sg.Button('Quit')]]

# *Window.Create
window = sg.Window('Rock_Paper_Scissors', layout, size=(230,300),
                   element_justification='c', no_titlebar=True,
                   grab_anywhere=True)

# *Window.Display
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    comp = random.choice(['Rock','Paper','Scissors'])
    result_info = results(event,comp)
    result = result_info[0]
    uwin += result_info[1]
    cwin += result_info[2]
    
    
    window['-o-'].update('You choose: ' + event +'\nComputer choose: ' + comp + '\n\n' + result) 
    window['wins'].update('Player: {}\nComputer: {}'.format(uwin,cwin))
    

# *Window.Close
window.close()




