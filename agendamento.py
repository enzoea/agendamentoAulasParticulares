import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="enzo123",
        database="aulas_particulares"
    )

def cadastrar_aluno(cursor):
    nome = input("Nome do aluno: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    cursor.execute("""
        INSERT INTO aluno (nome, email, telefone)
        VALUES (%s, %s, %s)
    """, (nome, email, telefone))
    print("Aluno cadastrado com sucesso!")

def cadastrar_professor(cursor):
    nome = input("Nome do professor: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    especialidade = input("Especialidade: ")

    cursor.execute("""
        INSERT INTO professor (nome, email, telefone, especialidade)
        VALUES (%s, %s, %s, %s)
    """, (nome, email, telefone, especialidade))
    print("Professor cadastrado com sucesso!")

def cadastrar_disciplina(cursor):
    nome = input("Nome da disciplina: ")
    descricao = input("Descrição: ")

    cursor.execute("""
        INSERT INTO disciplina (nome, descricao)
        VALUES (%s, %s)
    """, (nome, descricao))
    print("Disciplina cadastrada com sucesso!")

def registrar_aula(cursor):
    print("Informe os IDs para registrar a aula:")
    id_aluno = input("ID do aluno: ")
    id_professor = input("ID do professor: ")
    id_disciplina = input("ID da disciplina: ")
    data_aula = input("Data da aula (AAAA-MM-DD): ")
    horario = input("Horário (HH:MM:SS): ")
    obs = input("Observações: ")

    cursor.execute("""
        INSERT INTO agenda (id_aluno, id_professor, id_disciplina, data_aula, horario, observacoes)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (id_aluno, id_professor, id_disciplina, data_aula, horario, obs))
    print("Aula registrada com sucesso!")

def exibir_agenda(cursor):
    cursor.execute("""
        SELECT a.id_agenda, al.nome AS aluno, p.nome AS professor, d.nome AS disciplina, 
               a.data_aula, a.horario, a.observacoes
        FROM agenda a
        JOIN aluno al ON a.id_aluno = al.id_aluno
        JOIN professor p ON a.id_professor = p.id_professor
        JOIN disciplina d ON a.id_disciplina = d.id_disciplina
    """)
    resultados = cursor.fetchall()
    print("\n--- AGENDA DE AULAS ---")
    for row in resultados:
        print(f"Aula #{row[0]} | Aluno: {row[1]} | Professor: {row[2]} | Disciplina: {row[3]} | Data: {row[4]} | Hora: {row[5]} | Obs: {row[6]}")

while True:
        print("\n=== SISTEMA DE AULAS PARTICULARES ===")
        print("1. Cadastrar aluno")
        print("2. Cadastrar professor")
        print("3. Cadastrar disciplina")
        print("4. Registrar aula")
        print("5. Ver agenda de aulas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        try:
            conexao = conectar()
            cursor = conexao.cursor()

            if opcao == '1':
                cadastrar_aluno(cursor)
            elif opcao == '2':
                cadastrar_professor(cursor)
            elif opcao == '3':
                cadastrar_disciplina(cursor)
            elif opcao == '4':
                registrar_aula(cursor)
            elif opcao == '5':
                exibir_agenda(cursor)
            elif opcao == '0':
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

            conexao.commit()
            cursor.close()
            conexao.close()

        except mysql.connector.Error as erro:
            print("Erro ao conectar ou executar no MySQL:", erro)
