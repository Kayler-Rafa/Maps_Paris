import heapq
from collections import deque
import webbrowser

# Velocidade do trem (30 km/h) e tempo de baldeação (4 min convertidos para horas)
TREM_VELOCIDADE = 30
TEMPO_BALDEACAO = 4 / 60

# Definição das linhas do metrô
linhas_metro = {
    'azul': ['E1', 'E2', 'E3', 'E4', 'E5', 'E6'],
    'amarela': ['E10', 'E2', 'E9', 'E8', 'E5', 'E7'],
    'vermelha': ['E11', 'E9', 'E3', 'E13'],
    'verde': ['E12', 'E8', 'E4', 'E13', 'E14']
}

# Distâncias entre estações (em km)
distancias_reais = {
    ('E1', 'E2'): 10, ('E2', 'E3'): 8.5, ('E3', 'E4'): 6.3, ('E4', 'E5'): 13, ('E5', 'E6'): 3,
    ('E10', 'E2'): 10, ('E2', 'E9'): 3.5, ('E9', 'E8'): 9.6, ('E8', 'E5'): 19.4, ('E5', 'E7'): 2.4,
    ('E11', 'E9'): 12.2, ('E9', 'E3'): 9.4, ('E3', 'E13'): 18.7,
    ('E12', 'E8'): 6.4, ('E8', 'E4'): 15.3, ('E4', 'E13'): 12.8, ('E13', 'E14'): 5.1
}

# Tornando o grafo bidirecional
for (a, b), dist in list(distancias_reais.items()):
    distancias_reais[(b, a)] = dist

# Função para obter as linhas de uma estação
def linhas_estacao(estacao):
    return [linha for linha, estacoes in linhas_metro.items() if estacao in estacoes]

# Converte distância em tempo (horas)
def tempo_viagem(dist_km):
    return dist_km / TREM_VELOCIDADE

# Busca cega (largura) - Agora calcula o tempo total gasto
def busca_cega(origem, destino):
    fila = deque()
    fila.append((origem, [origem]))
    visitados = set()

    while fila:
        atual, caminho = fila.popleft()

        if atual == destino:
            return caminho

        visitados.add(atual)

        for (e1, e2), _ in distancias_reais.items():
            if e1 == atual and e2 not in visitados and e2 not in caminho:
                fila.append((e2, caminho + [e2]))

    return None

# Calcula o tempo de um caminho qualquer
def calcular_tempo_total(caminho):
    tempo_total = 0
    for i in range(len(caminho) - 1):
        est1, est2 = caminho[i], caminho[i + 1]
        tempo_total += tempo_viagem(distancias_reais[(est1, est2)])
    return tempo_total

# Busca heurística (best-first search), considerando tempo de baldeação
def busca_heuristica(origem, linha_origem, destino):
    fila = []
    heapq.heappush(fila, (0, origem, linha_origem, []))
    visitados = set()

    while fila:
        tempo_acumulado, atual, linha_atual, caminho = heapq.heappop(fila)

        if (atual, linha_atual) in visitados:
            continue
        visitados.add((atual, linha_atual))

        caminho = caminho + [(atual, linha_atual)]

        if atual == destino:
            return caminho, tempo_acumulado

        for (e1, e2), dist in distancias_reais.items():
            if e1 == atual:
                for prox_linha in linhas_estacao(e2):
                    troca = TEMPO_BALDEACAO if prox_linha != linha_atual else 0
                    tempo_total = tempo_acumulado + tempo_viagem(dist) + troca
                    heapq.heappush(fila, (tempo_total, e2, prox_linha, caminho))

    return None, float('inf')

# Gera um arquivo HTML para visualização do trajeto
def gerar_visualizacao(caminho_cego, tempo_cego, caminho_heuristico, tempo_heuristico):
    html_content = f"""
    <html>
    <head>
        <title>Visualização da Busca no Metrô</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .container {{ max-width: 600px; margin: auto; }}
            .route {{ background: #f4f4f4; padding: 10px; margin-bottom: 10px; border-radius: 5px; }}
            .heuristic {{ color: blue; }}
            .blind {{ color: red; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Comparação de Rotas</h2>

            <div class="route blind">
                <h3>Busca Cega</h3>
                <p><strong>Caminho:</strong> {' -> '.join(caminho_cego)}</p>
                <p><strong>Tempo Estimado:</strong> {tempo_cego * 60:.2f} minutos</p>
            </div>

            <div class="route heuristic">
                <h3>Busca Heurística</h3>
                <p><strong>Caminho:</strong></p>
                <ul>
                    {''.join([f"<li>{est[0]} ({est[1]})</li>" for est in caminho_heuristico])}
                </ul>
                <p><strong>Tempo Estimado:</strong> {tempo_heuristico * 60:.2f} minutos</p>
            </div>
        </div>
    </body>
    </html>
    """

    with open("visualizacao.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    webbrowser.open("visualizacao.html")

# Interface principal
if __name__ == "__main__":
    origem = input("Digite a estação de origem (ex: E1): ").strip().upper()
    linha_origem = input("Digite a linha em que está (azul, amarela, vermelha, verde): ").strip().lower()
    destino = input("Digite a estação de destino (ex: E14): ").strip().upper()

    print("\nRESULTADO DA BUSCA CEGA:")
    caminho_cego = busca_cega(origem, destino)
    if caminho_cego:
        tempo_cego = calcular_tempo_total(caminho_cego)
        print(f"Caminho encontrado (não otimizado): {' -> '.join(caminho_cego)}")
        print(f"Tempo estimado: {tempo_cego * 60:.2f} minutos")
    else:
        print("Caminho não encontrado.")

    print("\nRESULTADO DA BUSCA HEURÍSTICA:")
    caminho_heuristico, tempo_heuristico = busca_heuristica(origem, linha_origem, destino)
    if caminho_heuristico:
        for est, linha in caminho_heuristico:
            print(f"{est} ({linha})")
        print(f"Tempo estimado: {tempo_heuristico * 60:.2f} minutos")
    else:
        print("Caminho não encontrado.")

    # Gerar visualização HTML
    if caminho_cego and caminho_heuristico:
        gerar_visualizacao(caminho_cego, tempo_cego, caminho_heuristico, tempo_heuristico)
