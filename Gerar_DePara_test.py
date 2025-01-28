def gerar_arquivo_txt(de, para, metrica, ryg, nome_arquivo="saida.txt"):

    # Garantir que 'para' seja exibido corretamente
    para_formatado = str(para)
    de_formatado = str(de)
    
    # Garantir que 'metrica' preserve o comportamento desejado
    metrica_formatada = f"{metrica}" if int(metrica) < 10 else f"{int(metrica):02}"
    
    # Garantir que 'ryg' seja um único caractere
    ryg_formatado = ryg[0] if ryg else "N"
    
    # Formatar o conteúdo do arquivo
    conteudo = f"{de_formatado}{para_formatado}{metrica_formatada}{ryg_formatado}"
    
    # Escrever no arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
    
    print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")

# Exemplos de uso
gerar_arquivo_txt(de="500", para="QualquerValor", metrica=80, ryg="Y")   # Exemplo 1
