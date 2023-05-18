# Buybee Database Schema

This is the BuyBee database schema consisting of 10 tables: `users`, `shopping_carts`, `shopping_cart_items`, `purchases`, `comments`, `favorites`, `main_categories`, `sub_categories`, `side_categories`, and `products`.

## `users` Table
This table stores information about users, including their `id`, `username`, `email`, `password`, `first_name`, `last_name`, `phone_number`, and `address`.

## `shopping_carts` Table
This table stores information about shopping carts, including their `id` and the `user_id` of the user who owns the cart.

## `shopping_cart_items` Table
This table stores information about items in a shopping cart, including their `id`, `cart_id`, `product_id`, and `quantity`.

## `purchases` Table
This table stores information about purchases, including their `id`, `user_id`, `product_id`, `quantity`, and `purchase_date`.

## `comments` Table
This table stores information about comments made by users on products, including their `id`, `user_id`, `product_id`, `comment`, and `comment_date`.

## `favorites` Table
This table stores information about products that users have added to their favorites, including their `id`, `user_id`, and `product_id`.

## `main_categories` Table
This table stores information about main categories of products, including their `id` and `name`.

## `sub_categories` Table
This table stores information about subcategories of products, including their `id`, `name`, and `main_category_id`.

## `side_categories` Table
This table stores information about side categories of products, including their `id`, `name`, and `sub_category_id`.

## `products` Table
This table stores information about products, including their `id`, `product_name`, `selling_price`, `about_product`, `product_specification`, `shipping_weight`, `main_category_id`, `sub_category_id`, and `side_category_id`.

Foreign key constraints have been added to ensure data consistency and integrity across the tables.

![schema](/db/schema.png)
