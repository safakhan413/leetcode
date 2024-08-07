# Import your libraries
import pyspark
import pyspark.sql.functions as F

from pyspark.sql.window import Window
# Start writing code
worker.show()
# title.show()
title = title.withColumnRenamed("worker_ref_id", "worker_id")

title.show()

joined_worker_title = worker.join(title, on="worker_id")
# joined_worker_title.show()
joined_worker_title = joined_worker_title.groupBy("worker_title").agg(F.max('salary').alias('max_salary')).orderBy(F.desc('max_salary'))

result = joined_worker_title.withColumn('rank', F.rank().over(Window.orderBy(F.desc('max_salary'))))

result= result.select('worker_title').filter(result['rank']==1)
result.toPandas()
