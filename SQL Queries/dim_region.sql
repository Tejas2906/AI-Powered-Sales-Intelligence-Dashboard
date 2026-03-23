CREATE TABLE dim_region (
    region_id INT IDENTITY(1,1) PRIMARY KEY,
    region_name VARCHAR(50),
    state VARCHAR(50),
    city VARCHAR(50),
    country VARCHAR(50)
);

INSERT INTO dim_region (region_name, state, city, country)
VALUES
('West', 'Maharashtra', 'Mumbai', 'India'),
('West', 'Maharashtra', 'Pune', 'India'),
('South', 'Karnataka', 'Bengaluru', 'India'),
('South', 'Tamil Nadu', 'Chennai', 'India'),
('North', 'Delhi', 'New Delhi', 'India'),
('East', 'West Bengal', 'Kolkata', 'India');


UPDATE dim_region
SET region_name =
CASE
WHEN state IN ('Maharashtra','Gujarat') THEN 'West'
WHEN state IN ('Karnataka','Tamil Nadu','Kerala','Telangana','Andhra Pradesh') THEN 'South'
WHEN state IN ('Delhi','Punjab','Haryana','Uttar Pradesh','Rajasthan') THEN 'North'
WHEN state IN ('West Bengal','Odisha','Assam','Bihar') THEN 'East'
ELSE 'Central'
END;

UPDATE dim_region
SET country = 'India'
WHERE country IS NULL;

UPDATE dim_region
SET state =
CASE
    WHEN city IN ('Mumbai','Pune','Nagpur','Kolhapur') THEN 'Maharashtra'
    WHEN city IN ('Bengaluru','Hubli') THEN 'Karnataka'
    WHEN city IN ('Chennai','Coimbatore') THEN 'Tamil Nadu'
    WHEN city IN ('Delhi','Noida','Gurgaon','Faridabad') THEN 'Delhi NCR'
    WHEN city IN ('Kolkata') THEN 'West Bengal'
    WHEN city IN ('Ahmedabad','Surat','Rajkot','Vadodara') THEN 'Gujarat'
    WHEN city IN ('Hyderabad','Warangal') THEN 'Telangana'
    WHEN city IN ('Visakhapatnam','Vijayawada','Guntur') THEN 'Andhra Pradesh'
    WHEN city IN ('Lucknow','Agra','Kanpur','Varanasi') THEN 'Uttar Pradesh'
    WHEN city IN ('Patna') THEN 'Bihar'
    WHEN city IN ('Bhopal','Indore') THEN 'Madhya Pradesh'
    WHEN city IN ('Jaipur','Kota','Udaipur') THEN 'Rajasthan'
    WHEN city IN ('Chandigarh','Ludhiana') THEN 'Punjab'
    WHEN city IN ('Srinagar') THEN 'Jammu & Kashmir'
    WHEN city IN ('Kochi') THEN 'Kerala'
    WHEN city IN ('Panaji') THEN 'Goa'
    WHEN city IN ('Bhubaneswar','Cuttack') THEN 'Odisha'
    WHEN city IN ('Dibrugarh','Guwahati') THEN 'Assam'
    WHEN city IN ('Shimla') THEN 'Himachal Pradesh'
    WHEN city IN ('Raipur') THEN 'Chhattisgarh'
    ELSE state
END;

UPDATE dim_region
SET state = 
CASE 
    WHEN city = 'Mangalore' THEN 'Karnataka'
    WHEN city = 'Panipat' THEN 'Haryana'
    WHEN city = 'Kozhikode' THEN 'Kerala'
    WHEN city = 'Durgapur' THEN 'West Bengal'
    WHEN city = 'Madurai' THEN 'Tamil Nadu'
    WHEN city = 'Ranchi' THEN 'Jharkhand'
END
WHERE state IS NULL;



SELECT * FROM dim_region;