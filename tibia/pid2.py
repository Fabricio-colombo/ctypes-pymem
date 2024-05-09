from pymem import *
from pymem.process import *
import ctypes
import time

WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_MOUSEMOVE = 0x0200
MK_LBUTTON = 0x0001

WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202
WM_RBUTTONDOWN = 0x0204
WM_RBUTTONUP = 0x0205


F1 = 0x70
F2 = 0x71
F3 = 0x72
F4 = 0x73
F5 = 0x74
F6 = 0x75
F7 = 0x76
F8 = 0x77
F9 = 0x78
F10 = 0x79
F11 = 0x7A
F12 = 0x7B 

SCAN_F1= 0x3B
SCAN_F2= 0x3C
SCAN_F3= 0x3D
SCAN_F4= 0x3E
SCAN_F5= 0x3F
SCAN_F6= 0x40
SCAN_F7= 0x41
SCAN_F8= 0x42
SCAN_F9= 0x43
SCAN_F10= 0x44
SCAN_F11= 0x57
SCAN_F12= 0x58
SCAN_ENTER= 0x1C
SCAN_CTROL= 0x1D
SCAN_BACKSPACE= 0x0E
SCAN_CAPS= 0x3A
SCAN_NUNLOCK= 0x45
SCAN_TAB= 0x0F
SCAN_UP = 0xC8
SCAN_LEFT = 0xCB
SCAN_RIGHT = 0xCD
SCAN_DOWN = 0xD0
SCAN_ENTER = 0x1C
SCAN_ESC = 0x01

while True:
    def ler_endereco(pid, endereco):
        try:
            processo = pymem.Pymem(pid)
            valor = processo.read_int(endereco)
            processo.close_process()
            return valor
        except pymem.exception.MemoryReadError:
            return None

    pid = 19196
    enderecos = ["0B63DC50", "291BCBB4", "2923590C", "2B1039F8", "2B118E80"]

    for endereco in enderecos:
        valor = ler_endereco(pid, int(endereco, 16))
        if valor is not None:
            print(f"Valor no endereço {endereco}: {valor}")
        else:
            print(f"Falha ao ler o valor no endereço {endereco}")
            
    def send_message_keyboard(hwnd, key_code):
        ctypes.windll.user32.SendMessageW(hwnd, WM_KEYDOWN, key_code, 0)
        time.sleep(0.2)
        ctypes.windll.user32.SendMessageW(hwnd, WM_KEYUP, key_code, 0)

    hwnd = ctypes.windll.user32.FindWindowW(0, 'Tibia - Oleg Winchester')


    if valor <= 500:
        send_message_keyboard(hwnd, F10)
        print('Usou Exura...')
