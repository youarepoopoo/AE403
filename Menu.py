import tkinter as tk

window = tk.Tk()

window.title("麥噹噹速食店")

window.geometry("500x500")

menuBar = tk.Menu(window)

fileMenu = tk.Menu(menuBar, tearoff = False)

fileMenu.add_command(label = "雞塊")

fileMenu.add_command(label = "漢堡")

fileMenu.add_separator()

fileMenu.add_command(label = "薯條~")

menuBar.add_cascade(label = "麥噹噹菜單_主食", menu = fileMenu)

fileMenu2 = tk.Menu(menuBar, tearoff = False)

fileMenu2.add_command(label = "可樂")

fileMenu2.add_command(label = "雪屁")

subMenu = tk.Menu(menuBar, tearoff = False)

subMenu.add_command(label = "大屁屁")

subMenu.add_command(label = "38元喔~")

fileMenu2.add_cascade(label = "雪屁", menu = subMenu)

menuBar.add_cascade(label = "麥噹噹菜單_飲料", menu = fileMenu2)

fileMenu3 = tk.Menu(menuBar, tearoff = False)

fileMenu3.add_command(label = "吉拿娃娃棒")

fileMenu3.add_separator()

fileMenu3.add_command(label = "好好吃泥土")

menuBar.add_cascade(label = "麥噹噹菜單_點心", menu = fileMenu3)

submenu = tk.Menu(menuBar, tearoff = False)

submenu.add_command(label = "純種吉娃娃肉")

submenu.add_command(label = "380元喔~")

fileMenu3.add_cascade(label = "吉拿娃娃棒", menu = submenu)

window.config(menu = menuBar)

window.mainloop()