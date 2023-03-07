import PySimpleGUI as sg

layout = [[sg.Text("牛乳"),
           sg.Combo(list(range(1,10)),key = "-QUANTITY-"),
           sg.Text("個")],
          [sg.Button("購入" ,key = "-SUBMIT-")],
          [sg.Text(key="-AMOUNT-",size=(120,10))]]

window = sg.Window("ユウキの牛乳アプリ",layout,size=(350,350))

while True:
    event , values = window.read()
    if event == "-SUBMIT-":
        result = 150 * int(values["-QUANTITY-"])
        window["-AMOUNT-"].update(value=f"金額 {result}円です")

        if event == sg.WIN_CLOSED:
            break