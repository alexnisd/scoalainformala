import tkinter
import tkinter.messagebox
import pickle

# videoclip folosit pentru documentare: https://www.youtube.com/watch?v=8qUJ9a_3zSQ

root = tkinter.Tk()
root.title("Lista task-uri")


def add_task():  # functie pentru adaugarea unui task
    task = entry_task.get()  # ne da textul introdus
    if task != "":
        listbox_tasks.insert(tkinter.END, task)  # inseram la sfarsit, acel END la asta se refera, iar dupa , avem un
# task
        entry_task.delete(0, tkinter.END) # practic aici dupa ce introducem un task se va sterge textul
    # introdus din chenarul de add task
    else:
        tkinter.messagebox.showwarning(title="Avertizare", message="Nu poti introduce un task gol")  # practic aici am
# scris aceasta linie pentru ca utilizatorul sa nu poata introduce un task gol

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]  # practic aici pentru stergere ne trebuie o selectie
# iar acel 0 este pentru a sterge un singur task, deoarece poti selecta mai multe tasks in acelasi timp
        listbox_tasks.delete(task_index)  # iar aici aceasta comanda sterge selectia de index
    except:
        tkinter.messagebox.showwarning(title="Avertizare", message="Nu poti sa stergi nimic, selecteaza un task 😂")
        #  practic am folosit try si except pt ca in cazul in care dadeai delete si nu selectai un task murea codul
def load_tasks():
    tasks = pickle.load(open("tasks.dat", "rb"))  # practic acelasi concept ca si la save tasks doar ca aici nu avem
# write binary avem read binary
    for task in tasks:
        listbox_tasks.insert(tkinter.END, task)  # iar practic aici
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())  # practic aici o sa ne dea taskurile ca si un tuplu
    pickle.dump(tasks, open("tasks.dat", "wb"))  # practic aici am folosit pickle pentru ca era cel mai simplu de
# folosit, pentru moment cel putin, iar acel "wb" se refera la write binary

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)  # practic aici este chenarul
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)  # practic aici avem un scroll
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)  # aici am pus scroll-ul in dreapta, pentru ca previously era
# pus pe mijloc :))

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)  # practic asta este pentru scroll in directia "y"
scrollbar_tasks.config(command=listbox_tasks.yview)  # iar aici pentru view in directia "y"

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Adauga task", width=48, command=add_task)  # butonul pentru adaugarea task.
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Sterge task", width=48, command=delete_task)  # stergere task
button_delete_task.pack()

button_load_tasks = tkinter.Button(root, text="Incarca tasks", width=48, command=load_tasks)  # butonul pentru inc.task.
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Salveaza tasks", width=48, command=save_tasks)  # butonul pentru s. task.
button_save_tasks.pack()
root.mainloop()
