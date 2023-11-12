from tkinter import *
from PIL import  ImageTk, Image
from tkinter import ttk
from tkinter import filedialog

root = Tk()
root.title("Tk")
root.geometry("500x500")
root.configure(background="black")

Anna = ImageTk.PhotoImage(Image.open("anna.png" ).resize((300,300)))
Elsa = ImageTk.PhotoImage(Image.open("elsa.png").resize((300,300)))
DonaldDuck = ImageTk.PhotoImage(Image.open("donald.png").resize((300,300)))



label_charicter = Label(root, text="Charicter : ", bg="black")
label_charicter_name = Label(root,font=("courier",18,"bold"),bg="black")
label_charicter_image = Label(root, bg="gold2", highlightthickness=5, borderwidth=2, relief=RAISED)
label_charicter_info = Label(root,font=("courier",10,'bold'), bg="black", wraplength=400)

charicters = ["Anna","Elsa","Donald"]
selectedval = StringVar()
dropdown = ttk.Combobox(root, values = charicters, textvariable=selectedval)

img_path = ""
def RotateImage():
    global img_path 
    img_path = filedialog.askopenfilename(title=" Open Text File", filetypes=[("Image Files","*.jpg *.gif *.jpg *.png *.jpeg")])

    im = Image.open(img_path).resize((300,300)) 
    img = ImageTk.PhotoImage(im.rotate(180))
    label_charicter_image['image']=img
   # img.close()

def PlanetInfo():
    planet = selectedval.get()
    if planet == "Donald":
        label_charicter_name['text'] = "Donald Duck"
        label_charicter_image['image'] = DonaldDuck
      
    elif planet == "Anna":
        label_charicter_name['text'] = "Anna"
        label_charicter_image['image'] = Anna
      
    elif planet == "Elsa":
        label_charicter_name['text'] = "Elsa"
        label_charicter_image['image'] = Elsa
      
        
dropdown.place(relx=0.5, rely=0.1, anchor=CENTER)

    
btn = Button(root,text="Open Image" , command=PlanetInfo)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)

btn2 = Button(root,text="Rotate Image" , command=RotateImage())
btn2.place(relx=0.5, rely=0.9, anchor=CENTER)


label_charicter.place(relx=0.2, rely=0.1 , anchor=CENTER)
label_charicter_name.place(relx=0.5, rely=0.25 , anchor=CENTER)
label_charicter_image.place(relx=0.5, rely=0.5 , anchor=CENTER)
label_charicter_info.place(relx=0.5, rely=0.9 , anchor=CENTER)



root.mainloop()