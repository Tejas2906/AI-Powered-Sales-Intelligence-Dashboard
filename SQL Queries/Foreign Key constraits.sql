
ALTER TABLE fact_sales
ADD CONSTRAINT fk_product
FOREIGN KEY (product_id) REFERENCES dim_product(product_id);

ALTER TABLE fact_sales
ADD CONSTRAINT fk_customer
FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id);

ALTER TABLE fact_sales
ADD CONSTRAINT fk_region
FOREIGN KEY (region_id) REFERENCES dim_region(region_id);

ALTER TABLE fact_sales
ADD CONSTRAINT fk_date
FOREIGN KEY (date_id) REFERENCES dim_date(date_id);

ALTER TABLE fact_sales
ADD CONSTRAINT fk_channel
FOREIGN KEY (channel_id) REFERENCES dim_channel(channel_id);

ALTER TABLE fact_sales
ADD CONSTRAINT fk_promotion
FOREIGN KEY (promotion_id) REFERENCES dim_promotion(promotion_id);
