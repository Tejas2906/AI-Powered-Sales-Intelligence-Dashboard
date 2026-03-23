CREATE TABLE dim_customer (
    customer_id INT IDENTITY(1,1) PRIMARY KEY,
    gender VARCHAR(10),
    age_group VARCHAR(20),
    segment VARCHAR(50),
    loyalty_level VARCHAR(20)
);

INSERT INTO dim_customer (gender, age_group, segment, loyalty_level)
VALUES
('Male', '18-25', 'Retail', 'Silver'),
('Female', '26-35', 'Retail', 'Gold'),
('Male', '36-45', 'Corporate', 'Platinum'),
('Female', '26-35', 'Retail', 'Gold'),
('Male', '46-55', 'Corporate', 'Silver');

SELECT * FROM dim_customer;
