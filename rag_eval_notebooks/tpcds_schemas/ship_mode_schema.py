from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
ship_mode_schema = StructType([
    StructField("sm_ship_mode_sk", IntegerType(), True),
    StructField("sm_ship_mode_id", StringType(), True),
    StructField("sm_type", StringType(), True),
    StructField("sm_code", StringType(), True),
    StructField("sm_carrier", StringType(), True),
    StructField("sm_contract", StringType(), True)
])