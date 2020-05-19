from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
def scrapeInstagram(soup1):
    data = soup1.find(name="meta",attrs={"property":"og:description"})
    data_info = data['content'].split()

    if '"overall_category_name":null,"is_private":true' in get_url.text :
        private_or_not = "Private"
    else:
        private_or_not= "Not Private"
   
    return data_info,private_or_not

def action(account_name):
    username_instagram = account_name.get()
    global get_url
    get_url = requests.get("https://www.instagram.com/"+username_instagram)
    soup1 = BeautifulSoup(get_url.content,"lxml")
    data = scrapeInstagram(soup1)
    
    followers = f"{data[0][0]} Followers"
    following = f"{data[0][2]} Following"
    post = f"{data[0][4]} Posts"
    private_or_not = data[1]
    label([followers,following,post,private_or_not,username_instagram])
    account_name.delete(0,END)
    
def widget():    
    frame_root1 = tk.Frame(root)
    frame_root1.pack()
    frame_root2 = tk.Frame(root)
    frame_root2.pack()
    username_instagram = tk.Entry(frame_root1,insertwidth=5,bd=10,background="cyan",width=20,foreground='darkslategray',font=('arial', 15 , 'bold'),justify="center")
    username_instagram.pack()
    username_instagram.insert(0,"Name User")
    username_instagram.focus_set()
    username_instagram.select_range(0,END)
    
    enter = tk.Button(frame_root2,command=lambda : action(username_instagram),
            text='ENTER',font=('arial',15,'bold'),fg='darkslategray',relief="raised",
            background="cyan",bd=2).pack(side=RIGHT)
    root.bind('<Return>', (lambda button_enter: action(username_instagram)))

    clears = tk.Button(frame_root2,command= clear,
            text='CLEAR',font=('arial',15,'bold'),fg='darkslategray',relief="raised",
            background="cyan",bd=2).pack(side=LEFT)
    root.bind('<Delete>', (lambda button_delete : clear()))

def clear():
    children = root.winfo_children()
    for i in range(2,len(children)):
        children[i].destroy()
def label(textnya):

    frame_awal = tk.Frame(root)
    frame_awal.pack()
    frame_kedua = tk.Frame(root)
    frame_kedua.pack()
    frame_ketiga = tk.Frame(root)
    frame_ketiga.pack()
    frame_keempat = tk.Frame(root)
    frame_keempat.pack()
    frame_kelima = tk.Frame(root)
    frame_kelima.pack()
    username = Label(frame_awal,font=('arial',20),relief="raised",foreground='darkslategray',text="Username : ",background='cyan').pack(side=LEFT)
    label_username = Label(frame_awal,font=('arial',20),relief="raised",foreground='darkslategray',text=textnya[4],background='cyan').pack(side=RIGHT)
    
    follower = Label(frame_kedua,font=('arial',20),relief="raised",foreground='darkslategray',text="Followers : ",background='cyan').pack(side=LEFT)
    label_follower = Label(frame_kedua,text=textnya[0],font=('arial',20),relief="raised",foreground='darkslategray',background='cyan').pack(side=RIGHT)
    
    following = Label(frame_ketiga,font=('arial',20),relief="raised",text="Following : ",foreground='darkslategray',background='cyan').pack(side=LEFT)
    label_following = Label(frame_ketiga,text=textnya[1],font=('arial',20),relief="raised",foreground='darkslategray',background='cyan').pack(side=RIGHT)
   
    post = Label(frame_keempat,font=('arial',20),relief="raised",text="Post : ",foreground='darkslategray',background='cyan').pack(side=LEFT)
    label_post = Label(frame_keempat,text=textnya[2],font=('arial',20),relief="raised",foreground='darkslategray',background='cyan').pack(side=RIGHT)
    
    account_status = Label(frame_kelima,font=('arial',20),relief="raised",text=f"****{textnya[3]}****",foreground='darkslategray',background='cyan').pack()
    

    
    
if __name__ == '__main__':
    root = tk.Tk()
    # root.geometry("250x280")
    root.title("Insta_Info")
    root.config(bg="deepskyblue")
    root.resizable(False,False)
    widget()
    root.mainloop()