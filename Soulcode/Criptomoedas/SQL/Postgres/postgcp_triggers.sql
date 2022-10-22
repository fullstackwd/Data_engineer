--Dataset equipe2.csv criptomoeda
CREATE TABLE IF NOT EXISTS criptomoeda_origin(
	id_co       text,
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
    id_cdc          text, 
    name           text,
    symbol          text,
    slug            text,
    rank           text,
    is_active       text,
    first_data      text,
    last_data       text,
    
    CONSTRAINT id_cdc_pk PRIMARY KEY (id_cdc)
);

select * from cripto_data_criacao;

-- DROP TABLE cripto_data_criacao

DROP TABLE criptomoeda_origin
DROP TABLE LOGS_CRIPTOMOEDA
DROP TABLE criptomoeda_origin_LogFunc()

--Criação Tabela LOGS_MYSQL, caso não exista
CREATE TABLE LOGS_CRIPTOMOEDA(
	cod_log SERIAL NOT NULL,
	data_log TEXT NOT NULL,
	desc_log VARCHAR(150)
);

CREATE OR REPLACE FUNCTION criptomoeda_origin_LogFunc() RETURNS TRIGGER AS $$
	BEGIN
		--um IF para cada operação
		IF(TG_OP = 'INSERT') THEN
			INSERT INTO LOGS_CRIPTOMOEDA (data_log, desc_log) 
				VALUES	(CURRENT_TIMESTAMP, 'New ID: ' || NEW.ID ||
											' * Ticker: ' || NEW.Ticker ||
											' * TokenName: ' || NEW.TokenName ||
											' * Date: ' || NEW.Date);						
				RETURN NEW;
							
		ELSIF(TG_OP = 'UPDATE') THEN
			INSERT INTO LOGS_CRIPTOMOEDA (data_log, desc_log) 
				VALUES (CURRENT_TIMESTAMP, 'ID Alterado: ' || NEW.ID || 
										   ' * Ticker: ' || NEW.Ticker ||
										   ' * TokenName: ' || NEW.TokenName ||
										   ' * Date: ' || NEW.Date);
				RETURN NEW;
							
		ELSIF(TG_OP = 'DELETE') THEN
			INSERT INTO LOGS_CRIPTOMOEDA (data_log, desc_log) 
				VALUES (CURRENT_TIMESTAMP, 'ID Excluído: ' || OLD.ID || 
										   ' Ticker: ' || OLD.Ticker ||
										   ' TokenName:' || OLD.TokenName ||
										   ' Date: ' || OLD.Date );
											RETURN OLD;							
		END IF;
		RETURN NULL;

END;
$$
LANGUAGE 'plpgsql';


--TRIGGER ( GATILHO)
CREATE TRIGGER Gatilho_criptomoeda_origin_LogFunc AFTER
	INSERT OR UPDATE OR DELETE ON criptomoeda_origin
		FOR EACH ROW EXECUTE PROCEDURE criptomoeda_origin_LogFunc();
        
select * from CRIPTOMOEDA_ORIGIN;

select * from LOGS_CRIPTOMOEDA;

-- select * from criptomoeda_origin_LogFunc()

select open, close, ticker, high, low from CRIPTOMOEDA_ORIGIN where open < '0.01';