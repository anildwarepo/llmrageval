from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
customer_address_schema = StructType([
    StructField("ca_address_sk", IntegerType(), True),
    StructField("ca_address_id", StringType(), True),
    StructField("ca_street_number", StringType(), True),
    StructField("ca_street_name", StringType(), True),
    StructField("ca_street_type", StringType(), True),
    StructField("ca_suite_number", StringType(), True),
    StructField("ca_city", StringType(), True),
    StructField("ca_county", StringType(), True),
    StructField("ca_state", StringType(), True),
    StructField("ca_zip", StringType(), True),
    StructField("ca_country", StringType(), True),
    StructField("ca_gmt_offset", DecimalType(5, 2), True),
    StructField("ca_location_type", StringType(), True),
])