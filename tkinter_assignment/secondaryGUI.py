import logging
from tkinter import *
from tkinter.messagebox import showerror
from os import listdir
from pdfmerger import pdfmerger

try:
    
    def pdfmergerGUI(path :str) -> 'function':
        '''-> :Returns the function which creates the GUI for merging PDF.
        :parameters: (path) - The Directory path'''
    
        def subfunction():
            '''This function creates a Graphical User Interface for
            listing out the PDFs in the directory and to do the merging operation.'''

            allfiles=listdir(path)
            pdffiles=[i for i in allfiles if str(i).endswith(('.pdf','.PDF'))]

            if pdffiles:    #checking if there are any pdf files in the directory

                def mergerfunction():
                    '''This function calls the pdfmerger function from the pdfmerger module.'''

                    name=pdfmerger(pdfpath,inputname.get())
                    end=Label(main,text='Merging Successful : '+name)
                    end.pack()

                main=Tk()
                main.geometry('400x500')
                
                sub=Label(main,text='Enter filename for merged PDF :')
                sub.pack()

                inputname=Entry(main)
                inputname.pack()

                pdfpath=[path+'/'+i for i in pdffiles]
                
                merge=Button(main,text='Merge',command=mergerfunction,fg='white',bg='purple',activebackground='green')
                merge.pack()
                
                head=Label(main,text='\nPDF files in Directory :',font='helvetica 9 bold')
                head.pack()
                
                txt='\n'.join(pdffiles)
                body=Label(main,text=txt)
                body.pack()

                main.mainloop()

            else:
                showerror('Oops!','There are no PDFs in the Directory.')

        return subfunction

except Exception:

    logger=logging.getLogger(__name__)
    Handler=logging.FileHandler('secondaryGUI.log')
    Format=logging.Formatter('%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s',datefmt='%d/%m/%Y  %I:%M:%S %p')
    Handler.setFormatter(Format)
    logger.addHandler(Handler)

    logger.exception('Unexpected Exeption occured.')