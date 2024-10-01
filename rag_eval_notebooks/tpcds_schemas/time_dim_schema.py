from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
time_dim_schema = StructType([
    StructField("t_time_sk", IntegerType(), True),
    StructField("t_time_id", StringType(), True),
    StructField("t_time", IntegerType(), True),
    StructField("t_hour", IntegerType(), True),
    StructField("t_minute", IntegerType(), True),
    StructField("t_second", IntegerType(), True),
    StructField("t_am_pm", StringType(), True),
    StructField("t_shift", StringType(), True),
    StructField("t_sub_shift", StringType(), True),
    StructField("t_meal_time", StringType(), True),
])