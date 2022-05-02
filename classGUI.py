from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext, filedialog
from tkinter import messagebox

class GUI:
    def __init__(self, titulo, geometria):
        self.title = titulo
        self.geome = geometria
        self.txt = Entry()
        self.btn = Button()
        self.lbl = Label()
        self.combo = Combobox()
        self.scroll = scrolledtext.ScrolledText()
        self.chkbuton = Checkbutton()
        self.rdiobuton = Radiobutton()
        self.spnbox = Spinbox()
        self.progbar = Progressbar()
        self.unem = Menu()

    def ventana(self, window):
        window.title(self.title)
        window.geometry(self.geome)

    def label(self, window, texto, fuente, tamany, col, wor):
        if not fuente:
            ## Informado solo texto
            self.lbl = Label(window, text=texto)
        elif not tamany:
            ## Informado texto y fuente
            self.lbl = Label(window, text=texto, font=(fuente))
        else:
            ## Informado texto, fuente y tamany
            self.lbl = Label(window, text=texto, font=(fuente, tamany))
        self.lbl.grid(column=col, row=wor)

    def button(self, window, texto, col, wor, funcion):
        self.btn = Button(window, text=texto, command=funcion)
        self.btn.grid(column=col,row=wor)

    def entry(self, window, ancho, col, wor):
        self.txt = Entry(window, width=ancho)
        self.txt.grid(column=col, row=wor)

    def combobox(self,window,values,sel,col,wor):
        self.combo = Combobox(window)
        self.combo['values']=values
        self.combo.current(sel)
        self.combo.grid(column=col,row=wor)

    def Scrolltext(self,window,w,h,col,wor):
        self.scroll = scrolledtext.ScrolledText(window, width=w, height=h)
        self.scroll.grid(column=col,row=wor)

    def Scrolltext_insert(self,text):
        self.scroll.insert(INSERT, text) ## Insertamos texto por defecto al scrolltext

    def Scrolltext_borrar(self):
        self.scroll.delete(1.0,END) ## Borramos todo el scrolltext

    def Scrolltext_leer(self):
        return ventana.scroll.get(1.0,END) ## Leemos todo el scrolltext

    def checkbutton(self,window,texto,var,col,wor):
        self.chkbuton = Checkbutton(window, text=texto, variable=var, onvalue=1, offvalue=0)
        self.chkbuton.grid(column=col,row=wor)

    def radiobutton(self,window,texto,val,var,col,wor):
        self.rdiobuton = Radiobutton(window,text=texto, value=val, variable=var)
        self.rdiobuton.grid(column=col,row=wor)

    def spinbox(self,window,frm,ot,wid,txtvar,col,wor):
        self.spnbox = Spinbox(window,from_=frm,to=ot,width=wid,textvariable=txtvar)
        self.spnbox.grid(column=col,row=wor)

    def progressbar(self,window,long,col,wor): #(self,window,long,stilo,col,wor):
        self.progbar = Progressbar(window, length=long) #, style=stilo)
        self.progbar.grid(column=col,row=wor)

    def FileDialog(self,typefile1,typefile2,num):
        if num == 1:
            return filedialog.askopenfilename(filetypes=(typefile1,typefile2))
        else:
            return filedialog.askopenfilenames(filetypes=(typefile1,typefile2))

    def AskDialog(self):
        return filedialog.askdirectory()

    def menu(self,window,lbl,list):
        self.unem = Menu(window)
        for y in range(0,len(lbl)):
            item = 'new_item'+lbl[y] ## Por cada menu generamos el nombre de una variable
            item = Menu(self.unem, tearoff=0)
            for x in range(0,len(list[y])):
                item.add_command(label=list[y][x]) ## En cada menu ponemos todas sus opciones
                if x == len(list[y])-1:
                    self.unem.add_cascade(label=lbl[y], menu=item) ## Generamos el menu con sus opciones respectivas
        window.config(menu=self.unem)

class MSGBox:
    def ShowInfo(self,titulo,msg): ## Mensage de Información
        messagebox.showinfo(titulo,msg)

    def ShowWarning(self,titulo,msg): ## Mensage de Warning
        messagebox.showwarning(titulo,msg)

    def ShowError(self,titulo,msg): ## Mensage de Error
        messagebox.showerror(titulo,msg)

    def AskQuestion(self,titulo,msg): ## Pregunta de SI o NO
        return messagebox.askquestion(titulo,msg)

    def AskYesNo(self,titulo,msg): ## Pregunta de TRUE o FALSE
        return messagebox.askyesno(titulo,msg)

    def AskYesNoCancel(self,titulo,msg): ## Pregunta de TRUE, FALSE o CANCEL
        return messagebox.askyesnocancel(titulo,msg)

    def AskOkCancel(self,titulo,msg): ## Pregunta de TRUE o FALSE
        return messagebox.askokcancel(titulo,msg)

    def AskRetryCancel(self,titulo,msg): ## Pregunta de TRUE o FALSE
        return messagebox.askretrycancel(titulo,msg)

