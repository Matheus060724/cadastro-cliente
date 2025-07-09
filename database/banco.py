from pathlib import Path
import json

caminho = Path(__file__).parent.parent
reposi = caminho/"data"
arquivo = reposi/"cliente.json"

reposi.mkdir(exist_ok=True)


def salvar_arquivo(cliente_dict):
    if not arquivo.exists():
        with open(arquivo, "w", encoding="utf-8") as arq:
            json.dump([], arq, indent=4)
        
    with open(arquivo, "r+", encoding="utf-8") as arq:
        dados = json.load(arq)
        dados.append(cliente_dict)
        arq.seek(0)
        json.dump(dados, arq, indent=4)
        