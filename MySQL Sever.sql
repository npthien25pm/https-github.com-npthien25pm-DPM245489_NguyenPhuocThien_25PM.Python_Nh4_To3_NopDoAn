CREATE DATABASE quanly_benhnhan;

USE quanly_benhnhan;

CREATE TABLE benhnhan (
    ma_bn INT AUTO_INCREMENT PRIMARY KEY,
    ho_ten VARCHAR(100) NOT NULL,
    gioi_tinh VARCHAR(10),
    ngay_sinh DATE,
    dia_chi VARCHAR(200),
    ngay_nhap_vien DATE,
    chuan_doan VARCHAR(255),
    sdt VARCHAR(15)
);
