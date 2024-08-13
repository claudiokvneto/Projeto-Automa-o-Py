from funcoes import *

interrupt_key = 'ctrl + x' 

lista_objetos = (125, 91)
search_vscode = (125, 91) #aba de busca do VScode
open_in_editor = (501, 227) #501
bloco_notas = (2407, 642) #coordenadas do bloco de notas
distance = 18 #18 #distancia entre cada objeto

time.sleep(2)
mouse_x, mouse_y = pyautogui.position()
print('Posição inicial do mouse:', (mouse_x, mouse_y))

for i in range(10):
    pyautogui.moveTo(mouse_x, mouse_y + (distance * i))
    time.sleep(0.5)

    pyautogui.doubleClick()
    pyautogui.click()

    copiar()

    objeto = pyperclip.paste()

    pyautogui.moveTo(lista_objetos)
    pyautogui.click()
    time.sleep(0.1)

    if objeto.startswith('w') or objeto.startswith('u') or objeto.startswith('f'):
        colar()
    else:
        colar()
        keyboard.press_and_release('backspace')

    time.sleep(3)

    keyboard.press_and_release('alt + enter')

    time.sleep(4)

    pyautogui.moveTo(open_in_editor)
    pyautogui.doubleClick()
    time.sleep(0.3)
    
    copiar()
    time.sleep(0.3)

    keyboard.press_and_release('ctrl + F4')
    time.sleep(0.5)

    resultado = pyperclip.paste()

    time.sleep(0.5)

    resultado = int(resultado)

    if resultado <= 1:
        time.sleep(0.5)
        pyautogui.moveTo(bloco_notas)
        pyautogui.click()
        keyboard.press_and_release('enter')
        time.sleep(0.3)
        pyperclip.copy(objeto)
        time.sleep(0.3)
        colar()

    time.sleep(0.5)
    pyautogui.moveTo(search_vscode)
    pyautogui.doubleClick()
    time.sleep(0.1)
    keyboard.press_and_release('backspace')

    if resultado <= 1:
        print("O objeto: {} não está sendo utilizado".format(objeto))
    else:
        print("O objeto: {} está sendo utilizado".format(objeto))

    time.sleep(1)

    if keyboard.is_pressed(interrupt_key):
        print("Interrupção do usuário detectada.")
        break 