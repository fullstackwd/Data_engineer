CREATE TABLE Curso(
	numcurso int NOT NULL,
	nome varchar(60),
	totalcreditos int,
	
	PRIMARY KEY(numcurso)
);

INSERT INTO Curso Values(2142, 'Engenharia Cívil', 1500),
						(2143, 'Ciência da Computação', 2000),
						(2144, 'Direito', 1750),
						(2145, 'Pedagogia', 1500),
						(2146, 'Odontologia', 1600);
						
Select * from curso;

CREATE TABLE Aluno(
	numaluno int NOT NULL,
	nome varchar(60),
	endereco varchar(60),
	cidade varchar(20),
	telefone varchar(20),
	curso_fk int,
	PRIMARY KEY (numaluno),
	FOREIGN KEY (curso_fk) REFERENCES curso (numcurso)
);

INSERT INTO aluno VALUES (111,'Edvaldo Carlos Silva','Av Sao Carlos, 186','Sao Carlos-SP','(017)276-9999',2143),
						 (112,'Joao Benedito Scapin','R Jose Bonifacio, 70','Sao Carlos-SP','(017)276-9999',2142),
						 (113,'Carol Antonia Silveira','R Luiz Camoes, 120','Ibate -SP','(017)276-9999',2145),
					     (114,'Marcos Joao Casanova','Av Sao Carlos, 176','Sao Carlos-SP','(017)276-9999',2143),
						 (115,'Simone Cristina Lima','R Raul Junior, 180','Sao Carlos-SP','(017)276-9999',2144),
						 (116,'Ailton Castro','R Antonio Carlos,120','Ibate -SP','(017)276-9999',2142),
						 (117,'Jose Paulo Figueira','R XV Novembro, 871','Sao Carlos-SP','(017)276-9999',2145);
						 
CREATE TABLE professor (
	numprof int NOT NULL,
	nome varchar(40),
	areapesquisa varchar(40),
	
	PRIMARY KEY (numprof)

);

INSERT INTO professor VALUES (45675,'Abgair Simon Ferreira','Banco de Dados'),
							(45690,'Ramon Travanti','Direito Romano'),
							(45691,'Gustavo Golveia Netto','Sociologia'),
							(45692,'Marcos Salvador','Matematica Financeira'),
							(45693,'Cintia Falcao','Engenharia de Software');

CREATE TABLE disciplinas (
	numdisp int NOT NULL,
	nome varchar(40),
	quantcreditos int,

	PRIMARY KEY (numdisp)

);			


INSERT INTO disciplinas VALUES(1,'Banco de Dados',30),
							  (2,'Estrutura de Dados',30),
							  (3,'Direito Penal',25),
							  (4,'Calculo Numerico',30),
							  (5,'Psicologia Infantil',25),
							  (6,'Direito Tributario',33),
							  (7,'Engenharia de Software',27);

select * from disciplinas;

CREATE TABLE aula (
	aluno_fk int NOT NULL,
	disciplinas_fk int NOT NULL,
	professor_fk int NOT NULL,
	semestre varchar(7) NOT NULL,
	nota int,
	
	PRIMARY KEY (aluno_fk, disciplinas_fk, professor_fk, semestre),
	FOREIGN KEY (professor_fk) REFERENCES professor (numprof),
	FOREIGN KEY (disciplinas_fk) REFERENCES disciplinas (numdisp),
	FOREIGN KEY (aluno_fk) REFERENCES aluno (numaluno)
);

INSERT INTO aula VALUES (111,1,45675,'01/1998',9),
						(111,2,45675,'01/1998',6),
						(111,2,45675,'02/1998',7),
						(111,4,45692,'01/1998',8),
						(111,7,45693,'01/1998',10),
						(112,4,45692,'01/1998',7),
						(112,7,45693,'01/1998',6),
						(112,7,45693,'02/1998',10),
						(113,5,45691,'01/1998',8),
						(114,1,45675,'01/1998',7),
						(114,2,45675,'01/1998',8),
						(114,4,45692,'01/1998',7),
						(114,4,45692,'02/1998',9),
						(114,7,45693,'01/1998',10),
						(115,3,45690,'01/1998',5),
						(115,3,45690,'02/1998',8),
						(115,6,45690,'01/1998',9),
						(116,4,45692,'01/1998',4),
						(116,4,45692,'02/1998',10),
						(116,7,45693,'01/1998',9);
						
CREATE TABLE disciplinacurso (
	disciplinas_fk int NOT NULL,
	curso_fk      int NOT NULL,
	
	PRIMARY KEY (disciplinas_fk,curso_fk),
	FOREIGN KEY (disciplinas_fk) REFERENCES disciplinas (numdisp),
	FOREIGN KEY (curso_fk) REFERENCES curso (numcurso)

);

INSERT INTO disciplinacurso VALUES (4,2142),(7,2142),(1,2143),(2,2143),(4,2143),(7,2143),(3,2144),(6,2144),(5,2145);

select * from disciplinacurso;
