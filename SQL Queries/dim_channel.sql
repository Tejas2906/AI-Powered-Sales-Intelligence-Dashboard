CREATE TABLE dim_channel (
    channel_id INT IDENTITY(1,1) PRIMARY KEY,
    channel_name VARCHAR(20),
    platform VARCHAR(20)
);

INSERT INTO dim_channel (channel_name, platform)
VALUES
('Online', 'Mobile App'),
('Online', 'Website'),
('Offline', 'Retail Store');

SELECT * FROM dim_channel;
