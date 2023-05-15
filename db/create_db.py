import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("buybee.db")
cursor = connection.cursor()

# Create main_categories table
cursor.execute(
    """
CREATE TABLE main_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);
"""
)

# Create sub_categories table
cursor.execute(
    """
CREATE TABLE sub_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    main_category_id INTEGER,
    FOREIGN KEY (main_category_id) REFERENCES main_categories (id)
);
"""
)

# Create side_categories table
cursor.execute(
    """
CREATE TABLE side_categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    sub_category_id INTEGER,
    FOREIGN KEY (sub_category_id) REFERENCES sub_categories (id)
);
"""
)

# Create products table
cursor.execute(
    """
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    selling_price REAL NOT NULL,
    about_product TEXT,
    product_specification TEXT,
    shipping_weight REAL NOT NULL,
    main_category_id INTEGER NOT NULL,
    sub_category_id INTEGER NOT NULL,
    side_category_id INTEGER NOT NULL,
    FOREIGN KEY (main_category_id) REFERENCES main_categories (id),
    FOREIGN KEY (sub_category_id) REFERENCES sub_categories (id),
    FOREIGN KEY (side_category_id) REFERENCES side_categories (id)
);
"""
)

# Commit the changes and close the connection
connection.commit()
connection.close()
