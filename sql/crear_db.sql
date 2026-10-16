CREATE DATABASE IF NOT EXISTS sistema_hotel
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci;

CREATE USER IF NOT EXISTS 'sistema_hotel_user'@'localhost' IDENTIFIED BY 'INSANOVICH123';

GRANT ALL PRIVILEGES ON sistema_hotel.* TO 'sistema_hotel_user'@'localhost';

FLUSH PRIVILEGES;