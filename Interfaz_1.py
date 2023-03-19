from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.geometry("600x450")

noteBook = ttk.Notebook(raiz)
tabADD = ttk.Frame(noteBook)
tabDelete = ttk.Frame(noteBook)
tabSearch = ttk.Frame(noteBook)
tabService = ttk.Frame(noteBook)
tabHelp = ttk.Frame(noteBook)
FirstName = StringVar()
LastName = StringVar()
Country = StringVar()
Dia = IntVar()
Mes = StringVar()
Año = IntVar()
Credit = IntVar()
Days = IntVar()

style = ttk.Style()
style.theme_create("MyStyle", parent="alt", settings={
    "TNotebook.Tab": 
        {"configure": {"background": "deep sky blue", "foreground": "black"},
        "map": {"background": [("selected", "deep sky blue")]}}
})
style.theme_use("MyStyle")

noteBook.pack_configure(expand=True, fill="both")

noteBook.add(tabADD, text="                 Add                ")
noteBook.add(tabDelete, text="                 Delete             ")
noteBook.add(tabSearch, text="             Search                 ")
noteBook.add(tabService, text="                Service                ")
noteBook.add(tabHelp, text="                   Help                   ")

MainFrame = ttk.Frame(tabADD, padding="5 5 5 5")
MainFrame.grid(column=0, row= 0)
SecondFrame = ttk.Frame(MainFrame, padding="40 30 40 30", relief="raised")
SecondFrame.grid(column=0, row=1)
ThirdFrame = ttk.Frame(SecondFrame)
ThirdFrame.grid(column=1, row=1, sticky=(W), padx=5, pady=5)
FourthFrame = ttk.Frame(MainFrame, padding="40 30 202 30", relief="raised")
FourthFrame.grid(column=0, row=2, sticky=(W))
FifthFrame = ttk.Frame(MainFrame, padding="40 30 165 30", relief="raised")
FifthFrame.grid(column=0, row=3, sticky=(W))
SixthFrame = ttk.Frame(MainFrame, padding="275 30 275 30")
SixthFrame.grid(column=0, row=4, sticky=(W))

ttk.Radiobutton(FourthFrame, text="Visa").grid(column=1, row=1, sticky=(W), pady=2, padx=15)
ttk.Radiobutton(FourthFrame, text="MasterCard").grid(column=1, row=1, sticky=(W), pady=2 ,padx=65)
ttk.Radiobutton(FifthFrame, text="Normal").grid(column=1, row=0, sticky=(W), padx=5)
ttk.Radiobutton(FifthFrame, text="Familiar").grid(column=1, row=1, sticky=(W), padx=5)
ttk.Radiobutton(FifthFrame, text="Especial").grid(column=1, row=2, sticky=(W), padx=5)
SubmitBoton = ttk.Button(SixthFrame, text= "Submit").grid(column=2, row=4, sticky=(S))

ttk.Label(SecondFrame, text="First Name: ").grid(column=0, row=0,sticky=(W))
ttk.Label(SecondFrame, text="Last Name: ").grid(column=2, row=0,sticky=(W),padx=5)
ttk.Label(SecondFrame, text="Birth Date ").grid(column=0, row=1, sticky=(W))
ttk.Label(SecondFrame, text="Country: ").grid(column=2, row=1, sticky=(W), padx=5)
ttk.Label(FourthFrame, text="Credir Card (if any): ").grid(column=0,row=0,sticky=(W))
ttk.Label(FourthFrame, text="Type Credit Card (if any): ").grid(column=0, row=1,sticky=(W), pady=2)
ttk.Label(FifthFrame, text="RoomType: ").grid(column=0, row=0, sticky=(W))
ttk.Label(FifthFrame, text="Total Staying Time (days): ").grid(column=3, row=0,sticky=(W), padx=20)

FirstNameEntry = ttk.Entry(SecondFrame, textvariable=FirstName, width=25).grid(column=1, row=0, sticky=(W),padx=5)
LastNameEntry = ttk.Entry(SecondFrame, textvariable=LastName, width=25).grid(column=3, row=0, sticky=(W),padx=5)
CountryEntry = ttk.Entry(SecondFrame,textvariable=Country, width=20).grid(column=3, row=1, sticky=(W))
CreditEntry = ttk.Entry(FourthFrame, textvariable=Credit, width=25).grid(column=1, row=0, sticky=(W),padx=5)
CreditEntry = ttk.Entry(FifthFrame,textvariable= Days, width=10).grid(column=4, row=0)
DiaBox = ttk.Combobox(ThirdFrame, textvariable=Dia, width=3)
DiaBox.grid(column=0, row=0, sticky=(W), pady=10)
MesBox = ttk.Combobox(ThirdFrame, textvariable=Mes, width=3)
MesBox.grid(column=1, row=0, sticky=(W), padx=2, pady=10)
AñoBox = ttk.Combobox(ThirdFrame, textvariable=Año, width=3)
AñoBox.grid(column=2, row= 0,sticky=(W), padx=2, pady=10)


raiz.mainloop()