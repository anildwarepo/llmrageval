from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
web_page_schema = StructType([
    StructField("wp_web_page_sk", IntegerType(), True),
    StructField("wp_web_page_id", StringType(), True),
    StructField("wp_rec_start_date", DateType(), True),
    StructField("wp_rec_end_date", DateType(), True),
    StructField("wp_creation_date_sk", IntegerType(), True),
    StructField("wp_access_date_sk", IntegerType(), True),
    StructField("wp_autogen_flag", StringType(), True),
    StructField("wp_customer_sk", IntegerType(), True),
    StructField("wp_url", StringType(), True),
    StructField("wp_type", StringType(), True),
    StructField("wp_char_count", IntegerType(), True),
    StructField("wp_link_count", IntegerType(), True),
    StructField("wp_image_count", IntegerType(), True),
    StructField("wp_max_ad_count", IntegerType(), True),
])