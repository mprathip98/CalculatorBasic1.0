from customtkinter import *
#from PIL import Image
from tkinter import messagebox


window = CTk()
window.title("Calculator")
window.geometry("495x710")
set_appearance_mode("dark")
window.resizable(False, False)



# - Result Label

equationText = ""
equationLabel = StringVar()


resultLabel = CTkLabel(master=window,

                       corner_radius=5,
                       text_color='white',
                       width=470, height=90,
                       textvariable=equationLabel,
                       font=("Impact", 50),
                       anchor='e',
                       )
resultLabel.grid(column=1, row=1, pady=20, padx=1)

def buttonPress(nums):
    global equationText
    global equationLabel

    equationText = equationText + str(nums)
    equationLabel.set(equationText)


def equal():
    try:
        global equationText
        global equationLabel
        total = str(eval(equationText))
        equationLabel.set(total)
        equationText = " "
    except:
        messagebox.showinfo(title="error", message="try to clear and re-enter it again")


def clear():
    global equationText
    global equationLabel
    equationText = " "
    equationLabel.set(" ")

# - First Row Gray under the label



clearButton = CTkButton(master=window,
                        text="C",
                        fg_color="#BCC2C8",
                        corner_radius=20,
                        width=95,
                        height=95,
                        font=("Impact", 30),
                        text_color="black",
                        command=clear
                        )
clearButton.place(x=35, y=120)

#Set an if condition to button press and check if this is passed

signButton = CTkButton(master=window,
                       text="-/+",
                       fg_color="#BCC2C8",
                       corner_radius=20,
                       width=95,
                       height=95,
                       font=("Impact", 30),
                       text_color="black",
                       #command=buttonPress()
                       )
signButton.place(x=145, y=120)

percentButton = CTkButton(master=window,
                          text="%",
                          fg_color="#BCC2C8",
                          corner_radius=20,
                          width=95,
                          height=95,
                          font=("Impact", 30),
                          text_color="black",
                          #command=buttonPress()
                          )
percentButton.place(x=255, y=120)



# - Orange button for operations from right to down



divisionButton = CTkButton(master=window,
                           text="÷",
                           fg_color="#F7931E",
                           corner_radius=20,
                           width=95,
                           height=95,
                           font=("Impact", 30),
                           text_color="black",
                           command=lambda: buttonPress('/')
                           )
divisionButton.place(x=365, y=120)

multipyButton = CTkButton(master=window,
                          text="×",
                          fg_color="#F7931E",
                          corner_radius=20,
                          width=95,
                          height=95,
                          font=("Impact", 30),
                          text_color="black",
                          command=lambda: buttonPress('*'))
multipyButton.place(x=365, y=235)

addButton = CTkButton(master=window,
                      text="+",
                      fg_color="#F7931E",
                      corner_radius=20,
                      width=95,
                      height=95,
                      font=("Impact", 30),
                      text_color="black",
                      command=lambda: buttonPress('+'))
addButton.place(x=365, y=350)

subtractButton = CTkButton(master=window,
                           text="-",
                           fg_color="#F7931E",
                           corner_radius=20,
                           width=95,
                           height=95,
                           font=("Impact", 30),
                           text_color="black",
                           command=lambda: buttonPress('-'))
subtractButton.place(x=365, y=465)

equalButton = CTkButton(master=window,
                        text="=",
                        fg_color="#F7931E",
                        corner_radius=20,
                        width=95,
                        height=95,
                        font=("Impact", 30),
                        text_color="black",
                        command=equal)
equalButton.place(x=365, y=580)



# --- Number Button ---



sevenButton = CTkButton(master=window,
                        text="7",
                        fg_color="#848482",
                        corner_radius=20,
                        width=95,
                        height=95,
                        font=("Impact", 30),
                        text_color="white",
                        command=lambda: buttonPress(7))
sevenButton.place(x=35, y=235)

eightButton = CTkButton(master=window,
                        text="8",
                        fg_color="#848482",
                        corner_radius=20,
                        width=95,
                        height=95,
                        font=("Impact", 30),
                        text_color="white",
                        command=lambda: buttonPress(8))
eightButton.place(x=145, y=235)

nineButton = CTkButton(master=window,
                       text="9",
                       fg_color="#848482",
                       corner_radius=20,
                       width=95,
                       height=95,
                       font=("Impact", 30),
                       text_color="white",
                       command=lambda: buttonPress(9))
nineButton.place(x=255, y=235)

fourButton = CTkButton(master=window,
                       text="4",
                       fg_color="#848482",
                       corner_radius=20,
                       width=95,
                       height=95,
                       font=("Impact", 30),
                       text_color="white",
                       command=lambda: buttonPress(4))
fourButton.place(x=35, y=350)

fiveButton = CTkButton(master=window,
                       text="5",
                       fg_color="#848482",
                       corner_radius=20,
                       width=95,
                       height=95,
                       font=("Impact", 30),
                       text_color="white",
                       command=lambda: buttonPress(5))
fiveButton.place(x=145, y=350)

sixButton = CTkButton(master=window,
                      text="6",
                      fg_color="#848482",
                      corner_radius=20,
                      width=95,
                      height=95,
                      font=("Impact", 30),
                      text_color="white",
                      command=lambda: buttonPress(6))
sixButton.place(x=255, y=350)

oneButton = CTkButton(master=window,
                      text="1",
                      fg_color="#848482",
                      corner_radius=20,
                      width=95,
                      height=95,
                      font=("Impact", 30),
                      text_color="white",
                      command=lambda: buttonPress(1))
oneButton.place(x=35, y=465)

twoButton = CTkButton(master=window,
                      text="2",
                      fg_color="#848482",
                      corner_radius=20,
                      width=95,
                      height=95,
                      font=("Impact", 30),
                      text_color="white",
                      command=lambda: buttonPress(2))
twoButton.place(x=145, y=465)

threeButton = CTkButton(master=window,
                        text="3",
                        fg_color="#848482",
                        corner_radius=20,
                        width=95,
                        height=95,
                        font=("Impact", 30),
                        text_color="white",
                        command=lambda: buttonPress(3))
threeButton.place(x=255, y=465)

zeroButton = CTkButton(master=window,
                       text="0",
                       fg_color="#848482",
                       corner_radius=20,
                       width=205,
                       height=95,
                       font=("Impact", 30),
                       text_color="white",
                       command=lambda: buttonPress(0))
zeroButton.place(x=35, y=580)

pointButton = CTkButton(master=window,
                        text=".",
                        fg_color="#848482",
                        corner_radius=20,
                        width=95,
                        height=95,
                        font=("Impact", 30),
                        text_color="white",
                        command=lambda: buttonPress('.'))
pointButton.place(x=255, y=580)

window.mainloop()