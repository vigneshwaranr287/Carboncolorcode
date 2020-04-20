####This is a GUI based very simple carbon colour code decoder for inductor and
####resistor.This uses Tkinter module of pyhton#################################


from tkinter import *

root=Tk()
root.title("Carbon Color Code Calculator")

Dict1={"Black":0,"Brown":1,"Red":2,"Orange":3,"Yellow":4,"Green":5,"Blue":6,"Violet":7,"Grey":8,"White":9}
Dict2={"Red":2,"Brown":1,"Gold":5,"Silver":10,"None":20}
Dict3={"Silver":-2,"Gold":-1,"Black":0,"Brown":1,"Red":2,"Orange":3,"Yellow":4,"Green":5,"Blue":6}
Dict4={"Red":2,"Brown":1,"Gold":5,"Silver":10,"None":20,"Orange":3,"Yellow":4}

def show():
    list1=[clicked1.get(),clicked2.get(),clicked3.get(),clicked4.get()]
    
    if(clicked.get()==options[0]):
        str1="Resistance:"+str(Dict1[list1[0]])+str(Dict1[list1[1]])+"x10^"+str(Dict1[list1[2]])+"Ohms"
        str2="Tolerance:(+/-)"+str(Dict2[list1[3]])+"%"
        mylabel5.config(text=str1,bg="green",fg="yellow",font=("courier",15))
        mylabel6.config(text=str2,bg="green",fg="yellow",font=("courier",15))
    else:
        str1="Inductance:"+str(Dict1[list1[0]])+str(Dict1[list1[1]])+"x10^"+str(Dict3[list1[2]]-6)+"H"
        str2="Tolerance:(+/-)"+str(Dict4[list1[3]])+"%"
        mylabel5.config(text=str1,bg="green",fg="yellow",font=("courier",15))
        mylabel6.config(text=str2,bg="green",fg="yellow",font=("courier",15))
    mylabel5.grid(column=0,row=7,columnspan=2)
    mylabel6.grid(column=0,row=8,columnspan=2)


def component():
    if(clicked.get()==options[0]):
         options1=["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Grey","White"]
         options2=["Brown","Red","Gold","Silver","None"]
    else:
         options1=["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Grey","White"]
         options3=["Silver","Gold","Black","Brown","Red","Orange","Yellow","Green","Blue"]
         options2=["Brown","Red","Orange","Yellow","Gold","Silver","None"]
    
    clicked1.set(options1[0])
    clicked2.set(options1[0])
    if(clicked.get()==options[0]):
        clicked3.set(options1[0])
    else:
        clicked3.set(options3[0])
    clicked4.set(options2[0])

    mylabel1=Label(root,text="First band:",font=("courier",15))
    mylabel2=Label(root,text="Second band:",font=("courier",15))
    mylabel3=Label(root,text="Third band:",font=("courier",15))
    mylabel4=Label(root,text="Fourth band:",font=("courier",15))



    mylabel1.grid(column=0,row=2)
    mylabel2.grid(column=0,row=3)
    mylabel3.grid(column=0,row=4)
    mylabel4.grid(column=0,row=5)


    drop1=OptionMenu(root,clicked1,*options1)
    drop1.grid(row=2,column=1)
    drop2=OptionMenu(root,clicked2,*options1)
    drop2.grid(row=3,column=1)
    if(clicked.get()==options[0]):
       drop3=OptionMenu(root,clicked3,*options1)
    else:
       drop3=OptionMenu(root,clicked3,*options3)
    drop3.grid(row=4,column=1)
    drop4=OptionMenu(root,clicked4,*options2)
    drop4.grid(row=5,column=1)


    mybutton2=Button(root,text="Enter",command=show)
    mybutton2.grid(column=0,row=6,columnspan=2)



options=["Resistor","Inductor"]
clicked=StringVar()
clicked1=StringVar()
clicked2=StringVar()
clicked3=StringVar()
clicked4=StringVar()
clicked.set(options[0])
mylabel=Label(root,text=" Component:",font=("courier",15))
mylabel5=Label(root)
mylabel6=Label(root)
mylabel.grid(column=0,row=0)
drop=OptionMenu(root,clicked,*options)
drop.grid(row=0,column=1)
mybutton1=Button(root,text="Enter",command=component)
mybutton1.grid(column=0,row=1,columnspan=2)





root.mainloop()
