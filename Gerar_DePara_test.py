def entrada_depara():
    regras = []  
    Tamanho_Para = int(input("Quantidade de caracteres do Para: "))  # Tamanho total de cada linha

    while True:
        # Entradas do usuário
        De = input("De: ")
        Descricao_Retorno = input("Descrição_Retorno: ")
        Metrica = input("Metrica: ")
        Ryg = input("RYG: ")
        
        # Somar os caracteres já preenchidos
        caracteres_utilizados = len(De) + len(Descricao_Retorno) + len(Metrica) + len(Ryg)
        
        # Calcular os caracteres restantes
        espacos_restantes = Tamanho_Para - caracteres_utilizados
        
        if espacos_restantes < 0:
            print("Erro: o tamanho total dos campos excede o limite definido.")
            continue
        
        # Preencher a diferença em 'Descrição_Retorno'
        Descricao_Retorno += " " * espacos_restantes
        
        # Formatar a saída garantindo o tamanho correto
        saida = f"{De}{Descricao_Retorno}{Metrica}{Ryg}"
        
        # Garantir que a linha tenha exatamente Tamanho_Para caracteres antes da quebra de linha
        saida = saida[:Tamanho_Para] + "\n"
        
        # Adicionar a regra formatada à lista
        regras.append(saida)
        
        # Perguntar ao usuário se deseja inserir outra regra
        continuar = input("Deseja inserir mais uma regra? (S/N): ").strip().upper()
        if continuar != 'S':
            break

    # Exibir as saídas formatadas, garantindo que cada linha termine com uma quebra de linha
    print("Saídas:")
    for regra in regras:
        print(regra, end="")  # Impede que o print adicione uma quebra extra
    
    # Salvar todas as regras em um arquivo txt
    with open("Teste_valida_tipo_atividade.txt", "w", encoding="utf-8", newline="\n") as arquivo:
        arquivo.writelines(regras)  # Garante que as quebras de linha sejam mantidas corretamente
    
    print("Saída salva em 'saida.txt'.")
    print("Cada regra termina com uma quebra de linha.")

# Executar a função
entrada_depara()
