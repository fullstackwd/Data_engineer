/*
** 1 Crie uma trigger que quando alterada a senha do professor, crie um
** registro na tabela log informando que essa modificação aconteceu
** informando o nome do professor
*/

CREATE OR REPLACE FUNCTION gatilho1()
	RETURNS TRIGGER AS $$
		BEGIN		
			--Aqui temos um bloco de condição IF para cada tipo de operação (UPDATE)
			IF((new.senhaprofessor <> old.senhaprofessor )) THEN
				INSERT INTO log (descricaolog) VALUES
				( 'a senha '|| OLD.senhaprofessor || ' do Professor '|| OLD.nomeprofessor||' foi alterada para '|| NEW.senhaprofessor||'.');
				 RETURN NEW;			
			END IF;
			RETURN NULL;
		END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER gatilho_1 AFTER update 
	ON  professor FOR EACH ROW
		EXECUTE PROCEDURE gatilho1();


INSERT INTO professor(codprofessor, nomeprofessor,cpfprofessor,senhaprofessor, quantdisciplinas)
VALUES (3,'Adriano',75321465489,123456,1);

UPDATE professor SET senhaprofessor = '123459' WHERE codprofessor = 3;

SELECT * FROM professor;
SELECT * FROM log;

/*
** 2 Crie uma trigger que quando alterado o status do aluno, crie um registro na
** tabela log informando que essa modificação aconteceu informando o nome do aluno
*/

CREATE OR REPLACE FUNCTION gatilho2()
	RETURNS TRIGGER AS $$
		BEGIN		
			--Aqui temos um bloco de condição IF para cada tipo de operação (UPDATE)
			 IF((NEW.statusaluno <> OLD.statusaluno )) THEN
				INSERT INTO log1 (descricaolog) VALUES
				( 'o status - '|| OLD.statusaluno || ' - do aluno '|| OLD.nomealuno||' foi alterada para '|| NEW.statusaluno||'.');
				 RETURN NEW;			
			END IF;
			RETURN NULL;
		END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER gatilho_2 AFTER update 
	ON  aluno FOR EACH ROW
		EXECUTE PROCEDURE gatilho2();
		
		
UPDATE aluno SET statusaluno = '123456' WHERE codaluno = 1;

INSERT INTO aluno(nomealuno,cpfaluno,senhaaluno, statusaluno )
VALUES ('marina loana',69547845,56,78);
	
SELECT * FROM log;


/*
** 3 Crie uma trigger que quando for adicionado a uma turma, crie um registro
** na tabela log informando que essa adição aconteceu informando o nome da turma
*/

CREATE OR REPLACE FUNCTION gatilho3()
	RETURNS TRIGGER AS $$
		BEGIN	
			INSERT INTO log (descricaolog) VALUES
			('o aluno do id  ' || NEW.codaluno || ' foi inserido na turma de  :  '||
			 (SELECT nometurma FROM turma Tr WHERE Tr.codturma = NEW.codturma )||'.' );
			 RETURN NEW;

			RETURN NULL;
		END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER gatilho_3 AFTER INSERT 
	ON turma_aluno FOR EACH ROW
		EXECUTE PROCEDURE gatilho3();
		
/*		
** 4 Crie uma trigger que quando uma nota for adicionada na tabela nota, crie
** um registro na tabela log informando a nota e o codaluno que recebeu a nota		
*/

CREATE OR REPLACE FUNCTION gatilho4()
	RETURNS TRIGGER AS $$
		BEGIN		
			INSERT INTO log1 (descricaolog) VALUES
				( 'a nota semestre 1   '|| new.nota1semestre || '  e nota semestre 2  ' || new.nota2semestre || ' - do aluno id :  '||new.codaluno||' foi inserido .');
				 RETURN NEW;			
			
			RETURN NULL;
		END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER gatilho_4 AFTER insert 
	ON  nota FOR EACH ROW
		EXECUTE PROCEDURE gatilho4();
		
INSERT INTO nota (nota1semestre, nota2semestre, codaluno, coddisciplina) VALUES (9,8,2,1);

/*
** 5 Crie um a trigger que quando for adicionado algum aluno na tabela
** turma_aluno, adicione +1 aluno em quantidadealunos na tabela turma
*/

CREATE OR REPLACE FUNCTION gatilho5()
	RETURNS TRIGGER AS $$
		BEGIN
			if new.codturma = (SELECT codturma FROM turma T WHERE T.codturma = NEW.codturma ) THEN
			UPDATE turma SET quantidadealunos = quantidadealunos + 1 WHERE codturma = NEW.codturma;
			RETURN NEW;	
		END IF;
		RETURN NULL;
	END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER gatilho_5 AFTER insert 
	ON  turma_aluno FOR EACH ROW
		EXECUTE PROCEDURE gatilho5();


/*
** 6. Crie uma trigger que quando for adicionado algum professor na tabela
** disciplina, adicione +1 disciplina em quantdisciplina na tabela professor
*/

CREATE OR REPLACE FUNCTION gatilho6()
	RETURNS TRIGGER AS $$
		BEGIN
			IF NEW.codprofessor = (SELECT codtproseffor FROM professor P WHERE P.codprofessor = NEW.codprofessor ) THEN
			UPDATE professor SET quantdisciplina = quantdisciplina + 1 WHERE codprofessor = NEW.codprofessor;
			RETURN NEW;	
		END IF;
		RETURN NULL;
		END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER gatilho_6 AFTER insert 
	ON  turma_aluno FOR EACH ROW
		EXECUTE PROCEDURE gatilho6();
		
/*
** 7. Crie uma trigger que quando for adicionado ou alterado uma nota, altere o
** campo nota final segundo o padrão n1+n2/2
*/

CREATE OR REPLACE FUNCTION gatilho8()
	RETURNS TRIGGER AS $$
		BEGIN
			UPDATE nota SET notafinal = (nota1semestre+nota2semestre)/2 WHERE codaluno = NEW.codaluno;
			RETURN NEW;	
		RETURN NULL;
		END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER gatilho_8 AFTER insert 
	ON  nota FOR EACH ROW
		EXECUTE PROCEDURE gatilho8();
		
INSERT INTO nota (nota1semestre, nota2semestre,codaluno, coddisciplina) values (1,2,3,4)

/*
** 8. Crie uma trigger que quando for adicionado a nota final do aluno, crie um
** registro na tabela log informando a disciplina, código do aluno e a nota final
*/

CREATE OR REPLACE FUNCTION gatilho9()
	RETURNS TRIGGER AS $$
		BEGIN
			INSERT INTO log1 (descricaolog) VALUES
			('disiciplna '|| (SELECT nomedisciplina FROM disciplina WHERE coddisciplina = newcoddisciplina) ||
 			'codaluno ' || NEW.codaluno || 'e nota ' || NEW.notafinal || '. ') ;
			RETURN NEW;	
		RETURN NULL;
		END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER gatilho_9 AFTER UPDATE 
ON nota FOR EACH ROW EXECUTE PROCEDURE gatilho9();
		