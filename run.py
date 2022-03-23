# Implementação da identificação de cores do tabuleiro utilizando a biblioteca OpenCV

import cv2
import numpy as np
import biblioteca
import os

if __name__ == '__main__':
    print ("OpenCV Version : %s " % cv2.__version__)

    # Este programa vai capturar um frame da webcam quando uma tecla específica for pressionada
    # e vai identificar o tabuleiro e as peças posicionadas.
    # A tecla a ser pressionada para captura é: (ainda não definida)

    # Para motivo de teste, é possível pegar tabuleiros de jogos jogados por um ser humano
    # no site https://connect4.gamesolver.org/
    # Terminados os jogos, as capturas de tela podem ser salvas e utilizadas nos testes

    frame = cv2.imread("img/teste2.png")

    ###########################################################################################
    ### Essa seção é utilizada para separar apenas o tabuleiro do resto da imagem.
    ### Para fazer isso, utilizarei a máscara do tabuleiro como guia para identificar
    ### o tabuleiro no ambiente e cortar um retângulo contendo esse tabuleiro
    ### para poder analisar as peças do tabuleiro sem interferências.

    # hsv_frame = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2HSV)
    ### Essas cores devem servir para estipular uma faixa da cor do tabuleiro que deve ser segmentado
    # lower_color = ( 236/2 , int(0.2*255) , int(0.68*255) )
    # upper_color = ( 250/2 , int(0.3*255) , int(0.75*255) )
    # mask_tabuleiro = cv2.inRange(hsv_frame, lower_color, upper_color)

    # i_linhas, i_colunas = np.where(mask_tabuleiro!=0)
    # min_linha = min(i_linhas)
    # max_linha = max(i_linhas)
    # min_coluna = min(i_colunas)
    # max_coluna = max(i_colunas)

    # frame = frame[min_linha:max_linha, min_coluna:max_coluna]
    ###########################################################################################

    altura_tabela = frame.shape[0]
    altura_linha = int(altura_tabela/6)
    altura_tabela = frame.shape[1]
    largura_coluna = int(altura_tabela/7)

    pos00 = frame[0:altura_linha, 0:largura_coluna]
    pos01 = frame[0:altura_linha, largura_coluna:largura_coluna*2]
    pos02 = frame[0:altura_linha, largura_coluna*2:largura_coluna*3]
    pos03 = frame[0:altura_linha, largura_coluna*3:largura_coluna*4]
    pos04 = frame[0:altura_linha, largura_coluna*4:largura_coluna*5]
    pos05 = frame[0:altura_linha, largura_coluna*5:largura_coluna*6]
    pos06 = frame[0:altura_linha, largura_coluna*6:]

    pos10 = frame[altura_linha:altura_linha*2, 0:largura_coluna]
    pos11 = frame[altura_linha:altura_linha*2, largura_coluna:largura_coluna*2]
    pos12 = frame[altura_linha:altura_linha*2, largura_coluna*2:largura_coluna*3]
    pos13 = frame[altura_linha:altura_linha*2, largura_coluna*3:largura_coluna*4]
    pos14 = frame[altura_linha:altura_linha*2, largura_coluna*4:largura_coluna*5]
    pos15 = frame[altura_linha:altura_linha*2, largura_coluna*5:largura_coluna*6]
    pos16 = frame[altura_linha:altura_linha*2, largura_coluna*6:]

    pos20 = frame[altura_linha*2:altura_linha*3, 0:largura_coluna]
    pos21 = frame[altura_linha*2:altura_linha*3, largura_coluna:largura_coluna*2]
    pos22 = frame[altura_linha*2:altura_linha*3, largura_coluna*2:largura_coluna*3]
    pos23 = frame[altura_linha*2:altura_linha*3, largura_coluna*3:largura_coluna*4]
    pos24 = frame[altura_linha*2:altura_linha*3, largura_coluna*4:largura_coluna*5]
    pos25 = frame[altura_linha*2:altura_linha*3, largura_coluna*5:largura_coluna*6]
    pos26 = frame[altura_linha*2:altura_linha*3, largura_coluna*6:]

    pos30 = frame[altura_linha*3:altura_linha*4, 0:largura_coluna]
    pos31 = frame[altura_linha*3:altura_linha*4, largura_coluna:largura_coluna*2]
    pos32 = frame[altura_linha*3:altura_linha*4, largura_coluna*2:largura_coluna*3]
    pos33 = frame[altura_linha*3:altura_linha*4, largura_coluna*3:largura_coluna*4]
    pos34 = frame[altura_linha*3:altura_linha*4, largura_coluna*4:largura_coluna*5]
    pos35 = frame[altura_linha*3:altura_linha*4, largura_coluna*5:largura_coluna*6]
    pos36 = frame[altura_linha*3:altura_linha*4, largura_coluna*6:]

    pos40 = frame[altura_linha*4:altura_linha*5, 0:largura_coluna]
    pos41 = frame[altura_linha*4:altura_linha*5, largura_coluna:largura_coluna*2]
    pos42 = frame[altura_linha*4:altura_linha*5, largura_coluna*2:largura_coluna*3]
    pos43 = frame[altura_linha*4:altura_linha*5, largura_coluna*3:largura_coluna*4]
    pos44 = frame[altura_linha*4:altura_linha*5, largura_coluna*4:largura_coluna*5]
    pos45 = frame[altura_linha*4:altura_linha*5, largura_coluna*5:largura_coluna*6]
    pos46 = frame[altura_linha*4:altura_linha*5, largura_coluna*6:]

    pos50 = frame[altura_linha*5:altura_linha*6, 0:largura_coluna]
    pos51 = frame[altura_linha*5:altura_linha*6, largura_coluna:largura_coluna*2]
    pos52 = frame[altura_linha*5:altura_linha*6, largura_coluna*2:largura_coluna*3]
    pos53 = frame[altura_linha*5:altura_linha*6, largura_coluna*3:largura_coluna*4]
    pos54 = frame[altura_linha*5:altura_linha*6, largura_coluna*4:largura_coluna*5]
    pos55 = frame[altura_linha*5:altura_linha*6, largura_coluna*5:largura_coluna*6]
    pos56 = frame[altura_linha*5:altura_linha*6, largura_coluna*6:]

    matriz_posicoes = [ [pos00, pos01, pos02, pos03, pos04, pos05, pos06],
                        [pos10, pos11, pos12, pos13, pos14, pos15, pos16],
                        [pos20, pos21, pos22, pos23, pos24, pos25, pos26],
                        [pos30, pos31, pos32, pos33, pos34, pos35, pos36],
                        [pos40, pos41, pos42, pos43, pos44, pos45, pos46],
                        [pos50, pos51, pos52, pos53, pos54, pos55, pos56]
                      ]

    matriz_tabuleiro = np.zeros((6,7))

    for i in range(0,6):
        for j in range(0,7):
            # 0 -> sem peça
            # 1 -> peça vermelha
            # 2 -> peça amarela
            matriz_tabuleiro[i][j] = biblioteca.encontra_peca(matriz_posicoes[i][j])

    peca_vermelha = 1
    peca_amarela = 2
    
    print(matriz_tabuleiro)
    ganhou = biblioteca.checa_vitoria(matriz_tabuleiro, peca_vermelha)
    print(f'Vermelho ganhou?{ganhou}')
    ganhou = biblioteca.checa_vitoria(matriz_tabuleiro, peca_amarela)
    print(f'Amarelo ganhou?{ganhou}')


    while True:
        cv2.imshow('Frame', frame)
        # cv2.imshow('Mask tabuleiro', mask_tabuleiro)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
