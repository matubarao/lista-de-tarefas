#Chama a blibioteca tkinter onde posso fazer um front para o py, além de armazenar alguns dados temporarios
import tkinter as tk

#Cria a tela para criar as tarefas
def addtaref():
    tarefa = tk.Toplevel(root)
    
    #Criar uma descrição para as tarefas
    def sub_tarefa():
        desctarefa = textbox_sub.get()
        subtarefas.append(desctarefa)
        textbox_sub.delete(0, tk.END)
    
    #Adiciona a tarefa a lista de tarefas
    def criar_tarefa():
        ntarefas = textbox_tarefa.get()
        listarefa.append({"nome": ntarefas, "subtarefas":subtarefas[:]})
        subtarefas.clear()
        textbox_tarefa.delete(0, tk.END)
   
    #Declara o nome das tarefas    
    tk.Label(tarefa, text="Digite o nome da tarefa").pack()
    textbox_tarefa = tk.Entry(tarefa)
    textbox_tarefa.pack()
    
    tk.Label(tarefa, text="Descrição da tarefa").pack()
    textbox_sub = tk.Entry(tarefa)
    textbox_sub.pack()
    
    tk.Button(tarefa, text="criar subtarefa", command=sub_tarefa).pack()
    tk.Button(tarefa, text="criar terefa", command=criar_tarefa).pack()


#Cria uma analize das tarefas     
def analis_tarefas():
    analizar_tarefas = tk.Toplevel(root)
    for tarefa in listarefa:
        tk.Label(analizar_tarefas, text=tarefa["nome"]).pack()
        for subtarefa_a in tarefa["subtarefas"]:
            tk.Label(analizar_tarefas, text=" - " + subtarefa_a).pack()

#Cria a lista das tarefas que estão sendo adicionadas        
listarefa=[]

#Cria a descrição das tarefas
subtarefas=[]

root = tk.Tk()

#comando para abrir o add tarefas
tk.Button(root, text="Add tarefas", command=addtaref).pack()

#Comando para abrir o analizador de tarefas
tk.Button(root, text="Analisar tarefas", command=analis_tarefas).pack()

#Define o sistema como um sistema de loop permitindo mais que uma ação por acesso
root.mainloop()