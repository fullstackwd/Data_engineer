-- 1. Crie um banco de dados chamado lista_triggers.

-- CREATE DATABASE lista_triggers;

-- 2. Crie as tabelas seguindo o modelo:

-- -----------------------------------------------------
-- Table professor
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS professor (
  codprofessor      INT     NOT NULL,
  nomeprofessor     VARCHAR(45) NULL,
  cpfprofessor      VARCHAR(45) NULL,
  senhaprofessor    VARCHAR(45) NULL,
  quantdisciplinas  VARCHAR(45) NULL,
  PRIMARY KEY (codprofessor)
);

-- -----------------------------------------------------
-- Table disciplina
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS disciplina (
  coddisciplina   INT      NOT NULL,
  nomedisciplina  VARCHAR(45)  NULL,
  codprofessor    INT      NOT NULL,
	
  PRIMARY KEY (coddisciplina),
  CONSTRAINT fk_disciplina_professor FOREIGN KEY (codprofessor) REFERENCES professor (codprofessor)
);

-- -----------------------------------------------------
-- Table aluno
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS aluno(
  codaluno     INT           NULL,
  nomealuno    VARCHAR(100)  NULL,
  cpfaluno     VARCHAR(45)   NULL,
  senhaaluno   VARCHAR(100)   NULL,
  statusaluno  INT           NULL,
  PRIMARY KEY (codaluno)
);

-- -----------------------------------------------------
-- Table nota
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS nota(
  	codnota        INT           NULL,
  	nota1semestre  DECIMAL(2,1)  NULL,
  	nota2semestre  DECIMAL(2,1)  NULL,
  	notafinal      DECIMAL(2,1)  NULL,
  	coddisciplina  INT       NOT NULL,
  	codaluno       INT       NOT NULL,
  
	PRIMARY KEY (codnota),
	CONSTRAINT fk_nota_disciplina1 FOREIGN KEY (coddisciplina) REFERENCES disciplina (coddisciplina),
	CONSTRAINT fk_nota_aluno1 FOREIGN KEY (codaluno) REFERENCES aluno (codaluno)
);

-- -----------------------------------------------------
-- Table turma
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS turma (
  	codturma          INT      NOT NULL,
  	nometurma         VARCHAR(45)  NULL,
  	quantidadealunos  INT          NULL,
  
	PRIMARY KEY (codturma)
);

-- -----------------------------------------------------
-- Table turma_aluno
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS turma_aluno (
  	codturma_aluno  INT       NOT NULL,
  	codaluno 		INT 	  NOT NULL,
  	codturma 		INT 	  NOT NULL,
	
  	PRIMARY KEY (codturma_aluno, codaluno, codturma),
    CONSTRAINT fk_turma_aluno_aluno1 FOREIGN KEY (codaluno) REFERENCES aluno (codaluno),
    CONSTRAINT fk_turma_aluno_turma1 FOREIGN KEY (codturma) REFERENCES turma (codturma)
);

-- -----------------------------------------------------
-- Table log
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS log(
	codlog 		  INT 	   NOT NULL,
	descricaolog  VARCHAR(45)  NULL,
	
	PRIMARY KEY (codlog)
);

-- -----------------------------------------------------
-- Testes - SELECT * FROM TABLES
-- -----------------------------------------------------

SELECT * FROM professor;
SELECT * FROM disciplina;
SELECT * FROM aluno;
SELECT * FROM nota;
SELECT * FROM turma;
SELECT * FROM turma_aluno;
SELECT * FROM log;

