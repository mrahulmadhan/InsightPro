import sqlite3
import random
import os
from datetime import datetime, timedelta
from faker import Faker
from config import Config
from database.db_init import init_db

fake = Faker()

def generate_and_insert_data():
    """Generates realistic sample data and inserts it into the database."""
    print("Starting data generation process...")
    

    if not os.path.exists(Config.DATABASE_PATH):
        print("Database not found. Initializing...")
        init_db()
        
    conn = sqlite3.connect(Config.DATABASE_PATH)
    cursor = conn.cursor()
    

    cursor.execute("PRAGMA foreign_keys = ON;")
    

    cursor.executescript("""
        DELETE FROM orders;
        DELETE FROM customers;
        DELETE FROM products;
        DELETE FROM regions;
    """)
    
    # 1. Generate Regions
    print("Generating 5 regions...")
    regions = [
        ('R01', 'North', 'USA'),
        ('R02', 'South', 'USA'),
        ('R03', 'East', 'USA'),
        ('R04', 'West', 'USA'),
        ('R05', 'Central', 'USA')
    ]
    cursor.executemany("INSERT INTO regions VALUES (?, ?, ?)", regions)
    
    # 2. Generate Products
    print("Generating 15 products...")
    products = [
        ('P001', 'Wireless Headphones Pro', 'Electronics', 149.99, 62.00),
        ('P002', 'Smart Watch Series X', 'Electronics', 299.99, 130.00),
        ('P003', 'Bluetooth Speaker', 'Electronics', 79.99, 28.00),
        ('P004', 'USB-C Laptop Hub', 'Electronics', 59.99, 18.00),
        ('P005', '4K Webcam', 'Electronics', 119.99, 45.00),
        ('P006', 'Running Sneakers', 'Clothing', 89.99, 32.00),
        ('P007', 'Yoga Pants Premium', 'Clothing', 54.99, 18.00),
        ('P008', 'Winter Jacket Pro', 'Clothing', 129.99, 52.00),
        ('P009', 'Air Purifier 500', 'Home', 199.99, 80.00),
        ('P010', 'Coffee Maker Deluxe', 'Home', 89.99, 35.00),
        ('P011', 'Smart LED Bulb 4pk', 'Home', 34.99, 10.00),
        ('P012', 'Robot Vacuum Lite', 'Home', 249.99, 105.00),
        ('P013', 'Adjustable Dumbbells', 'Sports', 179.99, 72.00),
        ('P014', 'Resistance Band Set', 'Sports', 24.99, 6.00),
        ('P015', 'Foam Roller Pro', 'Sports', 39.99, 12.00)
    ]
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?)", products)
    
    # 3. Generate Customers
    print("Generating 100 customers...")
    customers = []
    region_ids = [r[0] for r in regions]
    segments = ['Enterprise', 'SMB', 'Consumer']
    
    for i in range(1, 101):
        customer_id = f'C{i:03d}'
        

        segment = random.choices(segments, weights=[20, 40, 40])[0]
        

        if segment == 'Consumer':
            name = fake.name()
        else:
            name = fake.company()
            
        email = fake.email()
        

        signup_date = fake.date_between(start_date='-3y', end_date='-1y').strftime('%Y-%m-%d')
        

        region_id = random.choice(region_ids)
        
        customers.append((customer_id, name, email, segment, signup_date, region_id))
        
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?)", customers)
    
    # 4. Generate Orders
    print("Generating 5000 sales orders (this might take a few seconds)...")
    orders = []
    
    # This ensures the JS default "last 12 months" always lands inside the data.
    end_date   = datetime.today()
    start_date = datetime(end_date.year - 2, 1, 1)
    delta_days = (end_date - start_date).days
    
    statuses = ['Completed', 'Completed', 'Completed', 'Completed', 'Refunded'] # 80% completed
    
    for i in range(1, 5001):
        order_id = f'ORD-{i:05d}'
        

        random_days = random.randrange(delta_days)
        order_date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
        

        customer = random.choice(customers)
        customer_id = customer[0]
        region_id = customer[5] # Order is placed in customer's region
        

        product = random.choice(products)
        product_id = product[0]
        unit_price = product[3]
        

        segment = customer[3]
        if segment == 'Enterprise':
            quantity = random.randint(10, 50)  # Enterprises buy in bulk
        elif segment == 'SMB':
            quantity = random.randint(2, 15)   # SMBs buy multiple
        else:
            quantity = random.randint(1, 3)    # Consumers buy few
            
        total_amount = round(quantity * unit_price, 2)
        status = random.choice(statuses)
        
        orders.append((
            order_id, order_date, customer_id, product_id, region_id,
            quantity, unit_price, total_amount, status
        ))
        
    cursor.executemany("INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", orders)
    

    conn.commit()
    conn.close()
    
    print("\nSuccess! Database has been seeded.")
    print("Summary:")
    print(f"- {len(regions)} Regions inserted")
    print(f"- {len(products)} Products inserted")
    print(f"- {len(customers)} Customers inserted")
    print(f"- {len(orders)} Orders inserted")
    print(f"Database location: {Config.DATABASE_PATH}")

if __name__ == '__main__':
    generate_and_insert_data()
