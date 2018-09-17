from tkinter import *


def ClearScreen():
    print("\033[0d\033[2J")

def Debug_Message():
    print("CLI Output:")

def doNothing():
    print("Working one!")

def ExitApp():
    exit()



ClearScreen()
Debug_Message()


root = Tk()
root.geometry("800x600")
root.title("PyTerm 0.1")



menu = Menu(root)
root.config(menu = menu)



subMenu = Menu(menu)
menu.add_cascade(label = "FIle", menu = subMenu)

subMenu.add_command(label ="Clear screen        Ctrl+Shift+L", command = doNothing)
subMenu.add_command(label ="Send RAW file     Ctrl+Shift+R", command = doNothing)
subMenu.add_command(label ="Save RAW file     Ctrl+Shift+S ", command = doNothing)
subMenu.add_command(label ="Quit                     Alt+Shift+4", command = ExitApp)



editMenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editMenu)

editMenu.add_command(label = "Copy", command = doNothing)
editMenu.add_command(label = "Paste", command = doNothing)
editMenu.add_command(label = "Select All", command = doNothing)



logMenu = Menu(menu)
menu.add_cascade(label = "Log", menu = logMenu)

logMenu.add_command(label = "To file...", command = doNothing)
logMenu.add_command(label = "Resume", command = doNothing)
logMenu.add_command(label = "Stop", command = doNothing)
logMenu.add_command(label = "Clear", command = ClearScreen)


ConfigurationMenu = Menu(menu)
menu.add_cascade(label = "Configuration", menu = ConfigurationMenu)

ConfigurationMenu.add_command(label = "Port", command = doNothing)
ConfigurationMenu.add_command(label = "Main Window", command = doNothing)
ConfigurationMenu.add_command(label = "Local echo", command = doNothing)
ConfigurationMenu.add_command(label = "CR LF auto", command = doNothing)
ConfigurationMenu.add_command(label = "Macros", command = doNothing)
ConfigurationMenu.add_command(label = "Load Configuration", command = doNothing)
ConfigurationMenu.add_command(label = "Save Configuration", command = doNothing)
ConfigurationMenu.add_command(label = "Delete Configuration", command = doNothing)




ControlSignalsMenu = Menu(menu)
menu.add_cascade(label = "Control signals", menu = ControlSignalsMenu)

ControlSignalsMenu.add_command(label = "Send Break", command = doNothing)
ControlSignalsMenu.add_command(label = "Open Port", command = doNothing)
ControlSignalsMenu.add_command(label = "Close Port", command = doNothing)
ControlSignalsMenu.add_command(label = "Toogle DTR", command = doNothing)
ControlSignalsMenu.add_command(label = "Toogle RTS", command = doNothing)

ViewMenu = Menu(menu)
menu.add_cascade(label = "View", menu = ViewMenu)

ViewMenu.add_command(label = "ASCII", command = doNothing)
ViewMenu.add_command(label = "Hexadecimal", command = doNothing)
ViewMenu.add_command(label = "Hexadecimal chars", command = doNothing)
ViewMenu.add_command(label = "Show index", command = doNothing)
ViewMenu.add_command(label = "Send hexadecimal data", command = doNothing)



HelpMenu = Menu(menu)
menu.add_cascade(label = "Help", menu = HelpMenu)

HelpMenu.add_command(label = "About", command = doNothing)


text = Text(root, height = 30, width = 99)
text.grid()


root.mainloop()

