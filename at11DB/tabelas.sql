-- Criando as tabelas:
CREATE TABLE IF NOT EXISTS dados(
	id_dados serial,
	data_dados date NOT NULL,
	valor_dados decimal(10,2) NOT NULL,
	CONSTRAINT dados_pk PRIMARY KEY (id_dados)
);

select * from dados;

CREATE TABLE IF NOT EXISTS log_tabelas (
	id_log serial,
	usuario varchar(30),
	dt_log timestamp,
	msg_log varchar,
	CONSTRAINT log_tabelas_pk PRIMARY KEY (id_log)
);

select * from log_tabelas;

CREATE TABLE IF NOT EXISTS dados_blocos(
	id_bloco serial,
	media decimal(7,2),
	mediana decimal(7,2),
	moda decimal(7,2),
	desvio_padrao decimal(7,2),
	maximo decimal (8,2),
	minimo decimal (7,2),
	inicio date,
	fim date,
	CONSTRAINT dados_blocos_pk PRIMARY KEY (id_bloco)
);

select * from dados_blocos;