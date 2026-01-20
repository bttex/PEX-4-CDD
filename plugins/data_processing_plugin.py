import pandas as pd
from datetime import datetime, timedelta


def process_data(dados_json):
    # Inicializar estoque no início da função
    estoque = pd.DataFrame()  # Valor padrão
    
    # Verificação de entrada
    if dados_json is None:
        print("Dados JSON são None")
        return estoque
    
    try:
        # Conversão para dicionário se for lista
        if isinstance(dados_json, list):
            if not dados_json:  # Lista vazia
                print("Lista JSON vazia")
                return estoque
            dados_json = dados_json[0]
        
        # Verificar a estrutura do JSON
        if not all(key in dados_json for key in ['total', 'inuse', 'free']):
            print("Estrutura JSON inválida, faltando chaves necessárias")
            return estoque
        
        # Criação dos DataFrames
        total = pd.DataFrame(dados_json.get('total', []))
        inuse = pd.DataFrame(dados_json.get('inuse', []))
        free = pd.DataFrame(dados_json.get('free', []))
        
        if total.empty or inuse.empty or free.empty:
            print("Um ou mais DataFrames estão vazios")
            return estoque
            
        # Renomear colunas
        total = total.rename(columns={'count': 'Total', '_id': 'ddd'})
        inuse = inuse.rename(columns={'count': 'Em_Uso', '_id': 'ddd'})
        free = free.rename(columns={'count': 'Disponivel', '_id': 'ddd'})
        
        # Concatenar
        resultado = pd.concat([total, inuse, free], ignore_index=True)
        df = resultado[['ddd']].drop_duplicates()
        
        # Explodir colunas
        try:
            total_exp = total.explode('ddd')
            inuse_exp = inuse.explode('ddd')
            free_exp = free.explode('ddd')
        except Exception as e:
            print(f"Erro ao explodir colunas: {e}")
            return estoque
            
        # De-para
        de_para = resultado[['ddd']].drop_duplicates()
        de_para['ddd_EX'] = de_para['ddd']
        de_para = de_para.explode('ddd_EX')
        de_para = de_para.rename(columns={'ddd_EX': 'DE', 'ddd': 'PARA'})
        
        # Explodir df
        df = df.explode('ddd')
        
        # Mesclar DataFrames
        try:
            df_merged = pd.merge(df, total_exp, on='ddd', how='outer')
            df_merged = pd.merge(df_merged, inuse_exp, on='ddd', how='outer')
            df_merged = pd.merge(df_merged, free_exp, on='ddd', how='outer')
        except Exception as e:
            print(f"Erro ao mesclar DataFrames: {e}")
            return estoque
            
        # Verificar se o DataFrame mesclado tem dados
        if df_merged.empty or 'Disponivel' not in df_merged.columns:
            print("DataFrame mesclado vazio ou sem coluna 'Disponivel'")
            return estoque
            
        # Filtrar e tratar dados
        df_filtered = df_merged[df_merged['Disponivel'] > 0]
        
        if df_filtered.empty:
            print("Nenhum registro disponível após filtragem")
            return estoque
            
        # Tratar valores
        df_filtered['Disponivel'] = df_filtered['Disponivel'].replace([float('nan'), float('inf'), -float('inf')], 0).astype(int)
        df_filtered['Em_Uso'] = df_filtered['Em_Uso'].replace([float('nan'), float('inf'), -float('inf')], 0).astype(int)
        df_filtered['Total'] = df_filtered['Total'].replace([float('nan'), float('inf'), -float('inf')], 0).astype(int)
        df_filtered['ddd'] = df_filtered['ddd'].replace([float('nan'), float('inf'), -float('inf')], 0).astype(int)
        
        # Atribuir ao estoque
        estoque = df_filtered
        
        # Adicionar data
        data = (datetime.now() - timedelta(days=1)).date()
        estoque['Data'] = data
        
    except Exception as e:
        print(f"Erro não tratado: {e}")
        # Estoque já foi inicializado como DataFrame vazio
    
    # Retorna estoque (seja vazio ou preenchido)
    return estoque