def clk():
    print("Button clicked!!!")
    res = ventana.txt.get()
    print(res)

def clk_combo():
    print("Button Combobox")
    res = ventana.combo.get()
    print(res)

def clk_delscrolltext():
    ventana.Scrolltext_borrar() ## Para borrar el texto en el scrolltext
    ventana.Scrolltext_insert("Insert your code here!!!!")

def clk_readscrolltext():
    txt = ventana.Scrolltext_leer() ## Para leer el texto del scrolltext
    print(txt)

def clk_chkbutton(): ## Se tiene que chequear todas las variables de los checkbutton
    if C1.get() == 1:
        print("Selected C1")
    else:
        print("Not Selected C1")
    if C2.get() == 1:
        print("Selected C2")
    else:
        print("Not Selected C2")

def clk_rdiobuton():
    print(sel.get())

def clk_spinbox():
    print(var.get())

window = Tk()
ventana = GUI("Soy el REY!!", "480x720") ## (Titulo de la ventana, tamaño de la ventana)
ventana.ventana(window)
ventana.label(window, "Hola Mundo!!!", "Arial", "20", 0, 0) ## (Texto del label, fuente del label, tamaño del label, posX, posY)
ventana.button(window, "Boton", 0, 1, clk) ## (Texto del boton, posX, posY, funcion del evento)
ventana.entry(window, 10, 0, 2) ## (Ancho de la entrada de texto, posX, posY)
############### ComboBox
valor = [1, 2, 3, 4, 5, "Pedro!!"]
ventana.combobox(window, valor, 0, 0, 3) ## (Introduccion valores al combo, posinicial combo, posX, posY)
ventana.button(window, "Boton", 0, 4, clk_combo)
############### ScrollText
ventana.Scrolltext(window,50,10,0,5) ## (Ancho de caracteres, filas, posX, posY)
ventana.Scrolltext_insert("Insert here your code...") ## (Texto por defecto del scrolltext)
ventana.button(window,"Borrar",0,6,clk_delscrolltext) ## Boton borra el scrolltext
ventana.button(window,"Enviar",0,7,clk_readscrolltext) ## Boton lee el scrolltext
############### CheckButton
C1 = IntVar() ## Variable checkbutton
C2 = IntVar() ## Variable checkbutton
ventana.checkbutton(window,"Choose",C1,0,8) ## Opción checkbutton
ventana.checkbutton(window,"Music",C2,0,9) ## Opción checkbutton
ventana.button(window,"Enviar",0,10,clk_chkbutton) ## Boton checkbutton
############### RadioButton
sel = IntVar() ## Variable radiobutton
ventana.radiobutton(window,"Primer",1,sel,0,11) ## Opción radiobutton
ventana.radiobutton(window,"Segundo",2,sel,0,12) ## Opción radiobutton
ventana.radiobutton(window,"Tercero",3,sel,0,13) ## Opción radiobutton
ventana.button(window,"Enviar",0,14,clk_rdiobuton) ## Boton radiobutton
############### SpinBox
var = IntVar() ## Variable spinbox
var.set(20) ## Valor por defecto
ventana.spinbox(window,0,100,5,var,0,15)
ventana.button(window,"Enviar",0,16,clk_spinbox) ## Boton spinbox
############### ProgressBar
ventana.progressbar(window,100,0,17)#(window,100,'',0,17)
ventana.progbar['value'] = 30 # Valor de la ProgressBar, debe ir cambiando segun vaya evolucionando
############### FileDialog
file = ventana.FileDialog(("Text files","*.txt"),("all files","*.*"),1) ## Seleccionamos 1 archivo
print(file)
files = ventana.FileDialog(("Text files","*.txt"),("all files","*.*"),2) ## Seleccionamos + de 1 archivo
print(files)
############### AskDirectory
dir = ventana.AskDialog() ## Preguntamos directorio de trabajo
print(dir)
############### Menu
etiqueta = ["Archivo","Ayuda"]
lista = [["Abrir","Cerrar"],["Somos...","Version","Github"]] ## Lista con los elementos del menu
ventana.menu(window,etiqueta,lista) ## Llamamos para crear el menu
############### MessageBox
BoxMSG = MSGBox()
BoxMSG.ShowInfo("INFO","Soy FELIZ!!!")
BoxMSG.ShowWarning("WARNING","Noooooo!!!")
BoxMSG.ShowError("ERROR","Horror!!!")
res = BoxMSG.AskQuestion("PREGUNTA","Eres un crack??")
print(res)
res = BoxMSG.AskYesNo("Pregunta","Eres un crack??")
print(res)
res = BoxMSG.AskYesNoCancel("Pregunta","Eres un crack??")
print(res)
res = BoxMSG.AskOkCancel("Pregunta","Eres un crack??")
print(res)
res = BoxMSG.AskRetryCancel("Pregunta","Eres un crack??")
print(res)
###############
window.mainloop()
