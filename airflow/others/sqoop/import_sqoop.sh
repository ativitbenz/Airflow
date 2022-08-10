hdfs dfs -rm -r /user/sqoop
hdfs dfs -mkdir /user/sqoop

/usr/lib/sqoop/bin/sqoop import \
--connect jdbc:postgresql://postgres:5432/airflow \
--table order_detail \
--username airflow \
--password airflow \
--num-mappers 1 \
--map-column-hive order_created_timestamp=STRING,status=STRING,price=INT,discount=FLOAT,id=STRING,driver_id=STRING,user_id=STRING,restaurant_id=STRING \
--target-dir /user/sqoop/order_detail \

/usr/lib/sqoop/bin/sqoop import \
--connect jdbc:postgresql://postgres:5432/airflow \
--table restaurant_detail \
--username airflow \
--password airflow \
--num-mappers 1 \
--target-dir /user/sqoop/restaurant_detail \