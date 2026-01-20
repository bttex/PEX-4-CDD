import pandas as pd
import random

# -----------------------------
# Configurações gerais
# -----------------------------
SEED = 42
OUTPUT_FILE = "estoque_esim_mock.csv"

random.seed(SEED)

# Lista de DDDs brasileiros (exemplo)
DDDS = [11, 21, 31, 41, 51, 61, 71, 81, 91]

# -----------------------------
# Geração dos dados
# -----------------------------
dados = []

for ddd in DDDS:
    total = random.randint(500, 3000)
    em_uso = random.randint(0, total)
    disponivel = total - em_uso

    dados.append(
        {"DDD": ddd, "Total": total, "Em_uso": em_uso, "Disponivel": disponivel}
    )

# -----------------------------
# Criação do DataFrame
# -----------------------------
df = pd.DataFrame(dados)

# -----------------------------
# Exportação para CSV
# -----------------------------
df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print(f"Arquivo '{OUTPUT_FILE}' gerado com sucesso!")
