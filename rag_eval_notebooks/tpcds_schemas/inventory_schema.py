from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, DecimalType
inventory_schema = StructType([
    StructField("inv_date_sk", IntegerType(), True),
    StructField("inv_item_sk", IntegerType(), True),
    StructField("inv_warehouse_sk", IntegerType(), True),
    StructField("inv_quantity_on_hand", IntegerType(), True),
])