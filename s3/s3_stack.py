from aws_cdk import (
    # Duration,
    Stack,
    aws_s3 as s3
    # aws_sqs as sqs,
)
from constructs import Construct
import aws_cdk as cdk


class S3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "S3Queue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        bucket = s3.Bucket(self, "MyFirstBucket",
            versioned=True,
            access_control=s3.BucketAccessControl.BUCKET_OWNER_FULL_CONTROL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=cdk.RemovalPolicy.DESTROY,
            auto_delete_objects=True,
            # create a lifecycle rule to move to objects glacier after 1 day
            lifecycle_rules=[
                s3.LifecycleRule(
                    expiration=cdk.Duration.days(180),
                    transitions=[
                        s3.Transition(
                            storage_class=s3.StorageClass.GLACIER,
                            transition_after=cdk.Duration.days(1),
                        ),
                        s3.Transition(
                            storage_class=s3.StorageClass.DEEP_ARCHIVE,
                            transition_after=cdk.Duration.days(92),
                        ),
                        
                    ]
                )
            ]
        )

        # grant read/write permissions to the bucket
        

