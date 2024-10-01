from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
reason_schema = StructType([
    StructField("r_reason_sk", IntegerType(), True),
    StructField("r_reason_id", StringType(), True),
    StructField("r_reason_desc", StringType(), True),
])