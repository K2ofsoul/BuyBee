# Product Category Database Schema

This is a database schema for a product categorization system. The schema consists of four tables: `main_categories`, `sub_categories`, `side_categories`, and `products`. The relationships between the tables are as follows:

- Each `main_category` can have multiple `sub_categories`.
- Each `sub_category` can have multiple `side_categories`.
- Each `product` can belong to one `main_category`, one `sub_category`, and one `side_category`.

## Table Descriptions

### main_categories

The `main_categories` table contains the top-level categories for the products. Each category has a unique `id` and a `name` which is a non-null unique text field.

### sub_categories

The `sub_categories` table contains the sub-categories of the products. Each sub-category has a unique `id`, a `name` which is a non-null unique text field, and a `main_category_id` which is a foreign key referencing the `id` of the corresponding `main_category`.

### side_categories

The `side_categories` table contains the side-categories of the products. Each side-category has a unique `id`, a `name` which is a non-null unique text field, and a `sub_category_id` which is a foreign key referencing the `id` of the corresponding `sub_category`.

### products

The `products` table contains information about each product. Each product has a unique `id`, a `product_name` which is a non-null text field, a `selling_price` which is a non-null real field, an `about_product` which is a text field, a `product_specification` which is a text field, a `shipping_weight` which is a non-null real field, a `main_category_id` which is a foreign key referencing the `id` of the corresponding `main_category`, a `sub_category_id` which is a foreign key referencing the `id` of the corresponding `sub_category`, and a `side_category_id` which is a foreign key referencing the `id` of the corresponding `side_category`.

## Conclusion

This schema provides a way to organize products into hierarchies of categories and sub-categories. The `main_categories`, `sub_categories`, and `side_categories` tables provide a way to define the categories, while the `products` table allows for the storage of product information and categorization.

![schema](/db/schema.png)
