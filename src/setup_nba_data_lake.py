import json
import time
import requests
import os

from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

load_dotenv()

class NBADataLake:
  def __init__(self):
    """Initialize the Data lake with necessary configurations"""
    self.api_key = os.getenv("SPORTS_API_KEY")
    self.connect_str = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

    self.container_name = "NBA-data"
    self.blob_service_client = BlobServiceClient.from_connection_string(self.connect_str)
    self._create_container_if_not_exists()

  def _create_container_if_not_exists(self):
    """Ensure the Blob container exists, creating it if necessary."""
    container_client = self.blob_service_client.get_container_client(self.container_name)
    if not container_client.exists():
      container_client.create_container()
      print(f"Container '{self.container_name}' created.")

  def upload_to_blob(self, blob_name, data):
    """Upload data to the Blob storage."""
    try:
      blob_client = self.blob_service_client.get_blob_client(self.container_name, blob_name)
      blob_client.upload_blob(data, overwrite=True)
      print(f"Data uploaded to Blob: {blob_name}")
    except Exception as e:
      print(e)
  
  def fetch_nba_data(self, endpoint):
    """Fetch data from the NBA API."""
    url = f"https://api.sportsdata.io/v3/nba/stats/json/{endpoint}"
    headers = {
      "Ocp-Apim-Subscription-Key": self.api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()