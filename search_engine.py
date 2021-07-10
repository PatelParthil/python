from tkinter import *
import webbrowser
def serach_google(self):
    textin = entry_1.get()
    webbrowser.get().open("http://www.google.com/search?q="+textin)
def search_wiki(self):
    textin = entry_1.get()
    webbrowser.get().open("https://www.wikipedia.org/wiki/"+textin)
def search_yahho(self):
    textin = entry_1.get()
    webbrowser.get().open("https://in.search.yahoo.com//search?q="+textin)
root=Tk()
root.geometry('300x250')
root.title("Search engine")
lable_1=Label(root,text="Search here:",font='calibri')
lable_1.place(x=20,y=50)
entry_1=Entry(root,font='calibri')
entry_1.place(x=110,y=50)
button_1=Button(root,text="Google",bg='white',relief="groove",font='calibri',command=root.destroy)
button_1.place(x=50,y=110)
button_1.bind('<Button-1>',serach_google)
button_2=Button(root,text="Wikipedia",bg="white",relief="groove",font='calibri',command=root.destroy)
button_2.place(x=116,y=110)
button_2.bind('<Button-1>',search_wiki)
button_3=Button(root,text="Yahho",bg="white",relief="groove",font='calibri',command=root.destroy)
button_3.place(x=200,y=110)
button_3.bind('<Button-1>',search_yahho)
root.mainloop() 