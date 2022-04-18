-- 5. Quais os nomes das disciplinas do curso de Ciência da Computação.
SELECT Cr.nome FROM Curso Cr, DisciplinaCurso Dc WHERE Cr.numcurso = 2143 AND Dc.curso_fk = Cr.numcurso;
/*
2142, 'Engenharia Cívil'
2143, 'Ciência da Computação'
2144, 'Direito'
2145, 'Pedagogia'
2146, 'Odontologia'
*/

-- 6. Quais os nomes dos cursos que possuem no curriculum a disciplina Cálculo Numérico.
SELECT Cr.nome FROM Curso Cr, DisciplinaCurso Dc WHERE Dc.disciplinas_fk = 4 AND Dc.curso_fk = Cr.NumCurso;

-- 7. Quais os nomes das disciplina que o aluno Marcos João Casanova cursou no 1º semestre de 1998.
SELECT D.Nome FROM Aluno Al, Aula Au, Disciplinas D WHERE	Al.Nome ~ 'Joao Casanova' 
AND Al.numaluno = Au.aluno_fk AND D.numdisp = Au.disciplinas_fk	AND Au.semestre ~ '01/1998';

-- 8. Quais os nomes das disciplinas que o aluno Ailton Castro foi reprovado.
SELECT D.Nome FROM Aluno Al, Aula Au, Disciplinas D WHERE Al.Nome ~ 'Ailton Castro' 
AND Au.aluno_fk = Al.numaluno AND Au.disciplinas_fk = D.NumDisp AND Au.nota < 7;

-- 9. Quais os nomes de alunos reprovados na disciplina de Cálculo Numérico no 1º semestre de 1998.
SELECT Al.Nome FROM Aluno Al, Aula Au, Disciplinas D WHERE	Au.aluno_fk = Al.numaluno 
AND Au.disciplinas_fk = D.numdisp AND D.Nome ~ 'Calculo Numerico' AND Au.Nota < 7;

-- 10. Quais os nomes das disciplinas ministradas pelo prof. Ramon Travanti.
SELECT DISTINCT D.Nome AS Disciplina FROM Disciplinas D, Professor P, Aula Au 
WHERE	P.numprof = Au.professor_fk	AND D.NumDisp = Au.disciplinas_fk AND P.Nome ~ 'Ramon Travanti';

-- 11. Quais os nomes dos professores que já ministraram aula de Banco de Dados.
SELECT DISTINCT P.Nome AS Professor FROM Disciplinas D, Aula Au, Professor P WHERE	Au.professor_fk = P.numprof
AND D.numdisp = Au.disciplinas_fk AND D.nome ~* 'Banco de Dados';

-- 12. Qual a maior e a menor nota na disciplina de Cálculo Numérico no 1º semestre de 1998
SELECT MIN(Au.nota), MAX(Au.nota) FROM aula Au, Disciplinas D WHERE Au.disciplinas_fk = D.numdisp AND Au.semestre ~'01/1998';

-- 13 Qual o nome do aluno que obteve maior nota na disciplina de Engenharia de Software no 1º semestre de 1998. 
SELECT Al.nome, Au.nota FROM (SELECT MAX(Au.nota) FROM  Aluno Al, aula Au, Disciplinas D
WHERE Au.aluno_fk = Al.numaluno AND D.numdisp = Au.disciplinas_fk AND D.nome = 'Engenharia de Software' 
AND Au.semestre = '01/1998') AS M, Aluno Al, aula Au, Disciplinas D WHERE Au.aluno_fk = Al.numaluno AND D.numdisp = Au.disciplinas_fk
AND D.nome = 'Engenharia de Software' AND Au.semestre ~ '01/1998' AND Au.nota = M.max;

-- 14. Quais nomes de alunos, nome de disciplina e nome de professores que cursaram o 1º semestre de 1998 em ordem de aluno.
SELECT Al.nome AS Aluno, D.nome AS Disciplina, P.nome AS Professor FROM Aluno Al, aula Au, DisciplinaS D, Professor P 
WHERE Au.aluno_fk = Al.numaluno	AND Au.professor_fk = P.numprof AND Au.disciplinas_fk = D.numdisp AND Au.semestre = '01/1998' ORDER BY Al.nome;

-- 15. Quais nomes de alunos, nomes de disciplinas e notas do 1º semestre de 1998 no curso de Ciência da Computação.
SELECT Al.nome AS Aluno, D.nome AS Disciplina, Au.nota FROM Aluno Al, aula Au, Curso C, Disciplinas D WHERE	Au.aluno_fk = Al.numaluno
 AND Al.curso_fk = C.numcurso AND Au.disciplinas_fk = D.numdisp	AND Au.semestre ~ '01/1998'	AND C.nome = 'Ciência da Computação';

-- 16. Qual a média de notas do professor Marcos Salvador.
SELECT AVG(Au.nota) FROM aula Au, Professor P WHERE Au.professor_fk = P.numprof	AND P.nome = 'Marcos Salvador';

-- 17. Quais os alunos que tiveram nota entre 5.0 e 7.0 em ordem alfabetica de disciplina.
SELECT Al.nome, D.nome Disciplina, Au.nota FROM Aluno Al, aula Au, Disciplinas D  WHERE Au.aluno_fk = Al.numaluno 
AND Au.disciplinas_fk = D.numdisp AND Au.nota >= 5.0 AND Au.nota <= 7.0 ORDER BY D.nome;

