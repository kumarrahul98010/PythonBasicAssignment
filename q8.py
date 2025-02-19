import json
import csv

with open('sales.json', 'r') as file:
    orders_data = json.load(file)

processed_orders = []

SHIPPING_COST_PER_ITEM = 5.0
DISCOUNT_THRESHOLD = 100.0
DISCOUNT_RATE = 0.10

for order in orders_data['orders']:
    order_id = order['order_id']
    customer_name = order['customer']['name']
    shipping_address = order['shipping_address']
    country_code = shipping_address.split(',')[-1].strip()

    for item in order['items']:
        product_name = item['name']
        product_price = item['price']
        quantity = item['quantity']
        
        total_value = product_price * quantity
        discount = total_value * DISCOUNT_RATE if total_value > DISCOUNT_THRESHOLD else 0
        shipping_cost = quantity * SHIPPING_COST_PER_ITEM
        final_total = total_value - discount + shipping_cost
        
        processed_orders.append([
            order_id,
            customer_name,
            product_name,
            product_price,
            quantity,
            total_value,
            discount,
            shipping_cost,
            final_total,
            shipping_address,
            country_code
        ])

processed_orders.sort(key=lambda x: x[8], reverse=True)

with open('processed_orders.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'Order ID', 'Customer Name', 'Product Name', 'Product Price', 'Quantity Purchased',
        'Total Value', 'Discount', 'Shipping Cost', 'Final Total', 'Shipping Address', 'Country Code'
    ])
    writer.writerows(processed_orders)

print("Processed orders have been written to 'processed_orders.csv'.")


