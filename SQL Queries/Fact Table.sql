CREATE TABLE fact_sales (
    sale_id INT IDENTITY(1,1) PRIMARY KEY,
    sale_timestamp DATETIME,
    date_id INT,
    product_id INT,
    customer_id INT,
    region_id INT,
    channel_id INT,
    promotion_id INT,
    quantity INT,
    revenue DECIMAL(10,2),
    cost DECIMAL(10,2),
    profit DECIMAL(10,2)
);

select * from fact_sales;