-- 18. Qual a média de notas da disciplina de Cálculo Numérico no 1º semestre de 1998.
SELECT AVG(Au.nota) FROM aula Au, Disciplinas D WHERE Au.disciplinas_fk = D.numdisp AND Au.semestre ~'01/1998';

-- 19 Quantos alunos o professor Abgair teve no 1º semestre de 1998.
SELECT COUNT(*) FROM (SELECT DISTINCT Au.aluno_fk FROM aula Au, Professor P WHERE Au.professor_fk = P.numprof 
AND Au.semestre ~ '01/1998' AND P.nome ~ 'Abgair')E;

-- 20 Qual a média de notas do aluno Edvaldo Carlos Silva.
SELECT AVG(Au.nota) FROM Aluno Al, aula Au WHERE Al.numaluno = Au.aluno_fk AND Al.nome ~ 'Edvaldo';

-- 21 Quais as médias das notas, por nome de disciplina, de todos os cursos do 1º semestre de 1998 em ordem alfabética de disciplina.
SELECT D.nome, AVG(Au.Nota) FROM Aula Au, Disciplinas D WHERE Au.disciplinas_fk = D.numdisp 
AND Au.semestre ~ '01/1998' GROUP BY D.nome ORDER BY D.nome;

-- 22. Quais as médias das notas, por nome de professor, no 1º semestre de 1998.
SELECT AVG(Au.nota), P.nome FROM aula Au, Professor P WHERE Au.professor_fk = P.numprof
AND Au.semestre = '01/1998' GROUP BY P.nome;

-- 23. Qual a média das notas, por disciplina, no 1º semestre de 1998 do curso de Ciência da Computação.
SELECT D.nome, AVG(Au.nota) FROM Aula Au, Disciplinas D, Curso Cr, DisciplinaCurso DC
WHERE Au.disciplinas_fk = D.NumDisp	AND Cr.NumCurso = DC.curso_fk AND DC.disciplinas_fk = D.NumDisp
AND Au.Semestre ~ '01/1998'	AND Cr.Nome ~ 'Ciência da Computação' GROUP BY D.Nome;

-- 24. Qual foi a quantidade de créditos concluídos (somente as disciplinas aprovadas) do aluno Edvaldo Carlos Silva.
SELECT SUM(D.quantcreditos) FROM Aluno Al, aula Au, Disciplinas D WHERE Au.nota >= 7.0 AND Al.nome = 'Edvaldo Carlos Silva'
AND Au.aluno_fk = Al.numaluno AND D.numdisp = Au.disciplinas_fk;

-- 25. Quais os nomes de alunos que já completaram 70 créditos (somente os aprovados na disciplina).
SELECT Al.nome, SUM(D.quantcreditos) cred FROM Aluno Al, aula Au, Disciplinas D WHERE Au.nota >= 7.0 
AND Au.aluno_fk = Al.numaluno AND D.numdisp = Au.disciplinas_fk GROUP BY Al.nome HAVING SUM(D.quantcreditos) > 70;

-- 26. Quais os nomes de alunos que cursaram o 1º semestre de 1998, pertencem ao curso de Ciência da Computação e possuem nota superior à 8.0. 
SELECT Al.nome Aluno, D.nome Disciplina, P.nome Professor FROM Aluno Al, aula Au, Curso Cr, Professor P, Disciplinas D
WHERE Au.aluno_fk = Al.numaluno AND Au.semestre ~ '01/1998' AND Al.curso_fk = Cr.numcurso AND Au.nota > 8.0 AND P.numprof = Au.professor_fk
AND Au.disciplinas_fk = D.numdisp;

-- 27. Qual a disciplina com nota mais baixa em qualquer época?
SELECT D.nome FROM Disciplinas D join aula Au ON Au.disciplinas_fk = D.numdisp WHERE Au.nota = (SELECT MIN(nota) FROM aula);


-- 28. Qual a disciplina com média de nota mais alta em qualquer época
SELECT D.nome FROM Disciplinas D JOIN aula Au ON Au.disciplinas_fk = D.numdisp
GROUP BY D.nome HAVING AVG(nota) >= ALL (SELECT AVG(nota) FROM aula GROUP BY disciplinas_fk);

-- 29. Quais alunos já concluiram o curso de Ciência da Computação? ATENÇÃO: Critério utilizado é de 115 Creditos.
SELECT Al.nome, SUM(D.quantcreditos) cred FROM Aluno Al, aula Au, Disciplinas D 
WHERE Au.aluno_fk = Al.numaluno AND D.numdisp = Au.disciplinas_fk GROUP BY Al.nome HAVING SUM(D.quantcreditos) > 115;

-- 30. Ordene as disciplinas por quantidade de reprovações. ATENÇÃO: Critério utilizado é nota menor que 5.
SELECT Al.nome, D.nome Disciplina, Au.nota FROM Aluno Al, aula Au, Disciplinas D  WHERE Au.aluno_fk = Al.numaluno 
AND Au.disciplinas_fk = D.numdisp AND Au.nota < 5.0 ORDER BY D.nome;