from tkinter import *
import tkinter.messagebox
import random

class MineGUI:
    def __init__(self):
        self.counter = 0
        self.count=0
        self.visited=[]
        self.full=[]
        self.won=[]
        self.flag_list=[]
        self.root = Tk()
        self.frame = Frame(self.root)
        self.frame.pack(fill="both", expand=True)
        self.label = Label(self.frame, text='Game', height=3, bg='white', fg='blue')
        self.label.pack(fill="both", expand=True)
        self.canvas1 = Canvas(self.frame, width=400, height=100)
        self.canvas1.pack(fill="both", expand=True)
        self.photo_ng = PhotoImage(file="new_game_button.png")
        self.butt = PhotoImage(file="button.png")
        self.mine_flag = PhotoImage(file="flag.png")
        self.photo_nul = PhotoImage(file="button.png")
        self.mine_badflag = PhotoImage(file="mine_bad_flag.png")
        self.mine_gudflag = PhotoImage(file="mine.png")
        self.photo_l = PhotoImage(file="lost.png")
        self.photo_w = PhotoImage(file="won.png")

        self.but=Button(self.canvas1,command=self.start_gui,image=self.photo_ng)
        self.but.pack()
        self.canvas = Canvas(self.frame, width=400, height=300)
        self.canvas.pack(fill="both", expand=True)
        self.mine=0

#creates buttons form 0 to 81 in rows and columns
    def create_buttons(self):
        self.buttons = []
        self.index=0
        a=0
        for y in range(9):
            row = []
            for x in range(9):
                self.full.append(self.index)
                self.button = Button(self.canvas,name=str(self.index) , text='      ',command=lambda i=self.index :self.clicked(i))


                self.button.bind("<ButtonPress-3>",lambda evt,i=self.index :self.flag(i))
                self.button.grid(column=x, row=y)
                row.append(self.button)
                self.index+=1;
                a+=1
            self.buttons.append(row)

# create 10 random mines
    def mines(self):
        self.mine=random.sample(range(0,81), 10)
        for i in range(10):
            print (self.mine[i])

#flag creating  and removing at max 10 flags are allowed
    def flag(self,n):
        i=n
        y=int(i/9)
        x=int(i%9)
        self.button=self.buttons[y][x]
        if n not in self.flag_list :

            print(self.count)
            if self.count<10:
                self.count+=1
                self.flag_list.append(n)
                self.button['image'] = self.mine_flag

        else:

            print(self.count)
            self.count-=1
            if self.count<=10:

                self.flag_list.remove(n)
                self.button['image'] = ''


#gives the value of the clicked button and determines if game won or lost
    def clicked(self,n):
        print("clicked=",n)

        self.won=list(set(self.full).difference(set(self.mine)))
        bcount=int(self.button_value(n))

        #if clicked on mine
        if n in self.mine and n not in self.flag_list:
            self.but['image']=self.photo_l
            tkinter.messagebox.showinfo("Lost","Player Lost..!! Better Luck Next Time")
            for i in range(0,10):
                m=self.mine[i]
                y=int(self.mine[i]/9)
                x=int(self.mine[i]%9)
                self.button=self.buttons[y][x]
                if m in self.flag_list:
                    self.button['image']=self.mine_gudflag
                else:
                    self.button['image'] = self.mine_badflag

        #if clicked on null value
        elif bcount==0 and n not in self.flag_list and n not in self.visited:
            self.visited.append(n)
            self.button['image']=self.photo_nul
            b=self.sub_but_set(n)

            for k in range(len(b)):
                if b[k] not in self.visited and 0<=b[k]<81 :
                    self.clicked(b[k])
            print(self.won)
            self.won.sort();
            self.visited.sort();
            if self.visited==self.won:

                self.but['image']=self.photo_w
                tkinter.messagebox.showinfo("won","Congratulations Player Won")

        #if clicked on a cell with value
        elif bcount>0 and n not in self.flag_list and n not in self.visited:
            self.visited.append(n)
            self.button['text'] ='  '+ str(bcount)+' '
            self.won.sort();
            self.visited.sort();
            if self.visited==self.won:
                #self.photo_w = PhotoImage(file="C:\\Users\\ujwal\\Downloads\\won.png")
                self.but['image']=self.photo_w
                tkinter.messagebox.showinfo("Won","Congratulations Player Won")
# finding the sorrounding cells of a pirticular cell
    def sub_but_set(self,i):
        if i%9==0 and i!=0 and i!=72:
            return [i+1,i+9,i-9,i+10,i-8]
        elif i/9==0 and i!=0 and i!=8:
            return [i+1,i-1,i+9,i+10,i+8]
        elif i%9==8 and i!=8 and i!=80:
            return [i-1,i+9,i-9,i-10,i+8]
        elif i/9==8 and i!=80 and i!=72:
            return [i+1,i-1,i-9,i-10,i-8]
        elif i==0:
            return [i+1,1+9,i+10]
        elif i==80:
            return [i-1,i-9,i-10]
        elif i==8:
            return [i-1,i+8,i+9]
        elif i==72:
            return [i-9,i-8,i+1]
        else:
            return [i+1,i-1,i+9,i-9,i+10,i-10,i+8,i-8]
# finding the value of a button
    def button_value(self,bno):
        m=[]
        for i in range(10):
            m.append(self.mine[i])
        i=bno
        b=self.sub_but_set(i)
        y=int(i/9)
        x=int(i%9)
        leng=len(b)
        count=0
        self.button=self.buttons[y][x]
        if i not in m:

            for trav in range(len(b)):
                if 0<=b[trav]<81 :
                    print(b[trav])

                    if b[trav] in m:
                        count+=1
        return count


    def start_game(self):
        #list([self.buttons.pop() for i in range(len(self.buttons)) ])
        list([self.visited.pop() for i in range(len(self.visited)) ])
        list([self.flag_list.pop() for i in range(len(self.flag_list)) ])
        list([self.won.pop() for i in range(len(self.won)) ])
        list([self.full.pop() for i in range(len(self.full)) ])
        self.counter = 0
        self.count=0
        self.canvas.delete(ALL)
        self.create_buttons()
        self.mines()
        #self.canvas.create_rectangle(0,0,300,300, outline="black")
        #self.canvas.bind("<ButtonPress-1>", self.player_click)
        self.root.mainloop()
    def start_gui(self):
        #self.photo_ng = PhotoImage(file="C:\\Users\\ujwal\\Downloads\\new_game_button.png")
        self.but['image']=self.photo_ng
        self.canvas.delete(ALL)
        self.start_game()
game = MineGUI()
game.start_gui()