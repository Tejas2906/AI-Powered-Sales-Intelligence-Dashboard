CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    full_date DATE,
    day_name VARCHAR(10),
    month_name VARCHAR(10),
    quarter VARCHAR(2),
    year INT,
    is_weekend BIT
);


INSERT INTO dim_date (date_id, full_date, day_name, month_name, quarter, year, is_weekend)
VALUES
(20260101, '2026-01-01', 'Thursday', 'January', 'Q1', 2026, 0),
(20260102, '2026-01-02', 'Friday', 'January', 'Q1', 2026, 0),
(20260103, '2026-01-03', 'Saturday', 'January', 'Q1', 2026, 1),
(20260104, '2026-01-04', 'Sunday', 'January', 'Q1', 2026, 1);


SELECT * FROM dim_date;
