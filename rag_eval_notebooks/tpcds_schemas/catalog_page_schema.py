from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
catalog_page_schema = StructType([
    StructField("cp_catalog_page_sk", IntegerType(), True),
    StructField("cp_catalog_page_id", StringType(), True),
    StructField("cp_start_date_sk", IntegerType(), True),
    StructField("cp_end_date_sk", IntegerType(), True),
    StructField("cp_department", StringType(), True),
    StructField("cp_catalog_number", IntegerType(), True),
    StructField("cp_catalog_page_number", IntegerType(), True),
    StructField("cp_description", StringType(), True),
    StructField("cp_type", StringType(), True),
])