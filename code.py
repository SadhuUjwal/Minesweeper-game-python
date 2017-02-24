class Code:
    def __init__(self):
        self.column=0
        self.row=0
        self.rows=[]
        self.index=0
        self.move_str=''
        self.sum=0


    """def matrix(self,m,n):
        self.columns=[]
        self.index=0
        for x in range(0,m):
            row=[]
            for y in range(0,n):
                value=int(input("input value for:"+str(x)+","+str(y)))
                row.append(value)
                self.index+=1
            self.columns.append(row)"""
    def matrix_print(self,m,n):
        for x in range(0,m):
            for y in range(0,n):
                print(self.rows[x][y])
            print("\n")
    def move(self,x,y):
        l=x+1
        m=y+1



        if 0<=x<self.row and 0<=y<self.column:

            if 0<=x<self.row and 0<=y<self.column and 0<=l<self.row and 0<=m<self.column:
                c=1
                r=self.rows[x][y+1]
                b=self.rows[x+1][y]
                d=self.rows[x+1][y+1]
                if r<b :
                    if r<d:
                        self.move_str+='R'

                        self.sum+=r
                        self.move(x,m)


                    else:
                        self.move_str+='D'

                        self.sum+=d
                        self.move(l,m)

                else:
                    if b<d:
                        self.move_str+='B'

                        self.sum+=b
                        self.move(l,y)

                    else:
                        self.move_str+='D'

                        self.sum+=d
                        self.move(l,m)
            elif 0<=x<self.row and 0<=y<self.column and 0<=l<self.row and m>=self.column:
                c=2
                b=self.rows[x+1][y]
                self.move_str+='B'

                self.sum+=b
                self.move(l,y)
            elif 0<=x<self.row and 0<=y<self.column and l>=self.row and 0<=m<self.column:
                c=3
                r=self.rows[x][y+1]
                self.move_str+='R'

                self.sum+=r
                self.move(x,m)

    def sum_moves(self):
        print(self.rows[0][0])
        self.move(0,0)

    def minimumCost(self,input1,input2):

        cols=[]
        c=''

        for i in input1:

            if i.isdigit():
                c+=i

            elif i==',' or input1.endswith(i):
                if c!='':
                    x=int(c)
                    #print(c)

                    cols.append(x)
                    c=''

                c=''


                self.column=len(cols)
                self.rows.append(cols)
                cols=[]
            else:
                if c!='':
                    x=int(c)
                    #print(c)

                    cols.append(x)
                    c=''
        self.sum=self.rows[0][0]
        #self.matrix_print(self.row,self.column)
        self.sum_moves()
        return self.sum,str(self.move_str)






    def start_game(self):
        input1=input("input value rows:")
        self.row=int(input("input value for no rows:"))
        m=self.minimumCost(input1,self.row)
        #self.column=int(input("input value for no cols:"))
        #self.matrix(self.row,self.column)
        #print(self.rows)
        print (m)


game = Code()
game.start_game()

"""



    def minimumCost(input1,input2):"""
