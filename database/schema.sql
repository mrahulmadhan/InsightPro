-- Enable foreign key support
PRAGMA foreign_keys = ON;

-- TABLE: regions
CREATE TABLE IF NOT EXISTS regions (
    region_id   TEXT PRIMARY KEY,
    region_name TEXT NOT NULL,
    country     TEXT NOT NULL DEFAULT 'USA'
);

-- TABLE: products
CREATE TABLE IF NOT EXISTS products (
    product_id   TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category     TEXT NOT NULL,
    unit_price   REAL NOT NULL,
    unit_cost    REAL NOT NULL
);

-- TABLE: customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id   TEXT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    email         TEXT,
    segment       TEXT NOT NULL,
    signup_date   DATE NOT NULL,
    region_id     TEXT NOT NULL,
    FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

-- TABLE: orders (Fact Table)
CREATE TABLE IF NOT EXISTS orders (
    order_id     TEXT PRIMARY KEY,
    order_date   DATE NOT NULL,
    customer_id  TEXT NOT NULL,
    product_id   TEXT NOT NULL,
    region_id    TEXT NOT NULL,
    quantity     INTEGER NOT NULL DEFAULT 1,
    unit_price   REAL NOT NULL,
    total_amount REAL NOT NULL,
    status       TEXT NOT NULL DEFAULT 'Completed',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id)  REFERENCES products(product_id),
    FOREIGN KEY (region_id)   REFERENCES regions(region_id)
);
