import PySimpleGUI as sg
from count_syllables import countSyllables

# sg.Window(title = "Hello World", layout=[[]], margins = (100,50)).read()
sg.theme("DarkTeal1")
layout = [[sg.Text("Please enter your word below:")],
          [sg.Input(key='word')],
          [sg.Button("GO!",bind_return_key=True),sg.Button("Exit")],
          [sg.Text("",key='result'), sg.Text("",key='syllable')]
          ]
width, height = sg.Window.get_screen_size()

window = sg.Window("Syllable Checker", layout, resizable=True)
# window.Maximize()


while True:
    event, values = window.read()

    if event == "GO!":

        syllableCount = countSyllables(values['word'])
        window['result'].update("Number of syllables: ")
        window['syllable'].update(syllableCount)

    if event == sg.WIN_CLOSED or event == "Exit":
        break
window.close()
