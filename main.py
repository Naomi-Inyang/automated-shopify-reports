from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv
import requests, os, json

load_dotenv()

SHOPIFY_STORE_URL = os.getenv('STORE_URL')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')  
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

SHOPIFY_HEADER_VALUES = {
    'Content-Type': 'application/json', 
    'X-Shopify-Access-Token': ACCESS_TOKEN
}

STORE_REPORT_HEADER_VALUES = {
    'Content-Type': 'application/json'
}

def fetch_order_info():
    url = f'{SHOPIFY_STORE_URL}/admin/api/2025-01/orders.json'
    response = requests.get(url, headers=SHOPIFY_HEADER_VALUES)

    if response.status_code == 200:
        orders = response.json().get('orders', [])
        total_sales = '$' + str(sum(float(order['total_price']) for order in orders))
        total_orders = len(orders)
    else:
        total_sales, total_orders = 'Currently Unavailable', 'Currently Unavailable'

    return total_sales, total_orders

def fetch_store_name():
    url = f'{SHOPIFY_STORE_URL}/admin/api/2025-01/shop.json'
    response = requests.get(url, headers=SHOPIFY_HEADER_VALUES)

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

        💰 *Total Sales MTD:* {total_sales}  
        📦 *Total Orders MTD:* {total_orders}  
    '''

    return store_report

def send_report_to_google_chat():
    report_message = generate_store_report()
    
    message_payload = {
        "text": report_message
    }
    
    response = requests.post(WEBHOOK_URL, headers=STORE_REPORT_HEADER_VALUES, data=json.dumps(message_payload))

    if response.status_code == 200:
        print('Successfully sent store report')
    else:
        print('Something went wrong')


if __name__ == "__main__":
    # Runs daily at 09:00 AM
    scheduler = BlockingScheduler()
    scheduler.add_job(send_report_to_google_chat, 'cron', hour=9, minute=0)
    scheduler.start()
