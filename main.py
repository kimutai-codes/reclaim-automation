from reclaim_sdk.client import ReclaimClient
from reclaim_sdk.models.task import ReclaimTask
from datetime import datetime, timedelta

# Replace with your actual Reclaim API token

reclaim_client = ReclaimClient(token="d57aeb4a-8f92-4658-ad19-a7955a818815")

task = ReclaimTask()

task.name = "test_task_01"
task.duration = 0.25
task.min_work_duration = 0.75
task.max_work_duration = 2
task.start_date = datetime.now() + timedelta(days=3)
task.due_date = datetime.now() + timedelta(days=5)

# Then the object needs to be saved manually to the API.
task.save()
print(task)