from pathlib import Path
import json

#Caminhos e criação de arquivos e diretorios
caminho = Path(__file__).parent.parent
reposi = caminho/"data"
arquivo = reposi/"cliente.json"

reposi.mkdir(exist_ok=True)

#função para coletar os dados e transformar em JSON
def salvar_arquivo(cliente_dict):
    #Condição caso o arquivo não seja existente sua criação
    if not arquivo.exists():
        with open(arquivo, "w", encoding="utf-8") as arq:
            json.dump([], arq, indent=4)

    # leitiura e escrita de novos dados    
    with open(arquivo, "r+", encoding="utf-8") as arq:
        dados = json.load(arq)
        dados.append(cliente_dict)
        arq.seek(0)
        json.dump(dados, arq, indent=4)
        