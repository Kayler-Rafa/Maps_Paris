# 🚇 Busca de Rotas no Metrô de Paris

Este projeto implementa algoritmos de busca para encontrar trajetos entre estações do metrô de Paris. Ele utiliza tanto uma **busca cega** (em largura) quanto uma **busca heurística** (best-first search), considerando o tempo de deslocamento e trocas de linha. Os resultados são exibidos no terminal e em um arquivo HTML gerado dinamicamente.

---

## 🔍 Metodologias de Busca

### 🔴 Busca Cega (Largura-Primeiro)
A busca cega explora todas as possibilidades sem heurística, garantindo um caminho válido, mas sem otimização do tempo. Ela percorre todas as opções até encontrar a solução.

### 🔵 Busca Heurística (Best-First Search)
A busca heurística leva em consideração o tempo de deslocamento entre estações e aplica uma penalização ao tempo caso haja uma troca de linha. Isso torna o caminho mais eficiente em termos de tempo de viagem.

---

## 🛠️ Como Executar o Projeto

### 📌 Requisitos
- Python 3 instalado no sistema
- Navegador para visualizar os resultados

### 📥 Instalação e Execução
1. Clone ou baixe este repositório:
   ```sh
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```
2. Execute o script principal:
   ```sh
   python main.py
   ```
3. Insira a estação de origem, a linha de metrô correspondente e a estação de destino quando solicitado.
4. Após a execução, um arquivo `visualizacao.html` será gerado e aberto automaticamente em seu navegador.

---

## 📊 Visualização dos Resultados
Os resultados da busca são exibidos em um arquivo HTML, onde você pode comparar as duas buscas. O arquivo inclui:
- **Caminho encontrado pela Busca Cega**
- **Caminho encontrado pela Busca Heurística**
- **Tempo total estimado para cada rota**
- **Gráfico interativo com os tempos entre estações**

### 🖥️ Exemplo de Saída no HTML:
```html
<div class="route blind">
    <h3>Busca Cega</h3>
    <p><strong>Caminho:</strong> E1 -> E3 -> E5 -> E6</p>
    <p><strong>Tempo Estimado:</strong> 26.4 minutos</p>
</div>

<div class="route heuristic">
    <h3>Busca Heurística</h3>
    <p><strong>Caminho:</strong></p>
    <ul>
        <li>E1 (azul)</li>
        <li>E3 (azul)</li>
        <li>E5 (azul)</li>
        <li>E6 (azul)</li>
    </ul>
    <p><strong>Tempo Estimado:</strong> 22.8 minutos</p>
</div>
```

---

## 📌 Considerações Finais
- O código permite comparar eficiência entre os dois métodos de busca.
- A visualização HTML torna a análise mais intuitiva e interativa.
- O projeto pode ser expandido para incluir mais estações e outras otimizações de trajetos.

Se tiver sugestões ou melhorias, sinta-se à vontade para contribuir! 🚀

