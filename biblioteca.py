
import cv2

def encontra_peca(posicao):
    # Recebe um pedaço do tabuleiro e tenta descobrir se há peça nessa posição e,
    # se houver, usa visão computacional para descobrir se é vermelha ou amarela
    # 0 -> sem peça
    # 1 -> peça vermelha
    # 2 -> peça amarela
    hsv = cv2.cvtColor(posicao.copy(), cv2.COLOR_BGR2HSV)
    mask_vermelho = cv2.inRange(hsv,(0, 200, 200),(20/2, 255, 255))
    contornos_vermelhos, _ = cv2.findContours(mask_vermelho, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    mask_amarelo = cv2.inRange(hsv,(40/2, 200, int(0.5*255)),(60/2, 255, 255))
    contornos_amarelos, _ = cv2.findContours(mask_amarelo, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    if len(contornos_vermelhos) == 0 and len(contornos_amarelos) == 0:
        return 0
    elif len(contornos_vermelhos) > 0 and len(contornos_amarelos) > 0:
        maior_area_vermelho = 0
        for contorno_vermelho in contornos_vermelhos:
            if abs(cv2.contourArea(contorno_vermelho)) > maior_area_vermelho:
                maior_area_vermelho = abs(cv2.contourArea(contorno_vermelho))
        maior_area_amarelo = 0
        for contorno_amarelo in contornos_amarelos:
            if abs(cv2.contourArea(contorno_amarelo)) > maior_area_amarelo:
                maior_area_amarelo = abs(cv2.contourArea(contorno_amarelo))
        if maior_area_vermelho > maior_area_amarelo:
            return 1
        else:
            return 2
    elif len(contornos_vermelhos) > 0:
        return 1
    elif len(contornos_amarelos) > 0:
        return 2


# Esta sessão dedicada à checagem das peças do tabuleiro e se elas geram vitória não foi criada por mim,
# mas pelo usuário do GitHub ForrestKnight, em seu repositório ForrestKnight/ConnectFour
# https://github.com/ForrestKnight/ConnectFour

def checa_adjacente(matriz_tabuleiro, cor_peca, linha, coluna, delta_linha, delta_coluna):
    contagem = 0
    for i in range(4):
        peca_atual = matriz_tabuleiro[linha][coluna]
        if cor_peca == peca_atual:
            contagem += 1
        linha += delta_linha
        coluna += delta_coluna
    return contagem


def checa_vitoria(matriz_tabuleiro, cor_peca):
    # Vertical
    for linha in range(len(matriz_tabuleiro) - 3):
        for coluna in range(len(matriz_tabuleiro[0])):
            ticks = checa_adjacente(matriz_tabuleiro, cor_peca, linha, coluna, 1, 0)
            if ticks == 4: return True
    # Horizontal
    for linha in range(len(matriz_tabuleiro)):
        for coluna in range(len(matriz_tabuleiro[0]) - 3):
            ticks = checa_adjacente(matriz_tabuleiro, cor_peca, linha, coluna, 0, 1)
            if ticks == 4: return True
    # Diagonal com inclinação positiva
    for linha in range(len(matriz_tabuleiro) - 3):
        for coluna in range(len(matriz_tabuleiro[0]) - 3):
            ticks = checa_adjacente(matriz_tabuleiro, cor_peca, linha, coluna, 1, 1)
            if ticks == 4: return True
    # Diagonal com inclinação negativa
    for linha in range(3, len(matriz_tabuleiro)):
        for coluna in range(len(matriz_tabuleiro[0]) - 5):
            ticks = checa_adjacente(matriz_tabuleiro, cor_peca, linha, coluna, -1, 1)
            if ticks == 4: return True
    return False
