# -*- coding:utf-8 -*-
'''
Created on 31/10/2017

@author: victor Alves
'''

from graphics import *

class ProteinWindow:
    
    '''
    Classe que cria uma janela para vizualização grafica do estado da sequencia
    '''
    def __init__(self, cell_size, max_x, min_x, max_y, min_y):
        '''
        Cria nova instancia da  ProteinasWindow
        :param cell_size: tamanho da casa no ecra, em pixeis
        :param linhas: numero de linhas
        :param colunas: numero de colunas
        '''
        self.cell_size = cell_size
        self.max_cood_x = max_x
        self.min_cood_x = min_x
        self.max_cood_y = max_y
        self.min_cood_y = min_y
        self.nlinhas = max_y - min_y + 1
        self.ncolunas = max_x - min_x + 1
        self.janela = GraphWin("Proteinas", self.ncolunas * self.cell_size + self.cell_size, self.nlinhas * self.cell_size + self.cell_size)


   
    def __del__(self):
        self.janela.close()  # fechar a janela
                
    def desenhaLinha(self, x1, y1, x2, y2, espessura, cor):
        '''
        Desenha uma linha
        :param x1: (x1,y1)
        :param y1: (x1,y1)
        :param x2: (x2,y2)
        :param x2: (x2,y2)
        '''    
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        l = Line(p1, p2)
        l.setFill(cor)
        l.setWidth(espessura)
        l.draw(self.janela)
     
    
    def desenhaNumsColunas(self):
        '''
        Desenha os numeros das colunas e as linhas verticais da grelha
        ''' 
        coluna = self.min_cood_x
        for i in range(1, self.max_cood_x - self.min_cood_x + 2):
            px = i * self.cell_size + self.cell_size / 2
            py = self.cell_size / 2
            label = Text(Point(px, py), str(coluna))
            label.setTextColor("black")
            label.draw(self.janela)
            p1y = self.cell_size 
            p2y = p1y + self.nlinhas * self.cell_size
            self.desenhaLinha(px, p1y, px, p2y, 1, "black")
            coluna += 1
    
    def desenhaNumsLinhas(self):
        '''
        Desenha os numeros das linhas e as linhas horizontais da grelha
        ''' 
        linha = self.min_cood_y
        for i in range(1, self.max_cood_y - self.min_cood_y + 2):
            px = self.cell_size / 2
            py = i * self.cell_size + self.cell_size / 2
            label = Text(Point(px, py), str(linha))
            label.setTextColor("black")
            label.draw(self.janela)
            p1x = self.cell_size 
            p2x = p1x + self.ncolunas * self.cell_size
            self.desenhaLinha(p1x, py, p2x, py, 1, "black")
            linha += 1
                    
    def desenhaAB(self, coluna, linha, tipo):
        '''
        Desenha o A ou B na grelha 
        :param coluna: indice da coluna coordenada x da proteina
        :param linha: indice da linha coordenada y da proteina
        :param tipo: Tipo de carater a desenhar - A ou B 
        '''
        col = coluna + 1 - self.min_cood_x  # para mudar para a escala da grelha em que o (1,1) é a posição do canto superior esquerdo
        lin = linha + 1 - self.min_cood_y  # para mudar para a escala da grelha em que o (1,1) é a posição do canto superior esquerdo
        px = col * self.cell_size + self.cell_size / 2  # calculo do x do pixel
        py = lin * self.cell_size + self.cell_size / 2  # calculo do x do pixel
        p1 = Point(px, py)
        c = Circle(p1, self.cell_size / 4)
        if tipo == "A":
            c.setFill("yellow")
        elif tipo == "B":
            c.setFill("red")
        c.draw(self.janela)
                    
    def desenhaLigacao(self, coluna1, linha1, coluna2, linha2):  # coordenadas da proteina
        '''
        Desenha uma ligação entre dois carateres na grelha 
        :param coluna1: indice da coluna coordenada x do caratere da proteina
        :param linha1: indice da linha coordenada y da caratere da proteina
        :param coluna2: indice da coluna coordenada x da caratere da proteina
        :param linha2: indice da linha coordenada y da caratere da proteina
        '''
        col1 = coluna1 + 1 - self.min_cood_x  # para mudar para a escala da grelha em que o (1,1) é a posição do canto superior esquerdo
        lin1 = linha1 + 1 - self.min_cood_y  # para mudar para a escala da grelha em que o (1,1) é a posição do canto superior esquerdo
        col2 = coluna2 + 1 - self.min_cood_x  # para mudar para a escala da grelha em que o (1,1) é a posição do canto superior esquerdo
        lin2 = linha2 + 1 - self.min_cood_y  # para mudar para a escala da grelha em que o (1,1) é a posição do canto superior esquerdo
        p1x = col1 * self.cell_size + self.cell_size / 2  # calculo do x do pixel
        p1y = lin1 * self.cell_size + self.cell_size / 2  # calculo do y do pixel
        p2x = col2 * self.cell_size + self.cell_size / 2  # calculo do x do pixel
        p2y = lin2 * self.cell_size + self.cell_size / 2  # calculo do y do pixel
        self.desenhaLinha(p1x, p1y, p2x, p2y, 4, "blue")
                    
    def mostraJanela(self, eng):
        '''
        Percorre toda a janela, linha a linha e dentro de cada linha coluna a coluna, desenhando cada casa correspondente na sequencia
        '''
        try:
            self.janela.delete("all")
            self.desenhaNumsColunas()  # tambem desenha as linhas verticais da grelha
            self.desenhaNumsLinhas()  # tambem desenha as linhas horizontais da grelha
            pos_x_anterior = 0
            pos_y_anterior = 0
            for linha in eng.get_matriz_total():
                self.desenhaLigacao(pos_x_anterior, pos_y_anterior, linha[1], linha[2])
                self.desenhaAB(linha[1], linha[2], linha[0])
                pos_x_anterior = linha[1]
                pos_y_anterior = linha[2]
        except BaseException as e:
            print("erro ao desenhar:", e)
            return "NÃO"
        return "SIM"
                             

