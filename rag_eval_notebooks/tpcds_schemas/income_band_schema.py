from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
income_band_schema = StructType([
    StructField("ib_income_band_sk", IntegerType(), True),
    StructField("ib_lower_bound", IntegerType(), True),
    StructField("ib_upper_bound", IntegerType(), True),
])