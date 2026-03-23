USE Sales_GenAI_Analytics;

CREATE TABLE dim_product (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50),
    price_range VARCHAR(20)
);

INSERT INTO dim_product (product_name, category, brand, price_range)
VALUES
('Mobile Phone', 'Electronics', 'Samsung', 'Medium'),
('Laptop', 'Electronics', 'Dell', 'High'),
('Smart TV', 'Electronics', 'LG', 'High'),
('Washing Machine', 'Home Appliances', 'Whirlpool', 'Medium'),
('T-Shirt', 'Fashion', 'Reliance', 'Low'),
('Shoes', 'Fashion', 'Puma', 'Medium');


SELECT * FROM dim_product;


UPDATE dim_product
SET category =
CASE
WHEN product_name IN ('Laptop','Desktop Computer','Tablet','Printer','Router','Smart Watch','Camera','Gaming Console','Headphones','Bluetooth Speaker') THEN 'Electronics'
WHEN product_name IN ('Refrigerator','Microwave Oven','Air Conditioner','Water Purifier','Vacuum Cleaner','Mixer Grinder') THEN 'Home Appliances'
WHEN product_name IN ('Sneakers','Sports Shoes','Jeans','Handbag','Watch') THEN 'Fashion'
WHEN product_name IN ('Dining Table','Office Chair','Study Table','Bookshelf','Wardrobe','Sofa Set') THEN 'Furniture'
WHEN product_name IN ('Atta (Wheat Flour)','Rice Bag','Coffee Powder','Toothpaste','Soap','Cooking Oil') THEN 'Grocery'
ELSE 'Others'
END;

UPDATE dim_product
SET brand =
CASE
WHEN category = 'Electronics' THEN 'Samsung'
WHEN category = 'Home Appliances' THEN 'LG'
WHEN category = 'Fashion' THEN 'Nike'
WHEN category = 'Furniture' THEN 'IKEA'
WHEN category = 'Grocery' THEN 'Local Brand'
ELSE 'Generic'
END;

UPDATE dim_product
SET price_range =
CASE
WHEN category = 'Electronics' THEN 'High'
WHEN category = 'Home Appliances' THEN 'High'
WHEN category = 'Furniture' THEN 'Medium'
WHEN category = 'Fashion' THEN 'Medium'
WHEN category = 'Grocery' THEN 'Low'
ELSE 'Medium'
END;



SELECT * FROM dim_product;
