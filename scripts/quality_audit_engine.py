import pandas as pd
import numpy as np

def run_data_quality_checks(df):
    print("--- INICIANDO AUDITORIA DE QUALIDADE DE DADOS ---")
    
    null_count = df['transaction_id'].isnull().sum()
    print(f"[CHECK] Valores nulos em transaction_id: {null_count}")
    
    duplicate_count = df.duplicated(subset=['transaction_id']).sum()
    print(f"[CHECK] Registros duplicados encontrados: {duplicate_count}")
    
    negative_values = df[df['amount'] < 0].shape[0]
    print(f"[CHECK] Transações com valores negativos (Anomalias): {negative_values}")
    
    df['is_valid'] = np.where(
        (df['transaction_id'].notnull()) & 
        (~df.duplicated(subset=['transaction_id'])) & 
        (df['amount'] >= 0), 
        True, False
    )
    
    return df

dados_sujos = {
    'transaction_id': ['TX-100', 'TX-101', 'TX-101', None, 'TX-102'],
    'amount': [150.00, 200.00, 200.00, 50.00, -10.00],
    'event_timestamp': ['2026-04-10 10:00', '2026-04-10 10:05', '2026-04-10 10:05', '2026-04-10 10:10', '2026-04-10 10:15']
}

df_raw = pd.DataFrame(dados_sujos)

df_audited = run_data_quality_checks(df_raw)

df_gold = df_audited[df_audited['is_valid'] == True]
df_quarantine = df_audited[df_audited['is_valid'] == False]

print(f"\n[FINALIZADO] Registros Aprovados: {len(df_gold)}")
print(f"[FINALIZADO] Registros em Quarentena: {len(df_quarantine)}")

# Simulação de envio para AWS S3
# df_gold.to_parquet("s3://datalake/gold/transactions/")
# df_quarantine.to_csv("s3://datalake/quarantine/anomalies_log.csv")
