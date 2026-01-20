import subprocess
import json

def fetch_data(token, url):
    curl_command = [
        "curl", "-X", "GET", url,
        "-H", f"x-api-key: {token}",
        "-H", "Content-Type: application/json"
    ]
   
    result = subprocess.run(curl_command, capture_output=True, text=True)
   
    if result.returncode == 0:
        try:
            dados_json = json.loads(result.stdout)
            # Garantir que dados_json é um dicionário (mesmo comportamento do código original)
            if isinstance(dados_json, list) and dados_json:
                dados_json = dados_json[0]
            return dados_json
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar JSON: {e}")
            return None
    else:
        print("Erro ao executar o comando curl:", result.stderr)
        return None