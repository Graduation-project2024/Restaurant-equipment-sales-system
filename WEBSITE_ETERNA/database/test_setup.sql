DROP DATABASE IF EXISTS test_restaurant_equipment_sales_system;
CREATE DATABASE test_restaurant_equipment_sales_system;
USE test_restaurant_equipment_sales_system;

CREATE TABLE Customers (
    cust_id INT AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(255) NOT NULL,
    cust_phone VARCHAR(20),
    cust_email VARCHAR(255),
    cust_username VARCHAR(255) NOT NULL UNIQUE,
    cust_password VARCHAR(255) NOT NULL
);

CREATE TABLE auth_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME(6) NULL,
    is_superuser TINYINT(1) NOT NULL,
    username VARCHAR(150) NOT NULL UNIQUE,
    first_name VARCHAR(150) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(254) NOT NULL,
    is_staff TINYINT(1) NOT NULL,
    is_active TINYINT(1) NOT NULL,
    date_joined DATETIME(6) NOT NULL
);

CREATE TABLE django_session (
    session_key VARCHAR(40) NOT NULL PRIMARY KEY,
    session_data LONGTEXT NOT NULL,
    expire_date DATETIME(6) NOT NULL
);

CREATE TABLE django_migrations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    app VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    applied DATETIME(6) NOT NULL
);

CREATE TABLE django_content_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    app_label VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    UNIQUE KEY unique_app_model (app_label, model)
);

CREATE TABLE auth_permission (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    content_type_id INT NOT NULL,
    codename VARCHAR(100) NOT NULL,
    UNIQUE KEY unique_content_type_codename (content_type_id, codename),
    FOREIGN KEY (content_type_id) REFERENCES django_content_type (id)
);

CREATE TABLE auth_group (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL UNIQUE
);

CREATE TABLE auth_group_permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    group_id INT NOT NULL,
    permission_id INT NOT NULL,
    UNIQUE KEY unique_group_permission (group_id, permission_id),
    FOREIGN KEY (group_id) REFERENCES auth_group (id),
    FOREIGN KEY (permission_id) REFERENCES auth_permission (id)
);

CREATE TABLE auth_user_groups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    group_id INT NOT NULL,
    UNIQUE KEY unique_user_group (user_id, group_id),
    FOREIGN KEY (user_id) REFERENCES auth_user (id),
    FOREIGN KEY (group_id) REFERENCES auth_group (id)
);

CREATE TABLE auth_user_user_permissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    permission_id INT NOT NULL,
    UNIQUE KEY unique_user_permission (user_id, permission_id),
    FOREIGN KEY (user_id) REFERENCES auth_user (id),
    FOREIGN KEY (permission_id) REFERENCES auth_permission (id)
);
