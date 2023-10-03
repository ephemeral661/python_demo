import time


def mock_api_call():
    time.sleep(0.5)


def fetch_security_master_data(security_id):
    mock_api_call()

    # Hardcoded mock data for demonstration, all the data is fictional
    security_data = {
        'T001': {
            'security_id': 'T001',
            'security_name': 'Apple Inc.',
            'ticker': 'AAPL',
            'exchange': 'NASDAQ'
        },
        'T002': {
            'security_id': 'T002',
            'security_name': 'Microsoft Corp.',
            'ticker': 'MSFT',
            'exchange': 'NASDAQ'
        },
    }

    return security_data.get(security_id, {})


def fetch_issuer_data(issuer_id):
    mock_api_call()

    # Hardcoded mock data for demonstration
    issuer_data = {
        'Apple': {
            'issuer_id': 'Apple',
            'issuer_name': 'Apple Inc.',
            'sector': 'Technology',
            'industry': 'Consumer Electronics'
        },
        'Microsoft': {
            'issuer_id': 'Microsoft',
            'issuer_name': 'Microsoft Corporation',
            'sector': 'Technology',
            'industry': 'Software'
        },
        # Add more mock data as needed
    }

    return issuer_data.get(issuer_id, {})


# Testing the functions
if __name__ == "__main__":
    security_data = fetch_security_master_data('T001')
    print(security_data)

    issuer_data = fetch_issuer_data('Apple')
    print(issuer_data)
