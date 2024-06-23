from reclaim_sdk.client import ReclaimClient
from reclaim_sdk.models.task import ReclaimTask
import os

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("RECLAIM_TOKEN")

reclaim_client = ReclaimClient(token=token)

# task = ReclaimTask.search(title="test_task_01")
task = ReclaimTask.get(6801408)
print(task)