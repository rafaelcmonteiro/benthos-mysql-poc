CREATE DATABASE IF NOT EXISTS datasource;
USE datasource;

CREATE TABLE IF NOT EXISTS kern_log (
    date_time varchar(100),
    kernel_info varchar(200)
);