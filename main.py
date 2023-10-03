from database import init_db
from etl import run_complete_etl_demo, create_sample_data
from api_connector import fetch_security_master_data, fetch_issuer_data


def main():
    # 1. Initialize the database
    init_db()

    # 2. Generate and process sample data using ETL
    run_complete_etl_demo()

    # 3. Mock API Integration
    security_id_sample = "T001"  
    issuer_id_sample = "Apple" 

    # Fetch and print security master data (since we don't have access to a real API, just have to print it out)
    security_data = fetch_security_master_data(security_id_sample)
    print(f"\nSecurity Master Data for {security_id_sample}:")
    print(security_data)

    # Fetch and print issuer data
    issuer_data = fetch_issuer_data(issuer_id_sample)
    print(f"\nIssuer Data for {issuer_id_sample}:")
    print(issuer_data)


if __name__ == "__main__":
    main()


