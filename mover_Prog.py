from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
from moveFiles import move_files


gui = Tk()
gui.geometry("400x400")
gui.title("MoverProgram")
gui.resizable(False,False)

    
   



class FolderSelect(Frame):
    def __init__(self,parent=None,folderDescription="",**kw):
        Frame.__init__(self,master=parent,**kw)
        
        self.folderPath = StringVar()
        self.lblName = Label(self, text=folderDescription)
        self.lblName.grid(row=0,column=0,pady=2,padx=10)
        self.entPath = Entry(self, textvariable=self.folderPath)
        self.entPath.grid(row=0,column=1,padx=10,sticky="E")
        self.btnFind = ttk.Button(self, text="Browse Folder",command=self.setFolderPath)
        self.btnFind.grid(row=0,column=2)
      
    def setFolderPath(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)
    @property
    def folder_path(self):
        return self.folderPath.get()


    


         
        
   
    
            

folderPath = StringVar()

directory1Select = FolderSelect(gui,"Select desired folder")
directory1Select.grid(row=0,column=0,pady=10)

directory2Select = FolderSelect(gui,"Select destination")
directory2Select.grid(row=1,column=0,pady=0)



FILETYPES = [
".pdf",
".mp3",
".txt",
".jpg",
".wav",
".m4a",

] #etc



variable = StringVar(gui)
variable.set(FILETYPES[0])



dropList = OptionMenu(gui, variable, *FILETYPES)
dropList.grid(row=3,column=0)
def moveStuff():
    folder1 = directory1Select.folder_path
    
    folder2 = directory2Select.folder_path
    
    filetype=variable.get()
  
    move_files(folder1,folder2,filetype)

transferButton = ttk.Button(gui, text="Transfer", command=moveStuff)
transferButton.grid(row=4,column=0,pady=25)


gui.mainloop()



