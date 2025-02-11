# 30 Days DevOps Challenge - NBA Data Lake
Day 3: Building a building a Sports Data Lake leveraging Azure blob storage, and Synapse Analytics

# NBA Data Lake - DevOps Day 3 Challenge
![Project Structure](./DevopsChallenge_day01.drawio.png)


## Project Overview
This project demonstrates how to build a data pipeline for NBA sports analytics using Azure services. The pipeline fetches NBA player data from an API, stores it in Azure Blob Storage, and creates a queryable table in Azure Synapse Analytics. The data can then be queried and processed using any tool.

## Features
- Data Ingestion: Fetch NBA player data from the sportsdata.io API.
- Data Storage: Store raw JSON data in Azure Blob Storage.
- Schema Inference: Create a table in Azure Synapse Analytics with an inferred schema.
- Data Querying: Query the table using SQL.

## Prerequisites
- Python 3.x
- Azure Account: An active Azure subscription.
- Azure Blob Storage: To store raw JSON data.
- Azure Synapse Analytics: To create and query tables.
- SportsData API key

## Dependencies
- azure-storage-blob
- azure-synapse-spark
- requests
- python-dotenv
- pyodbc

## Project Structure
```shell
03_NBADataLake/
├── src/
│   ├── __init__.py
│   └── setup_nba_data_lake.py
├── .env
├── .gitignore
├── .env
├── requirements.txt
└── README.md
```

## Running the application
1. Clone the repository
    ```shell
    git clone git@github.com:Jekwulum/03_NBADataLake.git
    cd 03_NBADataLake
    ```
2. Create a virtual environment:
   ```shell
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows use `.venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```shell
   pip install -r requirements.txt
   ```
4. Configure environment variables (.env):
   ```shell
    # Azure configurations
    AZURE_STORAGE_ACCOUNT_NAME=your_storage_account_name
    AZURE_STORAGE_ACCOUNT_KEY=your_storage_account_key
    SYNAPSE_ENDPOINT=your_synapse_endpoint
    SYNAPSE_SPARK_POOL=your_spark_pool_name

    SYNAPSE_SERVER="<synapse_workspace_name>.sql.azuresynapse.net"
    SYNAPSE_DATABASE="<database_name>"
    SYNAPSE_USERNAME="<username>"
    SYNAPSE_PASWORD="<password>"

    # Sportsdata.io configurations
    SPORTS_DATA_API_KEY=your_api_key
    NBA_ENDPOINT=your_nba_endpoint
  ```
5. Run the application:
   ```shell
   python src/setup_nba_data_lake.py
   ```

## What I learned
- Azure Blob storage container creation and management
- Environment variable management for secure API keys
- Python best practices for API integration
- Git workflow for project development
- Error handling in distributed systems
- Cloud resource management

## Future Enhancements
- Add weather forecasting
- Implement data visualization
- Add more cities
- Create automated testing
- Set up CI/CD pipeline