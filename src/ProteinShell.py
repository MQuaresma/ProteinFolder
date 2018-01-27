# -*- coding:utf-8 -*-
from cmd import Cmd
from ProteinWindow import ProteinWindow
from ProteinEngine import ProteinEngine

class ProteinShell(Cmd):
    intro = 'Protein shell, help or ? for more info'
    prompt = '>> '
                          
    def do_seq(self, arg):
        "- Prints the current sequence if no arguments are given or updates it to the one passed as argument\n"
        try:
            argList = arg.split()
            noArgs = len(argList)
            if noArgs == 0:
                sequence = eng.getseq()
                print("Current sequence:", sequence)
            elif noArgs == 1:
                sequence=eng.do_descompactar(argList[0].upper())
                if eng.valid_seq(sequence):
                    eng.setseq(sequence)
                    print("Sequence updated")
                else:
                    print("Invalid sequence")
            else:
                print("Invalid number of arguments, check usage")
        except BaseException as e:
            print("SEQ command error:" , str(e))
    
    def do_fold(self, arg):
        " - Recieves a string with instructions(F(ront),L(eft),R(ight)) which will be used to fold the sequence\n"
        try:
            argList=arg.split()
            noArgs=len(argList)
            if noArgs==0:
                coords=eng.do_dobrar()
                print("Current coordinates:", coords)
            elif noArgs==1:
                dir=argList[0]
        except BaseException as e:
            print("FOLD command error:" , str(e))

    def do_coords(self, arg):
        " - Prints the current coordinates if no arguments are given or updates them to the ones passed as argument\n"
        try:    
            argList=arg.split()
            noArgs=len(argList)
            if noArgs==0:
                coordinates=eng.getcoord()
                print("Current coordinates: ", coordinates)
            elif noArgs==1:
                coordinates=argList[0]
                if eng.coord_validas(coordinates):
                    eng.setcoord(coordinates)
                    print("Coordinates updated!")
                else:
                    print("The arguments is invalid, please check usage: (x,y),...")
            else:
                print("Invalid number of arguments")
        except BaseException as e:
            print("COORDS command error:", str(e))
            
    def do_check(self, arg):    
        " - Checks if the current configuration(sequence and coordinates) are valid and prints \"YES\" or \"NO\"\n"
        try:
            argList=arg.split()
            noArgs=len(argList)
            if noArgs==0:
                if eng.validate():
                    print('YES')
                else:
                    print ('NO')
            else:
                print("Invalid arguments, please check usage")
        except BaseException as e:
            print("CHECK command error:" , str(e))

    def do_compress(self,arg):    
        " - Comando que deverÃƒÂ¡ imprimir a versÃƒÂ£o mais compactada possÃƒÂ­vel da sequÃƒÂªncia: COMPACTAR  \n"
        try:
            argList = arg.split()
            noArgs =len(argList)
            if noArgs ==0:
                sequence=eng.getseq()
                sequence=eng.compress(sequence)
            elif noArgs==1:
                sequence=argList[0]
                if not eng.validSeq(sequence):
                    raise BaseException("Given sequence is not valid")
            print("Compresssed sequence:", sequence)
        except BaseException as e:
            print("COMPRESS command error:" , str(e))
            
    def do_decompress(self,arg):
        "-Prints the longest possible version of the current or given sequence\n" 
        try:
            argList=arg.split() 
            noArgs=len(argList)
            if noArgs==0:
                sequence=eng.getseq() 
            elif noArgs==1:
                sequence=argList[0]
                if not eng.validSeq(sequence):
                    raise BaseException("Invalid sequence")
            de=eng.decompress(sequence)
            print("Decompressed sequence:", descompactar)
        except BaseException as e:
            print("DECOMPRESS command error:" , str(e))         
    
    def do_save(self, arg):    
        "-Saves current configuration(sequence and coordinates) to specified file\n"
        try:
            argList=arg.split()
            noArgs=len(argList)
            if noArgs==0:
                raise BaseException("No file specified")
            elif noArgs==1:
                eng.saveConfig(arg)
        except BaseException as e:
            print("SAVE command error:" , str(e))

    def do_read(self, arg):        
        "-Reads a configuration(sequence and coordinates) from specified file\n"
        try:
            argList=arg.split()
            noArgs=len(argList)
            if noArgs==0:
                raise BaseException("No file specified")
            elif noArgs==1:
                eng.readConfig(arg)
        except BaseException as e:
            print("READ command error:" , str(e))
            
    def do_energy(self,arg):    
        try: 
            argList=arg.split()
            noArgs=len(argList)
            if(noArgs==0):
                curEnergy=eng.calcEnergy([-1,0,0])
            elif(noArgs==3): 
                energyVal=[]
                for i in argList:
                    energyVal.append(int(i))
                curEnergy=eng.do_energia(energias_lista)
            else:
                raise BaseException("Numero de argumentos invalido")
            print("Current energy: ", curEnergy)
        except BaseException as e:
            print("ENERGY command error:" , str(e))
            
    def do_repair(self, arg):    
        "-Repairs current configuration to a near one if it is invalid\n"
        try:
            eng.repair()
        except BaseException as e:
            print("REPAIR command error:" , str(e))    
    
    def do_localSearch(self, arg):    
        "-Finds a locally lowest energy configuration\n"
        try:
            argList=arg.split()
            noArgs=len(argList)
            if(noArgs==0):
                energyVals=[-1,0,0]
            elif(noArgs==3): 
                energyVals=[]
                for i in argList:
                    energyVals.append(int(i))
            else:
                raise BaseException("Invalid number of arguments")
            eng.localSearch(energyVals)
        except BaseException as e:
            print("LOCALSEARCH command error:" , str(e))
    
    def do_search(self, arg):    
        "-Finds a globally lowest energy configuration possible in the least amount of time possible\n"
        try:
            argList=arg.split()
            noArgs=len(argList)
            if(noArg==0):
                energyVals=[-1,0,0]
            elif(len(argList)==3): 
                energyVals=[]
                for i in argList:
                    energyVals.append(int(i))
            else:
                raise BaseException("Invalid number of arguments")
            eng.globalSearch(energyVals)
        except BaseException as e:
            print("SEARCH command error:" , str(e))

    def do_seeConfig(self, arg):    
        "-See graphical representaion of current configuration\n"
        try:
            if len(eng.getcoord())> 0:
                for line in eng.get_matriz_total():
                    print("%s - (%d,%d)" % (line[0], line[1], line[2]))
                global window
                if window is not None:
                    del window
                cell_size = 50
                window=ProteinWindow(cell_size,eng.max_coord_x(),eng.min_coord_x(),eng.max_coord_y(),eng.min_coord_y()) 
                window.mostraJanela(eng)
            else:
                print('No coordinates found in configuration')
        except BaseException as e:
            print("SEECONFIG command error:", str(e))
    
    def do_exit(self, arg):
        "-Exit utility"
        print('Exiting...')
        return True


if __name__ == '__main__':
    eng=ProteinEngine()
    window=None
    sh=ProteinShell()
    sh.cmdloop()
