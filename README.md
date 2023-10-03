# Investment Data Integration Tool

This tool is a simple Python project that showcases the process of extracting, transforming, and loading (ETL) investment data from a CSV file into a SQLite database, as well as simulating API calls to fetch security and issuer data.

If successfully ran, it should generate a .db file that the 'amount' column has been changed to float, and print out security master data for demonstration purposes (since we don't have access to an real API like Bloomberg or Security Master here).

## Features

1. **ETL Process**: Extract data from a sample CSV file, transform it, and load into a SQLite database.
2. **Mock API Calls**: Simulate fetching security and issuer data via mock API functions.

## Prerequisites

- Python 3.x
- SQLite (included in the Python standard library)

## Directory Structure
- **InvestmentDataIntegrationTool/**
  - **main.py**               # Main driver script
  - **etl.py**                # Contains ETL process functions
  - **database.py**           # Handles SQLite database operations
  - **api_connector.py**      # Mock API calls for fetching security and issuer data
  - **utils/**                # Directory for utility scripts and shared

