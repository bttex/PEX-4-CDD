from plugins.selenium_plugin import (
    start_selenium_driver,
    interact_with_page,
    get_token,
    close_driver,
)
from plugins.curl_plugin import fetch_data
from plugins.data_processing_plugin import process_data
from plugins.bigquery_plugin import (
    truncate_claroesim,
    execute_procedure_deal,
    insert_data_to_bigquery,
)
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")


def run():
    # Passo 1: Iniciar o driver do Selenium e interagir com a página
    driver = start_selenium_driver()
    interact_with_page(driver)

    # Passo 2: Obter o token
    token = get_token(driver)

    # Passo 3: Fechar o driver
    close_driver(driver)

    # Passo 4: Executar o comando curl e obter os dados
    url = f"{API_URL}/esim/lastquantity"
    dados_json = fetch_data(token, url)

    # Passo 5: Processar os dados
    estoque = process_data(dados_json)

    # Passo 6: Enviar para o BigQuery
    project_id = "SEU_PROJECT_ID_AQUI"
    table_id = "SEU_DATASET.SEUS_TABELA_AQUI"
    truncate_claroesim(table_id)
    insert_data_to_bigquery(estoque, table_id, project_id)

    # Passo 7: Executar procedure no BigQuery
    procedure_name = "SUA_PROCEDURE_AQUI"
    execute_procedure_deal(project_id, procedure_name)

    print("Processo concluído com sucesso!")


if __name__ == "__main__":
    run()
