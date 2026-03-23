CREATE TABLE dim_promotion (
    promotion_id INT IDENTITY(1,1) PRIMARY KEY,
    promotion_type VARCHAR(50),
    discount_pct DECIMAL(5,2),
    campaign_name VARCHAR(100)
);


INSERT INTO dim_promotion (promotion_type, discount_pct, campaign_name)
VALUES
('Discount', 10, 'Diwali Sale'),
('Discount', 20, 'New Year Sale'),
('Cashback', 5, 'Independence Day Offer'),
('None', 0, 'No Promotion');

SELECT * FROM dim_promotion;


UPDATE dim_promotion
SET promotion_type =
CASE
WHEN campaign_name LIKE '%Diwali%' THEN 'Discount'
WHEN campaign_name LIKE '%New Year%' THEN 'Discount'
WHEN campaign_name LIKE '%Independence%' THEN 'Cashback'
WHEN campaign_name LIKE '%Black Friday%' THEN 'Discount'
WHEN campaign_name LIKE '%Republic%' THEN 'Discount'
ELSE 'None'
END;


UPDATE dim_promotion
SET discount_pct =
CASE
WHEN campaign_name = 'Black Friday Sale' THEN 30
WHEN campaign_name = 'Republic Day Sale' THEN 15
WHEN discount_pct IS NULL THEN 0
ELSE discount_pct
END;


SELECT * FROM dim_promotion;