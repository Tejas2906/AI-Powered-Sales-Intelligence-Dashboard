

CREATE TABLE ai_summary (
    id INT IDENTITY(1,1) PRIMARY KEY,
    performance_overview NVARCHAR(MAX),
    growth_drivers NVARCHAR(MAX),
    risk_areas NVARCHAR(MAX),
    recommendations NVARCHAR(MAX),
    generated_at DATETIME DEFAULT GETDATE()
);

SELECT TOP 1 * FROM ai_summary ORDER BY generated_at DESC;

IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ai_summary' AND xtype='U')
CREATE TABLE ai_summary (
    id INT IDENTITY(1,1) PRIMARY KEY,
    performance_overview NVARCHAR(MAX),
    growth_drivers NVARCHAR(MAX),
    risk_areas NVARCHAR(MAX),
    recommendations NVARCHAR(MAX),
    risk_score INT,
    generated_at DATETIME DEFAULT GETDATE()
);

ALTER TABLE ai_summary
ADD risk_score INT;


SELECT TOP 1 * FROM ai_summary
ORDER BY generated_at DESC;

