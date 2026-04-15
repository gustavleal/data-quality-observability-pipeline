-- Query de Monitoramento 

WITH DataQualityAudit AS (
    SELECT 
        DATE(event_timestamp) AS audit_date,
        COUNT(*) AS total_records,
        SUM(CASE WHEN is_valid = TRUE THEN 1 ELSE 0 END) AS valid_records,
        SUM(CASE WHEN is_valid = FALSE THEN 1 ELSE 0 END) AS failed_records,
        SUM(CASE WHEN transaction_id IS NULL THEN 1 ELSE 0 END) AS null_id_errors,
        SUM(CASE WHEN amount < 0 THEN 1 ELSE 0 END) AS anomaly_errors
    FROM analytics_db.transactions_audit_log
    GROUP BY 1
)
SELECT 
    audit_date,
    total_records,
    valid_records,
    failed_records,
    ROUND((valid_records::decimal / total_records) * 100, 2) AS reliability_score_pct,
    
    CASE 
        WHEN null_id_errors > anomaly_errors THEN 'Missing IDs'
        WHEN anomaly_errors > 0 THEN 'Negative Values / Anomaly'
        ELSE 'Healthy'
    END AS primary_issue_tag
FROM DataQualityAudit
ORDER BY audit_date DESC;
