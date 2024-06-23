from reclaim_sdk.client import ReclaimAPICall
from reclaim_sdk.models.model import ReclaimModel
from reclaim_sdk.client import ReclaimClient
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("RECLAIM_TOKEN")

# Initialize the Reclaim client with your token
reclaim_client = ReclaimClient(token=token)

if __name__ == "__main__":
    try:
        task_id = "6801408"  # Replace with the actual task ID
        url = f"{reclaim_client._api_url}/api/planner/prioritize/task/{task_id}"
        
        # Using the ReclaimClient instance to make the GET request
        res = reclaim_client.get(url)

        print("Task prioritized successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")