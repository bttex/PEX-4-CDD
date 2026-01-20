import pandas as pd
import random
from datetime import datetime, timedelta

# -----------------------------
# Configurações
# -----------------------------
SEED = 42
OUTPUT_FILE = "estoque_esim_mock.csv"
NUM_DIAS = 30  # quantidade de dias (D-1, D-2, ...)
random.seed(SEED)

# DDDs simulados
DDDS = [11, 21, 31, 41, 51, 61, 71, 81, 91]

# Data base (D-1)
data_base = datetime.today() - timedelta(days=1)

# -----------------------------
# Geração dos dados
# -----------------------------
dados = []

for ddd in DDDS:
    # Total fixo por DDD (simula capacidade de estoque)
    total = random.randint(500, 20000)

    em_uso_anterior = random.randint(0, total)

    for i in range(NUM_DIAS):
        data_ref = (data_base - timedelta(days=i)).date()

        # Pequena variação diária no uso
        variacao = random.randint(-50, 50)
        em_uso = max(0, min(total, em_uso_anterior + variacao))

        disponivel = total - em_uso

        dados.append(
            {
                "Data": data_ref.strftime("%Y-%m-%d"),
                "DDD": ddd,
                "Total": total,
                "Em_uso": em_uso,
                "Disponivel": disponivel,
            }
        )

        em_uso_anterior = em_uso

# -----------------------------
# DataFrame e exportação
# -----------------------------
df = pd.DataFrame(dados)

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print(f"Arquivo '{OUTPUT_FILE}' gerado com sucesso!")
