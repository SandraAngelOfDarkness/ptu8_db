CREATE TABLE pardavimai (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(100)
);

CREATE TABLE customer (
    id INTEGER PRIMARY KEY NOT NULL,
    f_name VARCHAR(50) NOT NULL,
    l_name VARCHAR(50) NOT NULL,
    email VARCHAR (200) UNIQUE
);

CREATE TABLE status (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY NOT NULL,
    date_ VARCHAR(50) NOT NULL,
    customer_id INTEGER,
    status_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customer (id),
    FOREIGN KEY (status_id) REFERENCES status (id)
);

CREATE TABLE product (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(50) NOT NULL,
    price VARCHAR(50) NOT NULL
);

CREATE TABLE product_order (
    id INTEGER PRIMARY KEY NOT NULL,
    quanity VARCHAR(50) NOT NULL,
    orders_id INTEGER,
    product_id INTEGER,
    FOREIGN KEY (orders_id) REFERENCES orders (id),
    FOREIGN KEY (product_id) REFERENCES product (id)
);

INSERT INTO "customer" ("f_name", "l_name", "email") VALUES ("Jonas", "Jonaitis", "jj@gmail.com");
INSERT INTO "customer" ("f_name", "l_name", "email") VALUES ("Petras", "Petraitis", "pp@gmail.com");
INSERT INTO "customer" ("f_name", "l_name", "email") VALUES ("Antanas", "Antanaitis", "aa@gmail.com");
INSERT INTO "customer" ("f_name", "l_name", "email") VALUES ("Onute", "Onaite", "oo@gmail.com");
INSERT INTO "customer" ("f_name", "l_name", "email") VALUES ("Maryte", "Melnikaite", "mm@gmail.com");

INSERT INTO "status" ("name") VALUES ("ivykdytas");
INSERT INTO "status" ("name") VALUES ("ivykdytas");
INSERT INTO "status" ("name") VALUES ("atmestas");
INSERT INTO "status" ("name") VALUES ("nera prekiu");
INSERT INTO "status" ("name") VALUES ("kelyje i sandeli");

INSERT INTO "product" ("name", "price") VALUES ("zvyras", 500);
INSERT INTO "product" ("name", "price") VALUES ("cementas", 500);
INSERT INTO "product" ("name", "price") VALUES ("akmenukai", 500);
INSERT INTO "product" ("name", "price") VALUES ("plytos", 500);
INSERT INTO "product" ("name", "price") VALUES ("putplastis", 500);

INSERT INTO "product_order" ("quanity", orders_id, product_id) VALUES (2, 3, 5);
INSERT INTO "product_order" ("quanity", orders_id, product_id) VALUES (1, 2, 4);
INSERT INTO "product_order" ("quanity", orders_id, product_id) VALUES (4, 1, 3);
INSERT INTO "product_order" ("quanity", orders_id, product_id) VALUES (5, 5, 2);
INSERT INTO "product_order" ("quanity", orders_id, product_id) VALUES (3, 4, 1);

INSERT INTO "orders" (customer_id, status_id, date_) VALUES (1, 3, "2021-11-12");
INSERT INTO "orders" (customer_id, status_id, date_) VALUES (3, 4, "2021-11-12");
INSERT INTO "orders" (customer_id, status_id, date_) VALUES (2, 1, "2021-11-12");
INSERT INTO "orders" (customer_id, status_id, date_) VALUES (4, 2, "2021-11-12");
INSERT INTO "orders" (customer_id, status_id, date_) VALUES (5, 5, "2021-11-12");

SELECT * FROM product_orders;

SELECT product_order.orders_id, l_name, orders.date_, price * quanity as suma FROM customer
    JOIN product_order ON orders_id = orders.id
    JOIN orders ON customer_id = customer.id
    JOIN product ON product_id = product.id;

SELECT product_order.orders_id, product.name, product_order.quanity as 
    product_order.quanity * product.price as suma FROM customer

