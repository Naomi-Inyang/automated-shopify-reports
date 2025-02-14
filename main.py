from dotenv import load_dotenv
import requests, os

load_dotenv()

SHOPIFY_STORE_DOMAIN = os.getenv('STORE_URL')
API_KEY = os.getenv('API_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')  
SECRET_KEY= os.getenv('SECRET_KEY') 
HEADER_VALUES = {
    'Content-Type': 'application/json', 
    'X-Shopify-Access-Token': ACCESS_TOKEN
}


# def fetch_reports():
#     url = f"{BASE_URL}/reports.json"
#     response = requests.get(url)
#     return response.json() if response.status_code == 200 else response.text

# # Fetch Orders Data (Month-to-Date)
# def fetch_orders():
#     url = f"{BASE_URL}/orders.json?status=any&created_at_min=2024-02-01"
#     response = requests.get(url)
#     return response.json() if response.status_code == 200 else response.text

# # Fetch Shop Info
# def fetch_shop_info():
#     url = f"{BASE_URL}/shop.json"
#     response = requests.get(url)

response = requests.get(f'{SHOPIFY_STORE_DOMAIN}/admin/api/2025-01/reports.json', headers=HEADER_VALUES)

print(response.json())

# if __name__ == "__main__":
#     reports_data = fetch_reports()
#     orders_data = fetch_orders()
#     shop_info = fetch_shop_info()

#     print("Shop Info:", shop_info)
#     print("Reports Data:", reports_data)
#     print("Orders Data:", orders_data)