import csv
import sqlite3

DATABASE_NAME = "investment_data.db"

#Creating some sample data and load into an Empty CSV file (sample_data.csv)
def create_sample_data():
    sample_data = """trade_id,security_name,amount,date,issuer,corporate_action
T001,Apple Inc.,5000.50,2023-10-01,Apple,None
T002,Microsoft Corp.,3000.25,2023-10-01,Microsoft,Dividend Issued
T003,Amazon.com Inc.,4200.75,2023-10-02,Amazon,None
T004,Google LLC,3800.10,2023-10-02,Google,Stock Split
T005,Facebook Inc.,2900.20,2023-10-03,Meta,None
"""

    with open("sample_data.csv", "w") as file:
        file.write(sample_data)


def run_complete_etl_demo():
    create_sample_data()
    run_etl_process("sample_data.csv")


# extract data from CSV file
def extract_data(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


# For demonstration, let's consider there's a field 'amount' which needs to be converted to float.
def transform_data(data):
    for item in data:
        item['amount'] = float(item['amount'])  # just an example of data transformation, in real world practice, this could be much more complicated
    return data


# Loading the data into SQLite database
def load_data(data, database):
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        for item in data:
            cursor.execute("""
                INSERT INTO Trades (trade_id, security_name, amount, date, issuer, corporate_action)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (item['trade_id'], item['security_name'], item['amount'], item['date'], item['issuer'],
                  item['corporate_action']))
        conn.commit()


# Main
def run_etl_process(filename):
    data = extract_data(filename)
    transformed_data = transform_data(data)
    load_data(transformed_data, DATABASE_NAME)
