CREATE DATABASE IF NOT EXISTS db;
USE db;

CREATE TABLE IF NOT EXISTS kern_log (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `time` varchar(100),
    `kernel_info` varchar(200),
    PRIMARY KEY(id)
);