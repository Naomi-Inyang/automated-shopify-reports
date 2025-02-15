from dotenv import load_dotenv
import requests, os

load_dotenv()

SHOPIFY_STORE_URL = os.getenv('STORE_URL')
API_KEY = os.getenv('API_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')  
SECRET_KEY= os.getenv('SECRET_KEY') 
HEADER_VALUES = {
    'Content-Type': 'application/json', 
    'X-Shopify-Access-Token': ACCESS_TOKEN
}

def fetch_order_info():
    url = f'{SHOPIFY_STORE_URL}/admin/api/2025-01/reports.json'
    response = requests.get(url, headers=HEADER_VALUES)

    if response.status_code == 200:
        orders = response.json().get('orders', [])
        total_sales = sum(float(order['total_price']) for order in orders)
        total_orders = len(orders)
    else:
        total_sales, total_orders = 0, 0

    return total_sales, total_orders

def fetch_store_name():
    url = f'{SHOPIFY_STORE_URL}/admin/api/2025-01/shop.json'
    response = requests.get(url, headers=HEADER_VALUES)

    if response.status_code == 200:
        store_name = response.json().get('shop', {}).get('name', "Your Shopify Store")
    else:
        store_name = "Your Shopify Store"

    return store_name

def generate_store_report():
    shop_name = fetch_store_name()
    total_sales, total_orders = fetch_order_info()

    store_report = f'''
        🚀 *Shopify Report for {shop_name}* 🚀

        💰 *Total Sales MTD:* ${total_sales}  
        📦 *Total Orders MTD:* {total_orders}  
    '''

    return store_report

if __name__ == "__main__":
    reports_data = generate_store_report()
    print("Reports Data:", reports_data)