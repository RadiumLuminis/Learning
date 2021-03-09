import PySimpleGUI as sg

sg.theme(new_theme = "Dark Amber")

layout = [[sg.Text("Your Text will appear here: "), sg.Text(size= (15, 1), key="-OUTPUT-")],
          [sg.Input(key="-IN-")],
          [sg.B("Show"), sg.B("Exit")]]

window = sg.Window("Pattern2", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Show":
        window["-OUTPUT-"].update(values["-IN-"])