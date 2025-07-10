USE phonepe;
-- Aggregated Tables
CREATE TABLE aggregated_user (
    state VARCHAR(100),
    year INT,
    quarter INT,
    brand VARCHAR(100),
    count BIGINT,
    percentage DECIMAL(10,2)
);


CREATE TABLE aggregated_transaction (
    state VARCHAR(100),
    year INT,
    quarter INT,
    transaction_type VARCHAR(100),
    count BIGINT,
    amount DECIMAL(20,2)
);


CREATE TABLE aggregated_insurance (
    state VARCHAR(100),
    year INT,
    quarter INT,
    insurance_type VARCHAR(100),
    count BIGINT,
    amount DECIMAL(20,2)
);


-- Map Tables
CREATE TABLE map_user (
    state VARCHAR(100),
    district VARCHAR(100),
    year INT,
    quarter INT,
    registered_users BIGINT,
    app_opens BIGINT
);


CREATE TABLE map_map (
    state VARCHAR(100),
    district VARCHAR(100),
    year INT,
    quarter INT,
    transaction_type VARCHAR(100),
    count BIGINT,
    amount DECIMAL(20,2)
);


CREATE TABLE map_insurance (
    state VARCHAR(100),
    district VARCHAR(100),
    year INT,
    quarter INT,
    insurance_type VARCHAR(100),
    count BIGINT,
    amount DECIMAL(20,2)
);



-- Top Tables
CREATE TABLE top_user (
    state VARCHAR(100),
    year INT,
    quarter INT,
    pincode INT,
    registered_users BIGINT
);



CREATE TABLE top_map (
    state VARCHAR(100),
    year INT,
    quarter INT,
    location_type VARCHAR(100),
    location_name VARCHAR(100),
    count BIGINT,
    amount DECIMAL(20,2)
);


CREATE TABLE top_insurance (
    state VARCHAR(100),
    year INT,
    quarter INT,
    insurance_type VARCHAR(100),
    count BIGINT,
    amount DECIMAL(20,2)
);
