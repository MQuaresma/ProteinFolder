# -*- coding:utf-8 -*-
from cmd import Cmd
from ProteinWindow import ProteinWindow
from ProteinEngine import ProteinEngine

class ProteinShell(Cmd):
    intro = 'Interpretador de comandos para jogo das proteÃƒÂ­nas. Escrever help ou ? para listar os comandos disponÃƒÂ­veis.\n'
    prompt = 'ProteÃƒÂ­nas> '
                          
    def do_seq(self, arg):
        " - Sem argumentos imprime a sequÃƒÂªncia, se tiver um argumento define a sequÃƒÂªncia constituÃƒÂ­da por A's e B's: SEQ sequÃƒÂªncia \n"
        try:
            lista_arg = arg.split()
            num_args = len(lista_arg)
            if num_args == 0:
                sequencia = eng.getseq()
                print("SEQ: ", sequencia)
            elif num_args == 1:
                sequencia = eng.do_descompactar(lista_arg[0].upper())
                if eng.seq_valida(sequencia):
                    eng.setseq(sequencia)
                    print("A sequÃƒÂªncia foi atualizada")
                else:
                    print("A sequÃƒÂªncia tem carateres invÃƒÂ¡lidos, sÃƒÂ³ ÃƒÂ© permitido o A e o B")
            else:
                print("NÃƒÂºmero de argumentos invÃƒÂ¡lido!")
        except BaseException as e:
            print("Erro: ao executar o comando SEQ:" , str(e))
    
    def do_dobrar(self, arg):
        " - Comando que recebe como argumento uma string com instruÃƒÂ§ÃƒÂµes (FED) que serÃƒÂ£o utilizadas para dobrar a sequÃƒÂªncia: DOBRAR instruÃƒÂ§ÃƒÂµes \n"
        try:
            lista_arg=arg.split()
            num_args=len(lista_arg)
            if num_args==0:
                dobrar_1= eng.do_dobrar()
                print("Coordenadas:", dobrar_1)
            elif num_args==1:
                dobrar=lista_arg[0]
                dobrar_1=eng.do_dobrar(dobrar)
                print("Coordenadas:", dobrar_1)
        except BaseException as e:
            print("Erro: ao executar o comando DOBRAR:" , str(e))

    def do_coords(self, arg):
        " - Sem argumentos imprime as coordenadas de cada caratere da sequÃƒÂªncia, se tiver um argumento define a posiÃƒÂ§ÃƒÂ£o (X,Y) de cada caratere da sequÃƒÂªncia: COORDS posiÃƒÂ§ÃƒÂµes \n"
        try:    
            lista_arg = arg.split()
            num_args = len(lista_arg)
            if num_args == 0:
                coordenadas = eng.getcoord()
                print("COORDENADAS: ", coordenadas)
            elif num_args == 1:
                coordenadas = lista_arg[0]
                if eng.coord_validas(coordenadas):
                    eng.setcoord(coordenadas)
                    print("As coordenadas foram atualizadas")
                else:
                    print("A string de coordenadas tem carateres invÃƒÂ¡lidos, o formato ÃƒÂ© (x,y)...")
            else:
                print("NÃƒÂºmero de argumentos invÃƒÂ¡lido!")
        except BaseException as e:
            print("Erro: ao fazer o COORDS:", str(e))
            
    def do_validar(self, arg):    
        " - Comando que valida a configuraÃƒÂ§ÃƒÂ£o atual da proteÃƒÂ­na; este comando deverÃƒÂ¡ imprimir as palavras SIM ou NAO caso a configuraÃƒÂ§ÃƒÂ£o seja vÃƒÂ¡lida: VALIDAR \n"
        try:
            lista_arg = arg.split()
            num_args =len(lista_arg)
            if num_args ==0:
                validar=eng.do_validar()
                if validar:
                    print('Sequencia valida')
                else:
                    print ('Sequencia invÃ¡lida')
            else:
                print("NÃƒÂºmero de argumentos invÃƒÂ¡lido!")
        except BaseException as e:
            print("Erro: ao executar o VALIDAR:" , str(e))

    def do_compactar(self,arg):    
        " - Comando que deverÃƒÂ¡ imprimir a versÃƒÂ£o mais compactada possÃƒÂ­vel da sequÃƒÂªncia: COMPACTAR  \n"
        try:
            lista_arg = arg.split()
            num_args =len(lista_arg)
            if num_args ==0:
                sequencia=eng.getseq()
                compactar= eng.do_compactar(sequencia)
                print("COMPACTAR:", compactar)
            elif num_args==1:
                compactar = lista_arg[0]
                if eng.do_validar(compactar):
                    print ("Proteina compactada")
                else:
                    raise BaseException("A proteina nao e valida")
        except BaseException as e:
            print("Erro: ao executar o comando COMPACTAR:" , str(e))
            
    def do_descompactar(self,arg):
        "-Comando que devera imprimir a versao mais distendida possivel da sequencia: DESCOMPACTAR \n" 
        try:
            lista_arg = arg.split() 
            num_args = len(lista_arg)
            if num_args==0:
                sequencia=eng.getseq() 
            elif num_args==1:
                sequencia=lista_arg[0]
                if not eng.seq_valida(sequencia):
                    raise BaseException("A proteina nao e valida")
            descompactar=eng.do_descompactar(sequencia)
            print("DESCOMPACTAR:", descompactar)
        except BaseException as e:
            print("Erro: ao executar o comando DESCOMPACTAR:" , str(e))         
    
    def do_gravar(self, arg):    
        " - Comando invocado com um argumento que serÃƒÆ’Ã‚Â¡ o nome de um ficheiro onde a aplicaÃƒÆ’Ã‚Â§ÃƒÆ’Ã‚Â£o deverÃƒÆ’Ã‚Â¡ armazenar a sequÃƒÆ’Ã‚Âªncia e as coordenadas: GRAVAR nomef.txt \n"
        try:
            lista_arg=arg.split()
            num_args=len(lista_arg)
            if num_args==0:
                print ("E necessario um nome para o ficheiro")
            elif num_args==1:
                eng.do_gravar(arg)
        except BaseException as e:
            print("Erro: ao executar o comando GRAVAR:" , str(e))

    def do_ler(self, arg):        
        " - Comando invocado com um argumento que serÃƒÂ¡ o nome de um ficheiro de onde a aplicaÃƒÂ§ÃƒÂ£o deverÃƒÂ¡ ler a sequÃƒÂªncia e as coordenadas: LER nomef.txt \n"
        try:
            lista_arg=arg.split()
            num_args=len(lista_arg)
            if num_args==0:
                print ("E necessario um nome para o ficheiro")
            elif num_args==1:
                eng.do_ler(arg)
        except BaseException as e:
            print("Erro: ao executar o comando LER:" , str(e))
            
    def do_energia(self,arg):    
        try: 
            argList=arg.split()
            if(len(argList)==0):
                energia_e = eng.do_energia([-1,0,0])
            elif(len(argList)==3): 
                energias_lista=[]
                for i in argList:
                    energias_lista.append(int(i))
                energia_e=eng.do_energia(energias_lista)
            else:
                raise BaseException("Numero de argumentos invalido")
            print("ENERGIA: ", energia_e)
        except BaseException as e:
            print("Erro: ao executar o comando SEQ:" , str(e))
            
    def do_reparar(self, arg):    
        " - Comando que deverÃƒÂ¡ reparar uma configuraÃƒÂ§ÃƒÂ£o caso esta seja invÃƒÂ¡lida achando a configuraÃƒÂ§ÃƒÂ£o mais prÃƒÂ³xima que seja vÃƒÂ¡lida: REPARAR \n"
        try:
            reparar_1=eng.do_reparar()
            print("REPARAR:", reparar_1)
        except BaseException as e:
            print("Erro: ao executar o comando REPARAR:" , str(e))    
    
    def do_proclocal(self, arg):    
        " - Comando que deverÃƒÂ¡ encontrar uma configuraÃƒÂ§ÃƒÂ£o vizinha da configuraÃƒÂ§ÃƒÂ£o atual com energia mais baixa: PROCLOCAL \n"
        try:
            argList=arg.split()
            if(len(argList)==0):
                energia_e = eng.do_energia([-1,0,0])
            elif(len(argList)==3): 
                energias_lista=[]
                for i in argList:
                    energias_lista.append(int(i))
                energia_e=eng.do_proclocal(energias_lista)
            else:
                raise BaseException("Numero de argumentos invalido")
            print("ENERGIA: ", energia_e)
        except BaseException as e:
            print("Erro: ao executar o comando SEQ:" , str(e))
    
    def do_procurar(self, arg):    
        " - Comando que deverÃƒÂ¡ encontrar a melhor configuraÃƒÂ§ÃƒÂ£o possÃƒÂ­vel (i.e., a configuraÃƒÂ§ÃƒÂ£o com energia mais baixa) num espaÃƒÂ§o de tempo aceitÃƒÂ¡vel: PROCURAR \n"
        try:
            argList=arg.split()
            if(len(argList)==0):
                energia_e = eng.do_energia([-1,0,0])
            elif(len(argList)==3): 
                energias_lista=[]
                for i in argList:
                    energias_lista.append(int(i))
                energia_e=eng.do_procurar(energias_lista)
            else:
                raise BaseException("Numero de argumentos invalido")
            print("PROCURAR: ", energia_e)
        except BaseException as e:
            print("Erro: ao executar o comando PROCURA:" , str(e))

    def do_ver(self, arg):    
        " - Comando para visualizar graficamente a configuraÃƒÂ§ÃƒÂ£o atual caso seja vÃƒÂ¡lida: VER  \n"
        try:
            if len(eng.getcoord()) > 0:
                for linha in eng.get_matriz_total():
                    print("%s - (%d,%d)" % (linha[0], linha[1], linha[2]))
                global janela
                if janela is not None:
                    del janela
                cell_size = 50
                janela = ProteinWindow(cell_size, eng.max_coord_x(), eng.min_coord_x(), eng.max_coord_y(), eng.min_coord_y()) 
                janela.mostraJanela(eng)
            else:
                print('AtenÃƒÂ§ÃƒÂ£o: a lista de coordenadas estÃƒÂ¡ vazia!')
        except BaseException as e:
            print("Erro: ao mostrar a janela com o estado da sequÃƒÂªncia (grÃƒÂ¡fica):", str(e))
    
    def do_sair(self, arg):
        "Sair do programa ProteÃƒÂ­nas: sair"
        print('Obrigado por ter utilizado o ProteÃƒÂ­nas, espero que tenha sido ÃƒÂºtil!')
        return True


if __name__ == '__main__':
    eng = ProteinEngine()
    janela = None
    sh = ProteinShell()
    sh.cmdloop()
