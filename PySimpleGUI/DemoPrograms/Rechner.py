import PySimpleGUI as sg
import string

sg.theme("LightGrey")

#Wiederverwendete Layouteinstellungen
bt1 = {"size":(7,2), "font":("ImprintMTShadow", 24), "button_color":("#c5eafa")}
bt2 = {"size":(7,2), "font":("ImprintMTShadow", 24), "button_color":("#4dc9ff")}
bt3 = {"size":(15,2), "font":("ImprintMTShadow", 24), "button_color":("#101b75")}

layout = [[sg.Text("0", size=(13, 1), justification="right", background_color="#c5eafa",font=("ImprintMTShadow", 59), key="-DISPLAY-")],
          [sg.B("C", **bt2), sg.B("CE", **bt2),sg.B("%", **bt2), sg.B("/", **bt2)],
          [sg.B("7", **bt1), sg.B("8", **bt1), sg.B("9", **bt1), sg.B("*", **bt2)],
          [sg.B("4", **bt1), sg.B("5", **bt1), sg.B("6", **bt1), sg.B("-", **bt2)],
          [sg.B("1", **bt1), sg.B("2", **bt1), sg.B("3", **bt1), sg.B("+", **bt2)],
          [sg.B("0", **bt1), sg.B(".", **bt1), sg.Button('=',**bt3, bind_return_key=True, focus=True)],
          ]

window = sg.Window("Rechner", layout, element_padding=(7,7))

floatnum = False
front = []
back = []
result = 0
operator = ""
zw = 0

def formatieren():
    global front, back
    if len(back) > 5:
        back = back[:5]
    if len(front) == 0 and len(back) == 0:
        return "0"
    elif floatnum:
        if len(front) != 0:
            return ("".join(front) + "." + "".join(back))
        else:
            return("0." + "".join(back))
    else:
        if float("".join(front) + "." + "".join(back)).is_integer() == False:
            return ("".join(front) + "." + "".join(back))
        else:
            return str("".join(front))
def update(txt):
    window["-DISPLAY-"].update(txt)

def numberclick(event):
    if floatnum == True:
        back.append(event)
    else:
        if event == "0" and len(front) == 0:
            pass
        else:
            front.append(event)
    update(formatieren())

def clearclick():
    global floatnum
    global front, back
    front = []
    back = []
    floatnum = False

def operatorclick(event):
    global zw
    global operator

    update(formatieren())

    if zw != 0:
        if operator == "+":
            zw += float(formatieren())
        if operator == "-":
            zw -= float(formatieren())
        if operator == "*":
            zw *= float(formatieren())
        if operator == "/":
            if float(formatieren()) != 0:
                zw = zw / float(formatieren())
            else:
                update("ERROR! DIV/0")

    else:
        zw = float(formatieren())

    if (zw).is_integer():
        front = int(zw)
        front = list(str(front))
    else:
        front, back = str(zw).split(".")
        floatnum = True

    print(zw)
    operator = event
    clearclick()

def calculate():
    global zw
    global operator
    global front, back, floatnum
    if operator == "+":
            zw += float(formatieren())
    if operator == "-":
        zw -= float(formatieren())
    if operator == "*":
        zw *= float(formatieren())
    if operator == "/":
        if float(formatieren()) != 0:
            zw = zw / float(formatieren()) 
        else:
            update("ERROR! DIV/0")

    clearclick()
    operator = ""

    if (zw).is_integer():
        front = int(zw)
        front = list(str(front))
    else:
        front, back = str(zw).split(".")
        floatnum = True
    update(formatieren())
    

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event in string.digits:
        if operator == "" and zw != 0:
            pass
        else:
            numberclick(event)
    if event in ["+", "-", "*", "/"]:
        operatorclick(event)
    if event == "=":
        if operator == "":
            pass
        else:
            calculate()
    if event == "%":
        if (float(formatieren())/100).is_integer():
            print(float(formatieren())/100)
            front = list(str(int(float(formatieren())/100)))
        else:
            front, back = (str(float(formatieren())/100)).split(".")
            front = list(front)
            back = list(back)
            floatnum = True
        update(formatieren())
    if event == ".":
        floatnum = True
        update(formatieren())
    if event == "C" or event == "CE":
        clearclick()
        zw = 0
        operator = ""
        update(0)
    


