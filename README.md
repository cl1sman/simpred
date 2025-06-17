# 🧠 simpred – Simulador de Predição de Desvios (Python)

Este projeto implementa um simulador educacional de predição de desvios (`branches`) para fins de estudo de arquitetura de computadores. Ele é utilizado para simular técnicas de predição estáticas e dinâmicas baseadas em um arquivo de trace fornecido.

## 📌 Técnicas implementadas

O simulador calcula a taxa de acertos de cada uma das seguintes técnicas de predição:

### Estáticas
- **Not-taken**: assume que todos os desvios **não serão tomados**
- **Taken**: assume que todos os desvios **serão tomados**
- **Direção**:
  - Desvios para trás (backward) → **taken**
  - Desvios para frente (forward) → **not-taken**

### Dinâmicas
- **1-bit**: armazena o último resultado de cada branch
- **2-bits**: contador saturado com 4 estados (00 a 11)

## 🗂️ Estrutura do trace

O arquivo de entrada deve ter o seguinte formato por linha:

```
branch  target  T|N
``` 

Exemplo:

```
13776 13864 N
14060 14072 T
```

## ▶️ Como executar

### Requisitos
- Python 3.x

### Comando

```bash
python simpred.py trace.txt 16
````

* `trace.txt`: nome do arquivo com os branches
* `16`: número de linhas da tabela BPB (deve ser potência de 2)

## 📊 Exemplo de saída

```
Total de branches executados: 1200
Taxa de acertos (Not-taken): 48.91%
Taxa de acertos (Taken): 51.08%
Taxa de acertos (Direção): 76.83%
Taxa de acertos (1-bit): 88.42%
Taxa de acertos (2-bits): 91.25%
```

<!-- ## 💡 Próximos passos

* Suporte à predição com correlação (global history)
* Geração de gráficos de desempenho
* Exportação para CSV -->

## 👨‍💻 Autor

Feito por `Clisman`, `Franciso`e `Larissa` como parte do Trabalho 2 da disciplina de Arquitetura de Computadores II (UFMS, 2025).
