-- -----------------------------------------------------
-- Schema restaurant_equipment_sales_system
-- -----------------------------------------------------
USE restaurant_equipment_sales_system;

-- -----------------------------------------------------
-- Table CATEGORIES
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS CATEGORIES (
  cate_id INT NOT NULL AUTO_INCREMENT,
  CategoryName VARCHAR(20) NOT NULL,
  PRIMARY KEY(cate_id));


-- -----------------------------------------------------
-- Table PRODUCTS
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS PRODUCTS (
  prod_id INT NOT NULL AUTO_INCREMENT,
  cate_id INT NOT NULL,
  prod_Name VARCHAR(20) NOT NULL,
  prod_Price FLOAT NOT NULL,
  Description TEXT NULL,
  PRIMARY KEY (prod_id, cate_id),
  FOREIGN KEY (cate_id) REFERENCES CATEGORIES(cate_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table CUSTOMERS
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS CUSTOMERS (
  cust_id INT NOT NULL AUTO_INCREMENT,
  cust_name VARCHAR(20) NOT NULL,
  cust_email VARCHAR(20) NOT NULL UNIQUE,
  cust_phone VARCHAR(11) NOT NULL UNIQUE,
  cust_address VARCHAR(50) NOT NULL,
  PRIMARY KEY (cust_id));


-- -----------------------------------------------------
-- Table ORDERS
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS ORDERS (
  ord_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  cust_id INT NOT NULL,
  ord_date TIMESTAMP(5) NOT NULL,
  QTY INT NOT NULL DEFAULT 1,
  FOREIGN KEY (cust_id) REFERENCES CUSTOMERS(cust_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table PAYMENT
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS PAYMENT (
  pay_id INT NOT NULL AUTO_INCREMENT,
  ord_id INT NOT NULL,
  pay_method ENUM('Visa/MasterCard', 'Cash', 'Bank Transfer') NOT NULL DEFAULT 'Visa/MasterCard',
  pay_date DATETIME(5) NOT NULL,
  pay_amount FLOAT NOT NULL,
  PRIMARY KEY (pay_id, ord_id),
  FOREIGN KEY (ord_id) REFERENCES ORDERS(ord_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);

-- -----------------------------------------------------
-- Table SUPPLIER
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS SUPPLIER (
  supp_id INT NOT NULL AUTO_INCREMENT,
  supp_name VARCHAR(25) NOT NULL,
  supp_address VARCHAR(50) NOT NULL,
  supp_phone VARCHAR(11) NOT NULL UNIQUE,
  supp_email VARCHAR(20) NOT NULL UNIQUE,
  PRIMARY KEY (supp_id));


-- -----------------------------------------------------
-- Table PRODUCT_SUPPLIER_
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS PRODUCT_SUPPLIER (
  prod_supp_id INT NOT NULL AUTO_INCREMENT,
  prod_id INT NOT NULL,
  supp_id INT NOT NULL,
  PRIMARY KEY (prod_supp_id, prod_id, supp_id),
  FOREIGN KEY (prod_id) REFERENCES PRODUCTS(prod_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (supp_id) REFERENCES SUPPLIER(supp_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table ROLES
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS ROLES (
  rol_id INT NOT NULL AUTO_INCREMENT,
  rol_Name ENUM('user', 'customer', 'manager') NOT NULL DEFAULT 'user',
  PRIMARY KEY (rol_id));


-- -----------------------------------------------------
-- Table USERS
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS USERS (
  usr_id INT NOT NULL AUTO_INCREMENT,
  rol_id INT NOT NULL,
  usr_UserName VARCHAR(30) UNIQUE NOT NULL,
  usr_Password CHAR(15) NOT NULL,
  usr_Email VARCHAR(20) UNIQUE NOT NULL,
  PRIMARY KEY (usr_id, rol_id),
  FOREIGN KEY (rol_id) REFERENCES ROLES(rol_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table INVOICES
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS INVOICES (
  invo_id INT NOT NULL AUTO_INCREMENT,
  ord_id INT NOT NULL,
  invo_date TIMESTAMP(5) NOT NULL,
  invo_totalAmount FLOAT NOT NULL,
  PRIMARY KEY (invo_id, ord_id),
  FOREIGN KEY (ord_id) REFERENCES ORDERS(ord_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table INVENTORY
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS INVENTORY (
  inve_id INT NOT NULL AUTO_INCREMENT,
  prod_id INT NOT NULL,
  QuantityInStock INT NOT NULL,
  PRIMARY KEY (inve_id, prod_id),
  FOREIGN KEY (prod_id) REFERENCES PRODUCTS(prod_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table SHIPPING
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS SHIPPING (
  shi_id INT NOT NULL AUTO_INCREMENT,
  ord_id INT NOT NULL,
  shi_address VARCHAR(50) NOT NULL,
  shi_date DATE NOT NULL,
  PRIMARY KEY (shi_id, ord_id),
  FOREIGN KEY (ord_id) REFERENCES ORDERS(ord_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table REVIEWS
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS REVIEWS (
  rev_id INT NOT NULL AUTO_INCREMENT,
  prod_id INT NOT NULL,
  cust_id INT NOT NULL,
  rev_rating FLOAT(2,1) NULL,
  rev_comment TEXT NULL,
  PRIMARY KEY (rev_id, prod_id, cust_id),
  FOREIGN KEY (prod_id) REFERENCES PRODUCTS(prod_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (cust_id) REFERENCES CUSTOMERS(cust_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table REPORTS
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS REPORTS (
  rep_id INT NOT NULL AUTO_INCREMENT,
  usr_id INT NOT NULL,
  rep_Content TEXT NOT NULL,
  rep_CreatedDate TIMESTAMP(5) NOT NULL,
  PRIMARY KEY (rep_id, usr_id),
  FOREIGN KEY (usr_id) REFERENCES USERS(usr_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table ORDER_ITEM
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS ORDER_ITEM (
  ord_item_id INT NOT NULL AUTO_INCREMENT,
  prod_id INT NOT NULL,
  ord_id INT NOT NULL,
  QTY INT NOT NULL DEFAULT 1,
  PRIMARY KEY (ord_item_id, prod_id, ord_id),
  FOREIGN KEY (prod_id) REFERENCES PRODUCTS(prod_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (ord_id) REFERENCES ORDERS(ord_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table INVENTORY_HISTORY
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS INVENTORY_HISTORY (
  hist_id INT NOT NULL AUTO_INCREMENT,
  prod_id INT NOT NULL,
  change_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  change_qty INT NOT NULL,
  change_type ENUM('add', 'remove') NOT NULL,
  PRIMARY KEY (hist_id),
  FOREIGN KEY (prod_id) REFERENCES PRODUCTS(prod_id)
  ON DELETE CASCADE
  ON UPDATE CASCADE
);



ALTER TABLE PRODUCTS
ADD COLUMN prod_image VARCHAR(255) NULL,
ADD COLUMN prod_status ENUM('active', 'inactive') NOT NULL DEFAULT 'active';


ALTER TABLE REPORTS
ADD COLUMN report_type ENUM('sales', 'inventory', 'customer_feedback') NOT NULL DEFAULT 'sales',
ADD COLUMN report_status ENUM('in_progress', 'completed') NOT NULL DEFAULT 'in_progress';
