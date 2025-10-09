import pyautogui

def automatico(nome, telefone):
    pyautogui.moveTo(120, 120, duration=2)
    pyautogui.click()
    pyautogui.write(nome)
    pyautogui.moveTo(200, 200, duration=1)
    pyautogui.click()
    pyautogui.write(telefone)
    pyautogui.moveTo(100, 280, duration=1)
    pyautogui.click()
    pyautogui.moveTo(80, 80, duration=1)
    pyautogui.click()

nomes = ['Edu', 'Beatriz', "Ana", "Claudia", 'Marcelo']
telefones = ['(11) 8923432', '(21) 932482', '(11) 73423234', '(31) 83423432', '(11) 823432432']

for i in range(len(nomes)):
    n = nomes[i]
    t = telefones[i]
    automatico(n, t)