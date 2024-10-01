from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
customer_demographics_schema = StructType([
    StructField("cd_demo_sk", IntegerType(), True),
    StructField("cd_gender", StringType(), True),
    StructField("cd_marital_status", StringType(), True),
    StructField("cd_education_status", StringType(), True),
    StructField("cd_purchase_estimate", IntegerType(), True),
    StructField("cd_credit_rating", StringType(), True),
    StructField("cd_dep_count", IntegerType(), True),
    StructField("cd_dep_employed_count", IntegerType(), True),
    StructField("cd_dep_college_count", IntegerType(), True),
])