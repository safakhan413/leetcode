# Import your libraries
import pyspark
from pyspark.sql.functions import col



# Start writing code
# forbes_global_2010_2014
# df = forbes_global_2010_2014.select(["company", "profits"])
# df = df.orderBy(col('profits').desc())
# df = df.limit(3)
# df.show()


df = forbes_global_2010_2014.select("company", "profits")

# Sort by profits in descending order
df = df.orderBy(col('profits').desc())

# Limit to the top 3
df = df.limit(3)
result = df.toPandas()