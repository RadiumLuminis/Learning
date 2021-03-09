import PySimpleGUI as sg

def second_Window():

    layout = [[sg.Text("Ein Fenster aus einem anderen heraus öffnen geht")], 
              [sg.OK()]]

    window = sg.Window("Zweites Fenster", layout)
    event, values = window.read(close=True)
    
def Test_Menu():

    sg.theme("Light Green")
    sg.set_options(element_padding=(1, 1))

    menu_def = [["&Datei", ["&Öffnen", "&Speichern", "&Einstellungen", "S&chließen"]],
                ["&Bearbeiten", ["&Einfügen", ["Spezial", "Normal",], "Rückgängig"],],
                ["&Symbolleiste", ["---", "Befehl &1", "Befehl &2", "---", "Befehl &3", "Befehl &4"]],
                ["&Hilfe", "&ÜberDasProgramm"],]

    right_click_menu = ["Unbenutzt", ["Rechts", "!&Klick", "&Menu", "S&chließen", "&Einstellungen"]]

    layout = [
              [sg.Menu(menu_def, tearoff=False, pad=(20,1))],
              [sg.Text('Click right on me to see right click menu')],
              [sg.Output(size=(60,20))],
              [sg.ButtonMenu('ButtonMenu',key='-BMENU-', menu_def=menu_def[0])],
              ]


    window = sg.Window("Windows-ähnliches Programm",
                       layout,
                       default_element_size=(12, 1),
                       default_button_element_size=(12, 1),
                       right_click_menu=right_click_menu,
                       grab_anywhere=True)

    while True:
        event, values = window.read()
        if event is None or event == "Exit":
            return

        if event == "ÜberDasProgramm":
            window.disappear()
            sg.popup("Über dieses Programm", "Version 1.0", "PySimpleGUI rockt!", grab_anywhere=True)
            window.reappear()
        elif event == "Öffnen":
            filename = sg.popup_get_file("Datei zum öffnen", no_window=True)
            print(filename)
        elif event == "Einstellungen":
            second_Window()
        elif event == "-BMENU-":
            print("Du hast aus dem Schaltflächenmenue", values["-BMENU-"], "ausgewählt")

Test_Menu()