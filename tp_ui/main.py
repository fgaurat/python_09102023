from tkinter import *
from tkinter import ttk

def center_window(root):
    # Mettre à jour les tâches en attente pour s'assurer que la fenêtre est complètement chargée
    root.update_idletasks()
    
    # Calculer la position x et y pour centrer la fenêtre
    x = (root.winfo_screenwidth() - root.winfo_width()) // 2
    y = (root.winfo_screenheight() - root.winfo_height()) // 2
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{x}+{y}")


def sayHello():
    print("Bonjour")

def main():
    root = Tk()

    frm = ttk.Frame(root, padding=10)
    frm.grid()
    lbl = ttk.Label(frm, text="Hello World!")
    lbl.grid(column=0, row=0)

    ttk.Button(frm, text="Quit", command=lambda :lbl.config(text="toto")).grid(column=1, row=0)
    # Button(frm, text="Say Hello", command=sayHello,bg="red").grid(column=0, row=1)
    Button(frm, text = 'Submit', bg='blue', fg='white').grid(column=0, row=1)

    entry =Entry(frm).grid(column=0, row=2,)
    root.after(0, center_window, root)
    root.mainloop()



if __name__=='__main__':
    main()
