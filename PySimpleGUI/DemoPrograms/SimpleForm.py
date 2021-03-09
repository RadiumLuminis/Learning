import PySimpleGUI as sg

layout = [[sg.Text("Please enter your credentials:")],
          [sg.Text("Name", (10, 1)), sg.InputText(key="-NAME-")],
          [sg.Text("Adresse", (10, 1)), sg.InputText(key="-ADRESSE-")],
          [sg.Text("Telefon", (10, 1)), sg.InputText(key="-TELEFON-")],
          [sg.B("Fertig")], [sg.B("Abbrechen")]]


window = sg.Window("Einfache Dateneingabe", layout)
event, values = window.read(close=True)

if event == "Fertig":
    print("The event was", event, "You Input", values["-NAME-"], values["-ADRESSE-"], values["-TELEFON-"])
else:
    print("User Cancelled")