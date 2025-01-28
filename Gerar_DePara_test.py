def gerar_arquivo_txt(de, para, metrica, ryg, nome_arquivo="saida.txt"):

    para_formatado = str(para)
    de_formatado = str(de)

    metrica_formatada = f"{metrica}" if int(metrica) < 10 else f"{int(metrica):02}"
    
    ryg_formatado = ryg[0] if ryg else "N"
    
    conteudo = f"{de_formatado}{para_formatado}{metrica_formatada}{ryg_formatado}"

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
    
    print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")

# Exemplos de uso
gerar_arquivo_txt(de="500", para="QualquerValor", metrica=80, ryg="Y")   
