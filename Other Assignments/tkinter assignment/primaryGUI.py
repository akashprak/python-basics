import logging
from tkinter import *
from tkinter.messagebox import showerror
from os import listdir
from secondaryGUI import pdfmergerGUI

try:

    parent=Tk()
    parent.geometry('400x500')

    s=Scrollbar(parent,orient='vertical')
    s.pack(side=RIGHT,fill='y')

    def fileslist():       # function to execute when enter button is clicked
        
        path=directory.get()

        try:
            val=listdir(path)

            txt='\n'.join(val)
            pdf.configure(command=pdfmergerGUI(path))
            pdf.pack()

            outheader.pack()

            output.pack()
            output.delete(1.0,END)             # deleting contents of text widget everytime this function is executed to avoid repetition         
            output.insert(1.0,txt,'center')

            s.config(command=output.yview)

        except FileNotFoundError as e:
            showerror('ERROR',e)


    header=Label(parent,text='Enter Directory Path')
    header.pack()

    directory=Entry(parent,width=50)
    directory.pack()

    B=Button(parent,text="ENTER",command=fileslist,fg='black',bg='grey',activebackground='green')
    B.pack()

    pdf=Button(parent,text='Merge PDFs in Directory',bg='purple',fg='white',activebackground='green')

    outheader=Label(parent,text='\nFiles in the Directory are :',font=('helvetica 9 bold'))

    output=Text(parent,background=header.cget("background"),
    borderwidth=0, font=header.cget("font"),yscrollcommand=s.set)       # the background and font for the text output is set to be the same as the header label

    output.tag_configure('center',justify='center')         # configuring the directory files output to be at center
    
    parent.mainloop()

except Exception as e:

    logger=logging.getLogger(__name__)
    Handler=logging.FileHandler('primaryGUI.log')
    Format=logging.Formatter('%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s',datefmt='%d/%m/%Y  %I:%M:%S %p')
    Handler.setFormatter(Format)
    logger.addHandler(Handler)

    logger.exception('Unexpected Exeption occured.')
