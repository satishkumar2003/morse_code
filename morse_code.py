import tkinter as tk

morse_code = {'a':'. _','b':'_ . . .','c':'_ . _ .','d':'_ . .','e':'.','f':'. . _ .','g':'_ _ .','h':'. . . .','i':'. .','j':'. _ _ _','k':'_ . _','l':'. _ . .',
            'm':'_ _','n':'_ .','o':'_ _ _','p':'. _ _ .','q':'_ _ . _','r':'. _ .','s':'. . .','t':'_','u':'. . _','v':'. . . _','w':'. _ _','x':'_ . . _',
            'y':'_ . _ _','z':'_ _ . .','0':'_ _ _ _ _','1':'. _ _ _ _','2':'. . _ _ _','3':'. . . _ _','4':'. . . . _','5':'. . . . .','6':'_ . . . .',
            '7':'_ _ . . .','8':'_ _ _ . .','9':'_ _ _ _ .','?':'. . _ _ . .','!':'_ . _ . _ _','.':'. _ . _ . _',',':'_ _ . . _ _',';':'_ . _ . _ .',':':'_ _ _ . . .'}

def english_conversion(inp):
    morse_text = ''
    for i in inp:
        if i != ' ':
            try:
                i = morse_code[i.lower()] + '   '
            except:
                i = '.......   '
        else:
            i = '    '
        morse_text += i
    em_converted.delete('1.0','end')
    em_converted.insert(tk.END,morse_text)

def morse_conversion(inp):
    words = inp.split('       ')
    characters = []
    for i in words:
        characters += [i.split('   '),]
    eng = list(morse_code.keys())
    morse = list(morse_code.values())
    english_text = ''
    for i in characters:
        for j in i:
            try:    
                ind = morse.index(j)
                english_text += eng[ind]
            except:
                english_text += '<couldn\'t find character>'
        english_text += ' '
    me_converted.delete('1.0','end')
    me_converted.insert(tk.END,english_text)

def morse_alphabet():
    popup = tk.Tk()
    popup.geometry('500x600')
    popup.title('Morse Alphabet')    
    
    alphabet = ''
    for eng,mrs in morse_code.items():
        alphabet += "%s : %s \n" % (eng,mrs)
    
    text = tk.Text(popup,height = 500,width=600,font = ('Consolas',18))
    text.insert(tk.END,alphabet)
    text.pack()
    
    
    popup.mainloop()

height,width = 700,1400

root = tk.Tk()
root.title('English-Morse Translator')

canvas = tk.Canvas(root,height = height,width = width)
canvas.pack()

frame = tk.Frame(root,bg = '#43c59e',bd = 5)
frame.place(relheight=1,relwidth=1)

help = tk.Button(frame,text='Morse Alphabet',font = ('Consolas',18),command = lambda:morse_alphabet())
help.place(relx = 0.5, rely = 0.02,relheight = 0.09,relwidth = 0.3,anchor = 'n')

em_entry = tk.Entry(frame,font =('Consolas',18))
em_entry.place(relx = 0.34,rely = 0.12,relheight = 0.07,relwidth = 0.64)

eng_to_mrs = tk.Button(frame,text = 'English to Morse',font =('Consola',18),command = lambda:english_conversion(em_entry.get()))
eng_to_mrs.place(relx = 0.01,rely = 0.12,relheight = 0.07,relwidth = 0.3)

me_entry = tk.Entry(frame,font = ('Consolas',18))
me_entry.place(relx=0.34,rely=0.56,relheight=0.07,relwidth=0.64)

mrs_to_eng = tk.Button(frame,font =('Consola',18),text = 'Morse to English',command = lambda:morse_conversion(me_entry.get()))
mrs_to_eng.place(relx=0.01,rely=0.56,relheight=0.07,relwidth=0.3)

em_converted = tk.Text(frame,font =('Consola',14))
em_converted.place(relx=0.34,rely=0.2,relheight = 0.34,relwidth = 0.64)

me_converted = tk.Text(frame,font =('Consola',12))
me_converted.place(relx=0.34,rely=0.64,relheight = 0.34,relwidth = 0.64)

root.mainloop()