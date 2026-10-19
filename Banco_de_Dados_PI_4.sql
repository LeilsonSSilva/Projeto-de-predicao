CREATE DATABASE IF NOT EXISTS onsale_iot_db;
USE onsale_iot_db;

CREATE TABLE IF NOT EXISTS sensores_leituras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dispositivo_id VARCHAR(50) NOT NULL,
    temperatura DECIMAL(5,2),
    umidade DECIMAL(5,2),
    consumo_kwh DECIMAL(10,2),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS predicoes_consumo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    semana_referencia VARCHAR(20) NOT NULL,
    temperatura_media DECIMAL(5,2),
    umidade_media DECIMAL(5,2),
    consumo_previsto_kwh DECIMAL(10,2),
    custo_previsto_rs DECIMAL(10,2),
    data_geracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);