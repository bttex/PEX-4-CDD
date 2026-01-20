from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "json_acesso.json"


def truncate_claroesim(table_id):
    client = bigquery.Client()
    query = f"TRUNCATE TABLE `{table_id}`"
    client.query(query).result()
    print(f"Tabela {table_id} truncada com sucesso!")


def execute_procedure_deal(project_id, procedure_name):
    client = bigquery.Client(project=project_id)
    sql = f"CALL `{project_id}.REPORT.{procedure_name}`();"
    try:
        query_job = client.query(sql)
        query_job.result()  # Aguarda a execução
        print("Procedure executada com sucesso!")
    except Exception as e:
        print(f"Erro ao executar a procedure: {e}")


def insert_data_to_bigquery(df, table_id, project_id):
    df.to_gbq(destination_table=table_id, project_id=project_id, if_exists="append")
    print("Dataframe inserido com sucesso.")
