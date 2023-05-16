import csv
import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("buybee.db")
cursor = connection.cursor()

# Read the CSV file
with open("buybee_dummy_products.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=",")
    for row in reader:
        # Insert main categories if they don't exist
        cursor.execute(
            "INSERT OR IGNORE INTO main_categories (name) VALUES (?)",
            (row["Main Category"],),
        )

        # Get the main category id
        main_category_id = cursor.execute(
            "SELECT id FROM main_categories WHERE name=?", (row["Main Category"],)
        ).fetchone()[0]

        # Insert sub categories if they don't exist and link them to the main category
        cursor.execute(
            "INSERT OR IGNORE INTO sub_categories (name, main_category_id) VALUES (?, ?)",
            (row["Sub-Category"], main_category_id),
        )

        # Get the sub category id
        sub_category_id = cursor.execute(
            "SELECT id FROM sub_categories WHERE name=?", (row["Sub-Category"],)
        ).fetchone()[0]

        # Insert side categories if they don't exist and link them to the sub category
        cursor.execute(
            "INSERT OR IGNORE INTO side_categories (name, sub_category_id) VALUES (?, ?)",
            (row["Side Category"], sub_category_id),
        )

        # Get the side category id
        side_category_id = cursor.execute(
            "SELECT id FROM side_categories WHERE name=?", (row["Side Category"],)
        ).fetchone()[0]

        # Insert the product
        cursor.execute(
            """
            INSERT INTO products (product_name, selling_price, about_product, product_specification,
                                  shipping_weight, main_category_id, sub_category_id, side_category_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row["Product Name"],
                row["Selling Price($)"],
                row["About Product"],
                row["Product Specification"],
                row["Shipping Weight(Pounds)"],
                main_category_id,
                sub_category_id,
                side_category_id,
            ),
        )

# Commit the changes and close the connection
connection.commit()
connection.close()
