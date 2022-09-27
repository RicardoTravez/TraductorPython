from tkinter import Tk,Frame,Button,PhotoImage,Label
from tkinter.scrolledtext import ScrolledText
from tkinter import scrolledtext as st
from tkinter import filedialog, messagebox
from tkinter import ttk
import tkinter as tk
import pyttsx3
import googletrans

def open_file():
	filepath = filedialog.askopenfilename(title= 'Seleccione archivo',
		filetype = (('archivo txt', '*.txt*'), ('Todos', '*.*')))
	if filepath != ' ':
		file = open(filepath, 'r')
		content = file.read()
		caja.delete('1.0', 'end')
		caja.insert('0.0', content)
		ventana.title(filepath)

def start_read():
	text_read = caja2.get('1.0', 'end')
	voice = selec_voice.get()
	voices = engine.getProperty('voices')
	if voice == 'Español':
		engine.setProperty('voice', voices[0].id)
	if voice == 'Ingles':
		engine.setProperty('voice', voices[1].id)

	if len(text_read)>2:
		engine.say(text_read)
		engine.runAndWait()
		engine.stop()
	else:
		messagebox.showerror('Error', 'No hay un texto para leer')

def save_sound():
	if len(caja2.get('1.0', 'end'))>2:
		name = caja2.get('1.0', 'end').split(' ')
		print(name)
		name = name[0:1][0]
		engine.save_to_file(caja2.get('1.0', 'end'), f'{name}.mp3')
		engine.runAndWait()
		messagebox.showinfo('Aviso', 'Audio guardado correctamente')
	else:
		messagebox.showerror('Error', 'No hay un texto para grabar')
		

ventana = tk.Tk()
ventana.title('Traductor con python')
ventana.config(bg='silver')
ventana.geometry('800x600+300+50')
ventana.iconbitmap('assets/icon.ico')
engine = pyttsx3.init('sapi5')


image_woman = PhotoImage(file= 'assets/woman.png')
image_record = PhotoImage(file= 'assets/record.png')
image_file = PhotoImage(file= 'assets/file.png')

frame_control = Frame(ventana, bg= 'gray', width=200, height=100)
frame_control.grid(column=0, row=1, sticky='nsew', pady = 5, padx=5)

ventana.columnconfigure(0, weight=6)
ventana.columnconfigure(1, weight=0)
ventana.rowconfigure(0, weight=1)

button_open = Button(frame_control,image = image_file,compound= 'left',text= 'ABRIR ARCHIVO',
font= ('Arial', 11, 'bold') , bg= 'magenta', command= open_file)
button_open.grid(columnspan=2, column=0, row=0, sticky='nsew')
button_open.place(x=20, y=30)

button_read = Button(frame_control,image = image_woman,compound= 'left',text= 'LEER',
font= ('Arial', 11, 'bold') , bg= 'magenta', command= start_read)
button_read.grid(columnspan=2, column=1, row=0, sticky='nsew')
button_read.place(x=350, y=30)

button_grab = Button(frame_control,image = image_record,compound= 'left',text= 'GRABAR AUDIO',
font= ('Arial', 11, 'bold') , bg= 'magenta', command= save_sound)
button_grab.grid(columnspan=2, column=2, row=0, sticky='nsew')
button_grab.place(x=590, y=30)

selec_voice = ttk.Combobox(ventana, values=['Ingles', 'Español'], state= 'readonly',width=10,)
selec_voice.grid(columnspan=3, column=0, row=0, sticky='')
selec_voice.set('Seleccionar')

traductor = googletrans.Translator()

boton_fondo = 'green'
lista_fondo = 'blue'

caja = st.ScrolledText(ventana, width=40, height=15, relief='flat', font=('Calibri Light', 12))
caja.place(x=15, y=100)

caja2 = st.ScrolledText(ventana, width=40, height=15, relief='flat', font=('Calibri Light', 12))
caja2.place(x=445, y=100)

def traducir():
    datos = caja.get('1.0', tk.END)
    traduccion = traductor.translate(datos, dest=idioma2.get())
    caja2.insert(tk.END, traduccion.text)

def borrar():
    caja.delete('1.0', tk.END)
    caja2.delete('1.0', tk.END)

idioma=tk.StringVar(ventana)
idioma2=tk.StringVar(ventana)
list1 = googletrans.LANGUAGES
list2 = list1.values()
list3 = list(list2)
idiomas = []
for i in list3:
    idiomas.append(i)

droplist= tk.OptionMenu(ventana, idioma, *idiomas)
idioma.set('Seleccione el idioma a traducir')
droplist.config(width=32, cursor='hand2', relief='flat', bg=lista_fondo, font=('Arial', 12, 'bold'))
droplist.place(x=15, y=31)

droplist2= tk.OptionMenu(ventana, idioma2, *idiomas)
idioma2.set('Traducir a:')
droplist2.config(width=31, cursor='hand2', relief='flat', bg=lista_fondo, font=('Arial', 12, 'bold'))
droplist2.place(x=445, y=30)

#botones
boton2 = tk.Button(ventana, text='Traducir', command=traducir, relief='flat', cursor='hand2', bg=boton_fondo, height=2, width=12, font=('Arial', 12, 'bold'))
boton2.place(x=135, y=400)
      
boton3 = tk.Button(ventana, text='Borrar',relief='flat', command=borrar, cursor='hand2', bg=boton_fondo, height=2, width=12, font=('Arial', 12, 'bold'))
boton3.place(x=515, y=400)

ventana.mainloop()



