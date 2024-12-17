import tkinter
import matplotlib.pyplot as plt

from  matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from email import message
from tkinter import ttk
from  tkinter import messagebox

from matplotlib.pyplot import title

resultlist = []
bmidict = {'underweight': 0, 'normal': 0, 'overweight': 0, 'obese': 0}
def save_data():


    username = enter_name.get()
    userage = enter_age.get()
    userheight=entry_height.get()

    userweight= entry_weight.get()
    if userage =='':
        tkinter.messagebox.showerror(title="Age can not be empty",message="Please enter valid age ")
        return


    if  userheight != '' and userweight != '':
      if int(userheight) <= 0 or int(userweight) <= 0:
            tkinter.messagebox.showerror(title="invalid input", message="Please input valid Height and Weight")
            return


      with open('bmi.txt','a') as bmifile:

             bmifile.write('\n name: '+username+'\n age '+userage+'\n height '+userheight+'\n weight '+userweight)
             tkinter.messagebox.showinfo(title="Saving..",message="Data saved successfully")


    else:
        tkinter.messagebox.showwarning(title="Error,Missing data",message="Enter valid height and weight ")


def load_data():
    userinfolist = []
    with open('bmi.txt', 'r') as bmifile:
        userinfolist = bmifile.read().split()
        print("list is", userinfolist)
    return userinfolist

def calculate_bmi(userinfolist):

    hlist=[]
    wlist=[]
    global resultlist
    for i in range(len(userinfolist)):
        if userinfolist[i]=='height':
            h=userinfolist[i+1]
            h = float(h) * .01
            hlist.append(h)
        elif userinfolist[i]=='weight':
            w=userinfolist[i+1]
            wlist.append(float(w))
    for i in range(len(hlist)):
        b = wlist[i]/ hlist[i] ** 2
        if b < 18.5:
            resultlist.append("underweight")

        elif b < 25:
            resultlist.append("normal")

        elif b < 30:
            resultlist.append("overweight")

        else:
            resultlist.append("obese")

    tkinter.messagebox.showinfo(title="BMI Result",message='Your BMI is ' +str(resultlist[i]))
    return resultlist

def show_graph():
    global bmidict
    bmidict = {'underweight': 0, 'normal': 0, 'overweight': 0, 'obese': 0}


    for result in  resultlist:
       if result=='underweight':
           bmidict['underweight']+=1
       elif result=='normal':
           bmidict['normal'] += 1
       elif result=='overweight':
           bmidict['overweight']+=1
       elif result=='obese':
           bmidict['obese']+=1
    print(bmidict)
    labels=[]
    counts=[]
    for label,count in bmidict.items():
      if count!=0:
        labels.append(label)
        counts.append(count)

    #f, a = plt.subplots()
    #a.pie(counts, labels=labels, autopct='%.0f%%')  # '%1.1f%%' 1 decimal place percentage
    #plt.title('Percentage of the people under each category')
    #plt.show()
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.pie(counts, labels=labels, autopct='%.0f%%')
    ax.set_title('Percentage of People in each BMI Category')

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

window=tkinter.Tk()
window.title("BMI calculator")
frame=tkinter.Frame(window)

frame.pack()
userinfoframe=tkinter.LabelFrame(frame,text="User information")
userinfoframe.grid(row=0,column=0)
user_name=tkinter.Label(userinfoframe,text="Name")
user_name.grid(row=0,column=0)
enter_name=tkinter.Entry(userinfoframe)
enter_name.grid(row=0,column=1)
valueage=list(range(101))

user_age=tkinter.Label(userinfoframe,text="Age")
user_age.grid(row=1,column=0)
enter_age=ttk.Combobox(userinfoframe,values=valueage)
enter_age.grid(row=1,column=1)

user_height=tkinter.Label(userinfoframe,text='Height')
user_height.grid(row=2,column=0)
entry_height=tkinter.Entry(userinfoframe)
entry_height.grid(row=2,column=1)
cm=tkinter.Label(userinfoframe,text="cm")
cm.grid(row=2,column=2)

user_weight=tkinter.Label(userinfoframe,text='Weight')
user_weight.grid(row=3,column=0)
entry_weight=tkinter.Entry(userinfoframe)
entry_weight.grid(row=3,column=1)

kg=tkinter.Label(userinfoframe,text="kg")
kg.grid(row=3,column=2)

save=tkinter.Button(userinfoframe,text='Save',command=save_data)
save.grid(row=4,column=1)

bmiframe=tkinter.LabelFrame(frame,text="BMI")
bmiframe.grid(row=1,column=0)



calculate=tkinter.Button(bmiframe,text='Calculate BMI',command=lambda: calculate_bmi(load_data()))
calculate.grid(row=1,column=1)
showgraph=tkinter.Button(bmiframe,text='Show Graph',command=show_graph)
showgraph.grid(row=1,column=2)

graph_frame = tkinter.Frame(window)
graph_frame.pack()
frame.pack()

window.mainloop()

