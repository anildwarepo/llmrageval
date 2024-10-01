from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
customer_schema = StructType([
    StructField("c_customer_sk", IntegerType(), True),
    StructField("c_customer_id", StringType(), True),
    StructField("c_current_cdemo_sk", IntegerType(), True),
    StructField("c_current_hdemo_sk", IntegerType(), True),
    StructField("c_current_addr_sk", IntegerType(), True),
    StructField("c_first_shipto_date_sk", IntegerType(), True),
    StructField("c_first_sales_date_sk", IntegerType(), True),
    StructField("c_salutation", StringType(), True),
    StructField("c_first_name", StringType(), True),
    StructField("c_last_name", StringType(), True),
    StructField("c_preferred_cust_flag", StringType(), True),
    StructField("c_birth_day", IntegerType(), True),
    StructField("c_birth_month", IntegerType(), True),
    StructField("c_birth_year", IntegerType(), True),
    StructField("c_birth_country", StringType(), True),
    StructField("c_login", StringType(), True),
    StructField("c_email_address", StringType(), True),
    StructField("c_last_review_date", StringType(), True)
])