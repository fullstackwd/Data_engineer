create table if not exists Postos (
	Regiao varchar(2),
	Estado varchar(2),
	Municipio varchar(150),
	Revenda varchar(150),
	CNPJ varchar(20),
	Rua varchar(150),
	Numero varchar(20),
	Complemento varchar(150),
	Bairro varchar(150),
	Cep varchar(15),
	Produto varchar(50),
	Data_da_Coleta varchar(15),
	Valor_de_Venda varchar(50),
	Valor_de_Compra varchar(50),
	Unidade_de_Medida varchar(50),
	Bandeira varchar(150)

	-- constraint postos_pk primary key (idposto)
);
