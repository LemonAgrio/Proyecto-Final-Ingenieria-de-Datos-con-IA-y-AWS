import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1782846781324 = glueContext.create_dynamic_frame.from_catalog(database="fintech_db", table_name="smartdata_projectofinal_royalarcon", transformation_ctx="AWSGlueDataCatalog_node1782846781324")

# Script generated for node Change Schema
ChangeSchema_node1782846794971 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1782846781324, mappings=[("time", "long", "date", "timestamp"), ("v3", "double", "open", "double"), ("v4", "double", "high", "double"), ("v5", "double", "low", "double"), ("v6", "double", "close", "double"), ("v7", "double", "volume btc", "double"), ("v8", "double", "volume  usd", "double")], transformation_ctx="ChangeSchema_node1782846794971")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=ChangeSchema_node1782846794971, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1782846764975", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1782846820779 = glueContext.write_dynamic_frame.from_options(frame=ChangeSchema_node1782846794971, connection_type="s3", format="glueparquet", connection_options={"path": "s3://smartdata-projectofinal-royalarcon", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="AmazonS3_node1782846820779")

job.commit()
