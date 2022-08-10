drop_order_detail_table = '''
DROP TABLE IF EXISTS order_detail;
'''

create_order_detail_table = '''
CREATE TABLE IF NOT EXISTS order_detail (
    order_created_timestamp TIMESTAMP,
    status VARCHAR,
    price INT,
    discount FLOAT,
    id VARCHAR PRIMARY KEY NOT NULL,
    driver_id VARCHAR,
    user_id VARCHAR,
    restaurant_id VARCHAR
);'''

copy_order_detail_data = '''
COPY order_detail FROM '/var/lib/postgresql/data/lmwn/order_detail.csv' DELIMITER ',' CSV HEADER;
'''

drop_restaurant_detail_table = '''
DROP TABLE IF EXISTS restaurant_detail;
'''

create_restaurant_detail_table = '''
CREATE TABLE IF NOT EXISTS restaurant_detail (
    id VARCHAR PRIMARY KEY NOT NULL,
    restaurant_name VARCHAR,
    category VARCHAR,
    estimated_cooking_time FLOAT,
    latitude FLOAT,
    longitude FLOAT
);'''

copy_restaurant_detail_data = '''
COPY restaurant_detail FROM '/var/lib/postgresql/data/lmwn/restaurant_detail.csv' DELIMITER ',' CSV HEADER;
'''

drop_order_table = '''
DROP TABLE IF EXISTS orders;
'''

create_order_table ='''
CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(225),
    date DATE,
    product_name VARCHAR(225),
    quantity INT);
'''

copy_order_data ='''
LOAD DATA INFILE '/var/lib/mysql/data/test/Orders.csv' INTO TABLE orders FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
'''

postgres_data_quality_check = {
    "SELECT COUNT(*) FROM order_detail;" : 395361,
    "SELECT COUNT(*) FROM restaurant_detail;" : 12623
}
