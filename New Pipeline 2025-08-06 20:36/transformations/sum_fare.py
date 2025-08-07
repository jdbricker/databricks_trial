import dlt
from pyspark.sql.functions import col, sum


# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.


@dlt.table
def sum_fare():
    # Read from the "sample_trips" table, then sum all the fares
    return (
        spark.read.table("sample_zones_aug_6_2036")
        .agg(
            sum("total_fare").alias("total_fare")
        )
    )