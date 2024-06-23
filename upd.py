from reclaim_sdk.client import ReclaimClient
from reclaim_sdk.models.task_event import ReclaimTaskEvent
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("RECLAIM_TOKEN")


# Initialize the Reclaim client with your token
reclaim_client = ReclaimClient(token=token)

# Define the actual event ID (replace with the one you found)
actual_event_id = "e9im6r31d5miqobjedkn6t1dehgn6qpqeoojkdho60oj8c1o78o0"  # Example ID, replace with your actual ID

# Define the event data with the correct event ID
event_data = {
    "start": "2024-06-23T09:16:19+00:00",
    "end": "2024-06-23T10:16:19+00:00",  # Assuming end time is required
    "eventId": actual_event_id
}

# Initialize the ReclaimTaskEvent instance with valid task ID and data
task_id = 6801408
task_event = ReclaimTaskEvent(data=event_data, task=task_id)

# Update the event (this will trigger the start update)
try:
    task_event._update()
    print("Event updated successfully.")
except Exception as e:
    print(f"Error updating event: {e}")
