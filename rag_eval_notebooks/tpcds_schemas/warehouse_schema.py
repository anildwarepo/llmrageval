from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
warehouse_schema = StructType([
    StructField("w_warehouse_sk", IntegerType(), True),
    StructField("w_warehouse_id", StringType(), True),
    StructField("w_warehouse_name", StringType(), True),
    StructField("w_warehouse_sq_ft", IntegerType(), True),
    StructField("w_street_number", StringType(), True),
    StructField("w_street_name", StringType(), True),
    StructField("w_street_type", StringType(), True),
    StructField("w_suite_number", StringType(), True),
    StructField("w_city", StringType(), True),
    StructField("w_county", StringType(), True),
    StructField("w_state", StringType(), True),
    StructField("w_zip", StringType(), True),
    StructField("w_country", StringType(), True),
    StructField("w_gmt_offset", DecimalType(5, 2), True),
])
