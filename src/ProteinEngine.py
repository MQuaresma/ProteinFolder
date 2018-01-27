# -*- coding:utf-8 -*-
class ProteinEngine:
    
    def __init__(self, seq=""):
        self.sequence = seq
        self.coordinates = []
        pass
    
    def getseq(self):
        return self.sequence  
    
    def setseq(self, seq):
        self.sequence = seq
        
    def validSeq(self, seq_a_verificar):
        car_validos = "AB()123456789"
        car_obrigatorios="AB" 
        min_car=False
        for car in seq_a_verificar:
            min_car=min_car or (car in car_obrigatorios)
            if car not in car_validos:
                return False
        return True and min_car

    def convert_coords_to_list_of_list(self, coords):
        coords = coords.replace(")(", ");(")
        L = coords.split(";")
        Lista_coords = []
        for c in L:
            li = c.strip("()").split(",")
            cc = []
            for t in li:
                cc.append(int(t))
            Lista_coords.append(cc)
        return Lista_coords

    def convert_list_of_list_to_coords(self, lista_coords):
        coords = ""
        for c in lista_coords:
            coords = coords + "(%d,%d)" % (c[0], c[1])
        return coords

    def getcoord(self):
        return self.convert_list_of_list_to_coords(self.coordinates)  
    
    def setcoord(self, coord):
        self.coordinates = self.convert_coords_to_list_of_list(coord)
        
    def coord_validas(self, coord_a_verificar):
        car_validos = "()0123456789,-"
        for car in coord_a_verificar:
            if car not in car_validos:
                return False
        return True

    def max_coord_x(self):
        maximo = 0
        for c in self.coordinates: 
            if c[0] > maximo:
                maximo = c[0]
        return maximo

    def min_coord_x(self):
        minimo = 0
        for c in self.coordinates: 
            if c[0] < minimo:
                minimo = c[0]
        return minimo

    def max_coord_y(self):
        maximo = 0
        for c in self.coordinates: 
            if c[1] > maximo:
                maximo = c[1]
        return maximo

    def min_coord_y(self):
        minimo = 0
        for c in self.coordinates: 
            if c[1] < minimo:
                minimo = c[1]
        return minimo
    
    def get_matriz_total(self):
        Matriz = []
        for i in range(len(self.sequence)):
            lin = []
            lin.append(self.sequence[i])
            lin.append(self.coordinates[i][0])
            lin.append(self.coordinates[i][1])
            Matriz.append(lin)
        return Matriz
    
    #TODO 
    #def fold(self,arg):

    def validate(self):
        L1=self.coordinates
        ort=True
        sobreposed=False
        i=0
        while i<len(L1)-1 and (not sobreposed) and ort:
            j=i+1
            ort=L1[i][0]==L1[i+1][0] or L1[i][1]==L1[i+1][1]
            while j<len(L1) and sobreposed and ort:
                sobreposed= (L1[i][0]==L1[j][0] and L1[i][1]==L1[j][1])
                j+=1
            i+=1
        return (ort and (not sobreposed))
    
    def compress(self, arg):
        comp=''
        pd1="AB" 
        pd2="BA"
        i=0
        while i<len(arg):
            c1=0
            c2=0
            c=1
            j=i
            while j<len(arg)-2 and arg[j:j+2]==pd1:
                c1+=1
                j+=2
            while j<len(arg)-2 and c1==0 and arg[j:j+2]==pd2:
                c2+=1
                j+=2
            while i<len(arg)-1 and c1==0 and c2==0 and arg[i]==arg[i+1]:
                c+=1
                i+=1
            if c1>1:
                comp+='('+ pd1 + ')' + str(c1)
                i=j
            elif c2>1:
                comp+='('+ pd2 + ')' + str(c2)
                i=j
            elif c>1:
                comp+= arg[i] + str(c)
                i+=1
            else:
                comp+= arg[i]
                i+=1
        return comp
    
    
    def decompress(self,arg):
        desc=''
        temp=''
        i=0
        while i<len(arg): 
            if arg[i]=='(':
                i+=1
                temp=arg[i:i+2]
                i+=3
            else:
                temp=arg[i]
                i+=1    
            j=1        
            while i+j<=len(arg) and arg[i:i+j].isdigit():
                    j+=1
            if j>1:
                a=int(arg[i:i+j-1])
                desc+=a*temp
                i+=j-1 
            else:
                desc+=temp
        return desc


    def saveConfig(self, arg):
        myfile=open(arg,'w') 
        myfile.write(self.getseq()+'\n'+self.getcoord())
        myfile.close()
        
    def readConfig(self, arg):
        myfile=open(arg, 'r')
        seq=myfile.readline()
        coords=myfile.readline()
        self.setseq(seq[0:len(seq)-1])
        self.setcoord(coords)
        myfile.close()

    #TODO
    #def calcEnergy(self, arg):
          
    def localSearch(self,arg):
        board=self.genBoard()
        for i in range(1,len(self.coordinates)): 
            self.procCoord(i,board,arg)
                             
    def procCoord(self,aminoIndice, board,arg):
        coordenadas=self.coordinates
        if aminoIndice>=1 and aminoIndice<len(self.coordinates)-1:
            before=coordenadas[aminoIndice-1]
            after=coordenadas[aminoIndice+1]
        else:
            before=after=coordenadas[aminoIndice-1]
        curPos=coordenadas[aminoIndice]
        curEnergy=self.calcLocalEnergy(arg,before,curPos,after,board)
        l1=self.posicoesPossiveis(antes)
        l2=self.posicoesPossiveis(depois)
        pos=self.intersection(l1,l2)
        pos.remove(curPos)
        for tempCoords in pos:
            tempEnergy=self.calcLocalEnergy(arg,tempCoords,board)
            if tempEnergy>curEnergy:
                self.coordinates[aminoIndice]=tempCoords
            else:
                curPos=tempCoords
                curEnergy=tempEnergy

    def calcLocalEnergy(self,arg,before,cur,after,board):
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        sPositions=[]
        for dir in direcions:
            tempPos=[x+y for (x,y) in zip(cur,dir)]
            if tempPos not in [before,after] and tempPos in self.coordinates:
                sPositions.append(tempPos)
        for amino in sPositions:
            if self.seq 

    def posicoesPossiveis(self,coord): 
        coordenadas=self.coordinates
        direcoes=[[1,0],[-1,0],[0,1],[0,-1]]
        posExistentes=[]
        for dir in direcoes:
            tempPos=[x+y for (x,y) in zip(coord,dir)]
            if tempPos not in coordenadas:
                posExistentes.append(tempPos)
        return posExistentes

    def intersection(self,l1,l2):
        res=[]
        for i in l1:
            if i in l2:
                res.append(i)
        return res

    def genBoard(self):
        col=2*max(self.max_coord_x(),abs(self.min_coord_x()))+2
        lin=2*max(self.max_coord_y(),abs(self.min_coord_y()))+2
        origemY=lin/2
        origemX=col/2
        coordProteina=self.get_matriz_total()
        board=[]
        for i in range(lin):
            temp=[]
            for j in range(col):
                temp.append('o')
            board.append(temp)
        for i in range(len(coordProteina)):
            amino=coordProteina[i][0]
            x=origemX+coordProteina[i][1]
            y=origemY+coordProteina[i][2]
            board[y][x]=amino
        return board
                       
    def globalSearch(self,arg):
        maxIter=len(self.sequence)
        energiaDiminui=True
        energiaLast=self.do_energia(arg)
        energiaTemp=0
        i=0
        while i<maxIter:
            self.do_proclocal(arg)
            energiaTemp=self.do_energia(arg)
            if energiaTemp<energiaLast:
                energiaLast=energiaTemp
                i=0
            else:
                i+=1

    #TODO
    #def repair(self):
