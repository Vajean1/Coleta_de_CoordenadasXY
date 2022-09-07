from time import sleep
import PySimpleGUI as sg
import pyautogui
import threading

def escrever_Coordendas():
    sleep(3)
    x, y = pyautogui.position()
    if pyautogui.onScreen(x,y):
        print('O mouse está na tela')
    else:
        print('O mouse está fora da tela.. Parando o programa!')
        exit()
    
    try:
        with open("coordenadas.txt", "a") as arquivo_coordenadas:
            arquivo_coordenadas.write(f'{x,y}\n')
        print('Coletado')
    except:
        print('Error')

sg.theme('DarkBlue')

layout = [[
    sg.Text('Deseja continuar marcando as coordenadas?', key='-OUTPUT-')
],[
    sg.Button('Continuar'), sg.Exit('Não')
]]

janela = sg.Window('Marcando coordenadas', size=(650, 100)).Layout(layout)
fechar = -1

while True:
    event, valores = janela.read(timeout=1000)
    if event == 'Não':
        janela['-OUTPUT-'].update('Fechando... Verifique o arquivo coordenadas...')
        fechar = 1
    elif event == 'Continuar':
        janela['-OUTPUT-'].update('Coletando as marcações.. Continue pressionando para continuar coletando.')
        threading.Thread(target=escrever_Coordendas).start()
        for i in range(1, 500):
            sg.one_line_progress_meter('Coletando Coordenadas', i+1, 500, key="-PROGRESS-", orientation="h", no_button=True)
    elif event == sg.WIN_CLOSED:
        break
    if fechar > -1:
        if fechar == 0:
            break
        fechar -= 1

janela.close()
