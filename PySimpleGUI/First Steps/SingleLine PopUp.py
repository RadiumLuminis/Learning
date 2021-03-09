import PySimpleGUI as sg

# STEP 1 - create the window, read the window, close the window.
event, values = sg.Window('My single-line GUI!',
                    [[sg.Text('My one-shot window.')],      
                     [sg.InputText(key='-IN-')],      
                     [sg.Submit(), sg.Cancel()]]).read(close=True)  

# finally show the input value in a popup window
sg.popup('You entered', values['-IN-'])
