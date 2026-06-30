SELECT 
    CAST(from_unixtime(unix) AS DATE) AS fecha_formateada,
    symbol AS activo,
    ROUND(close, 2) AS precio_cierre,
    ROUND("Volume USD", 2) AS volumen_total_usd
FROM "raw"
WHERE "Volume USD" IS NOT NULL
ORDER BY "Volume USD" DESC
LIMIT 5;
