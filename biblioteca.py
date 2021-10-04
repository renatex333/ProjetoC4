
import cv2

def encontra_peca(pos):
    # 0 -> sem peça
    # 1 -> peça vermelha
    # 2 -> peça amarela
    hsv = cv2.cvtColor(pos.copy(), cv2.COLOR_BGR2HSV)
    mask_vermelho = cv2.inRange(hsv,(0, 200, 200),(20/2, 255, 255))
    cont_vermelho, _ = cv2.findContours(mask_vermelho, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    mask_amarelo = cv2.inRange(hsv,(40/2, 200, int(0.5*255)),(60/2, 255, 255))
    cont_amarelo, _ = cv2.findContours(mask_amarelo, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    if len(cont_vermelho) == 0 and len(cont_amarelo) == 0:
        return 0
    elif len(cont_vermelho) > 0 and len(cont_amarelo) > 0:
        maior_area_v = 0
        for v in cont_vermelho:
            if abs(cv2.contourArea(v)) > maior_area_v:
                maior_area_v = abs(cv2.contourArea(v))
        maior_area_a = 0
        for a in cont_amarelo:
            if abs(cv2.contourArea(a)) > maior_area_a:
                maior_area_a = abs(cv2.contourArea(a))
        if maior_area_v > maior_area_a:
            return 1
        else:
            return 2
    elif len(cont_vermelho) > 0:
        return 1
    elif len(cont_amarelo) > 0:
        return 2


# Esta sessão dedicada à checagem das peças do tabuleiro e se elas geram vitória não foi criada por mim,
# mas pelo usuário do GitHub ForrestKnight, em seu repositório ForrestKnight/ConnectFour
# https://github.com/ForrestKnight/ConnectFour

def checa_adjacente(mat_tabuleiro, peca, linha, coluna, delta_linha, delta_coluna):
    contagem = 0
    for i in range(4):
        peca_atual = mat_tabuleiro[linha][coluna]
        if peca == peca_atual:
            contagem += 1
        linha += delta_linha
        coluna += delta_coluna
    return contagem


def checa_vitoria(mat_tabuleiro, peca):
    # Vertical
    for linha in range(len(mat_tabuleiro) - 3):
        for coluna in range(len(mat_tabuleiro[0])):
            ticks = checa_adjacente(mat_tabuleiro, peca, linha, coluna, 1, 0)
            if ticks == 4: return True
    # Horizontal
    for linha in range(len(mat_tabuleiro)):
        for coluna in range(len(mat_tabuleiro[0]) - 3):
            ticks = checa_adjacente(mat_tabuleiro, peca, linha, coluna, 0, 1)
            if ticks == 4: return True
    # Diagonal com inclinação positiva
    for linha in range(len(mat_tabuleiro) - 3):
        for coluna in range(len(mat_tabuleiro[0]) - 3):
            ticks = checa_adjacente(mat_tabuleiro, peca, linha, coluna, 1, 1)
            if ticks == 4: return True
    # Diagonal com inclinação negativa
    for linha in range(3, len(mat_tabuleiro)):
        for coluna in range(len(mat_tabuleiro[0]) - 5):
            ticks = checa_adjacente(mat_tabuleiro, peca, linha, coluna, -1, 1)
            if ticks == 4: return True
    return False
