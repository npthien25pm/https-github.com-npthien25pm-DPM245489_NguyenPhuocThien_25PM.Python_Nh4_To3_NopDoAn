CREATE DATABASE IF NOT EXISTS quanly_benhnhan;
USE quanly_benhnhan;

CREATE TABLE IF NOT EXISTS benhnhan (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ma_bn INT,
    ho_ten VARCHAR(100),
    gioi_tinh VARCHAR(10),
    ngay_sinh DATE,
    so_dt VARCHAR(15),
    dia_chi VARCHAR(200),
    chan_doan VARCHAR(200),
    ngay_nhapvien DATE,
    ghi_chu TEXT
);
