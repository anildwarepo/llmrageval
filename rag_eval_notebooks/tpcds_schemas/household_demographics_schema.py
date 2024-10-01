from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
household_demographics_schema = StructType([
    StructField("hd_demo_sk", IntegerType(), True),
    StructField("hd_income_band_sk", IntegerType(), True),
    StructField("hd_buy_potential", StringType(), True),
    StructField("hd_dep_count", IntegerType(), True),
    StructField("hd_vehicle_count", IntegerType(), True),
])