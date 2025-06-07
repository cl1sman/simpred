import sys

#################### Funções de Ajuste############################
def parse_trace_line(line):
    parts = line.strip().split()
    return int(parts[0]), int(parts[1]), parts[2]

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

# Função principal
def main():
    # Verifica argumetnos da linha de comando
    if len(sys.argv) != 3:
        print("Uso: python simpred.py trace.txt nLinhasBPB")
        return
    
    trace_file = sys.argv[1]
    n_lines = int(sys.argv[2])

    # Buffer the predição
    bpb_1bit = [0] * n_lines
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

    ######################### Result #############################
    print(f"Total de branches executados: {nBranches}")
    print(f"Total de acertos (Not-taken): {acertos_nt}")
    print(f"Total de acertos (Taken): {acertos_t}")
    print(f"Total de acertos (Direção): {acertos_dir}")

# Execução da função principal
if __name__ == "__main__":
    main()