import sys
import math

#################### Funções de Ajuste############################
def parse_trace_line(line):
    parts = line.strip().split()
    return int(parts[0]), int(parts[1]), parts[2]

# Função de indice do BPB
def index_bpb(addr, n_lines):
    bits = int(math.log2(n_lines))
    shifted = addr >> 2
    return shifted & ((1 << bits) - 1)

#################### Funções de Predição ##########################

# Função de Predição not-taken
def not_taken(ocorrido):
    return 1 if ocorrido == 0 else 0

# Função de Predição taken
def taken(ocorrido):
    return 1 if ocorrido == 1 else 0

# Função de Predição baseada na direção
def direction(branch, target, ocorrido):
    # Se desvio é "para trás", então predição é T.
    # Loops voltam para uma posição anterior
    is_backward = target < branch
    return 1 if ocorrido == is_backward else 0

# Função de Predição 1-bit
def predict_1bit(bpb, addr, ocorrido):
    index = index_bpb(addr, len(bpb))
    prediction = bpb[index]
    
    # Atualiza o BPB
    if ocorrido == 1:  # Taken
        bpb[index] = 1
    else:  # Not taken
        bpb[index] = 0
    # return prediction
    return 1 if prediction == ocorrido else 0

def predict_2bit(bpb, addr, ocorrido):
    index = index_bpb(addr, len(bpb))
    state = bpb[index]

    # Faz a predição primeiro (baseado no estado atual)
    pred = 1 if state >= 2 else 0

    # Agora atualiza o estado com base no resultado real
    # if pred == ocorrido # Taken
        # aux = 1 
    # Atualiza o estado
    if ocorrido == 1:
        bpb[index] = min(state + 1, 3)  # Incrementa o estado
    else:
        bpb[index] = max(state - 1, 0)
    # return acerto if pred == ocorrido else 0
    
    return 1 if pred == ocorrido else 0


# Função principal
def main():
    # Verifica argumetnos da linha de comando
    if len(sys.argv) != 3:
        print("Uso: python simpred.py trace.txt nLinhasBPB")
        return
    
    trace_file = sys.argv[1]
    n_lines = int(sys.argv[2])

    # Buffer the predição
    bpb_1bit = [0] * n_lines # Crio uma lista com o numero de "linhas" da tabela
    bpb_2bit = [0] * n_lines

    # Contadores para as taxas
    nBranches = 0
    acertos_nt = acertos_t = acertos_dir = 0
    acertos_1bit = acertos_2bit = 0

    with open(trace_file) as f:
        for line in f:
            branch, target, outcome = parse_trace_line(line)
            nBranches += 1
            ocorrido = 1 if outcome == 'T' else 0 # 1 = taken, 0 = not taken

            acertos_t += taken(ocorrido)
            acertos_nt += not_taken(ocorrido)
            acertos_dir += direction(branch, target, ocorrido)
            acertos_1bit += predict_1bit(bpb_1bit, branch, ocorrido)
            acertos_2bit += predict_2bit(bpb_2bit, branch, ocorrido)

    ######################### Result #############################
    print(f"Total de branches executados: {nBranches}")
    print(f"Total de acertos (Not-taken): {acertos_nt}")
    print(f"Total de acertos (Taken): {acertos_t}")
    print(f"Total de acertos (Direção): {acertos_dir}")
    print(f"Total de acertos (1-bit): {acertos_1bit}")
    print(f"Total de acertos (2-bit): {acertos_2bit}")

# Execução da função principal
if __name__ == "__main__":
    main()