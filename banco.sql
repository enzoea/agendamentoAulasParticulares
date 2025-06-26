CREATE DATABASE IF NOT EXISTS aulas_particulares;
use aulas_particulares;

CREATE TABLE IF NOT EXISTS aluno (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS professor (
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    especialidade VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS disciplina (
    id_disciplina INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS agenda (
    id_agenda INT AUTO_INCREMENT PRIMARY KEY,
    id_aluno INT,
    id_professor INT,
    id_disciplina INT,
    data_aula DATE NOT NULL,
    horario TIME NOT NULL,
    observacoes TEXT,
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno),
    FOREIGN KEY (id_professor) REFERENCES professor(id_professor),
    FOREIGN KEY (id_disciplina) REFERENCES disciplina(id_disciplina)
);

INSERT INTO professor (nome, email, telefone, especialidade)
VALUES ('Enzo Martins', 'enzo.martins@exemplo.com', '(11) 91234-5678', 'Banco de Dados');

INSERT INTO disciplina (nome, descricao)
VALUES ('Banco de Dados', 'Estudo de modelagem, SQL e estrutura de bancos relacionais.');

INSERT INTO aluno (nome, email, telefone) VALUES
('Ana Clara', 'ana.clara@email.com', '(11) 99876-5432'),
('João Pedro', 'joao.pedro@email.com', '(11) 98765-4321'),
('Mariana Silva', 'mariana.silva@email.com', '(11) 97654-3210');

INSERT INTO agenda (id_aluno, id_professor, id_disciplina, data_aula, horario, observacoes)
VALUES (1, 1, 1, '2025-06-20', '14:00:00', 'Primeira aula introdutória sobre modelagem de dados.');

SELECT * FROM aluno;
