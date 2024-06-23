from reclaim_sdk.client import ReclaimClient
from reclaim_sdk.models.task import ReclaimTask
import os

token = os.getenv("RECLAIM_TOKEN")

reclaim_client = ReclaimClient(token=token)

task = ReclaimTask.search(title="test_task_01")
print(task)