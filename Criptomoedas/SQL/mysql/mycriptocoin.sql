show databases;

use criptomoeda;

show tables;

--Dataset equipe2.csv criptomoeda
CREATE TABLE IF NOT EXISTS criptomoeda_origin(
	id_co       int not null,
	ticker		text,
	TokenName	text,
	Date		text,
	Open		text,
	High		text,
	Low			text,
	Close		text,
	Volume		text,
	Market_Cap	text,
    
   CONSTRAINT id_co_pk PRIMARY KEY (id_co)
);

-- DROP TABLE criptomoeda_origin

--Dataset auxiliar cripto_data_criacao.json
CREATE TABLE IF NOT EXISTS  cripto_data_criacao(
    id_cdc          int not null,
    name1           text,
    symbol          text,
    slug            text,
    rank1           text,
    is_active       text,
    first_data      text,
    last_data       text,
    platform        text,
    id_co           text,
    
    CONSTRAINT id_cdc_pk PRIMARY KEY (id_cdc)
);

select * from cripto_data_criacao;

-- drop table cripto_data_criacao;

SELECT * FROM LOGS_MYSQL;

SELECT * FROM cripto_data_criacao;


--Criação Tabela LOGS_MYSQL, caso não exista
CREATE TABLE logs_mysql(
	cod_log SERIAL NOT NULL,
	data_log TEXT NOT NULL,
	desc_log VARCHAR(150)
);

SELECT * FROM logs_mysql;

--DROP TABLE LOGS_MYSQL

--Criação da Função para o Trigger

DELIMITER $$
CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`criptomoeda_origin_AFTER_INSERT` AFTER INSERT ON `criptomoeda_origin` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`criptomoeda_origin_BEFORE_UPDATE` BEFORE UPDATE ON `criptomoeda_origin` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`criptomoeda_origin_AFTER_UPDATE` AFTER UPDATE ON `criptomoeda_origin` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`criptomoeda_origin_BEFORE_DELETE` BEFORE DELETE ON `criptomoeda_origin` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`criptomoeda_origin_AFTER_DELETE` AFTER DELETE ON `criptomoeda_origin` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`criptomoeda_origin_BEFORE_INSERT_1` BEFORE INSERT ON `criptomoeda_origin` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`cripto_data_criacao_BEFORE_INSERT` BEFORE INSERT ON `cripto_data_criacao` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`cripto_data_criacao_BEFORE_UPDATE` BEFORE UPDATE ON `cripto_data_criacao` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`cripto_data_criacao_AFTER_UPDATE` AFTER UPDATE ON `cripto_data_criacao` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`cripto_data_criacao_BEFORE_DELETE` BEFORE DELETE ON `cripto_data_criacao` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`cripto_data_criacao_AFTER_DELETE` AFTER DELETE ON `cripto_data_criacao` FOR EACH ROW
BEGIN

END
$$

CREATE DEFINER = CURRENT_USER TRIGGER `criptomoeda`.`cripto_data_criacao_AFTER_INSERT` AFTER INSERT ON `cripto_data_criacao` FOR EACH ROW
BEGIN

END
$$

DELIMITER ;




SELECT * FROM criptomoeda_origin;

SELECT * FROM cripto_data_criacao;

-- drop table criptomoeda_origin
