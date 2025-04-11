import sqlite3

class AppBd():
    def __init__(self):
        self.create_table()


    def abrirconexao(self):
        try:
            self.connect = sqlite3.connect("database.db")
        except sqlite3.Error as erro:
            print(f"Ocorreu um erro ao abrir o banco de dodos {erro}")

    def fecharconexao(self):
        try:
            self.connect.close()
            print("Banco foi fechado com sucesso")
        except sqlite3.Error as erro:
            print(f"falha ao fechar o banco {erro}")

    def create_table(self):
        create_table_query = """CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY,
                                                                    name TEXT NOT NULL,
                                                                    price REAL NOT NULL)"""
        self.abrirconexao()                    
        try:                                                
            cursor = self.connect.cursor()
            cursor.execute(create_table_query)
            self.connect.commit()
        except sqlite3.Error as erro:
            print(f"falha ao criar a tabela {erro}")
        finally:
            if self.connect:
                cursor.close()
                self.fecharconexao()

    def inserirdados(self,name, price):
        self.abrirconexao()
        insert_query = """INSERT INTO products (name, price) VALUES (?, ?)"""
        try:
            cursor = self.connect.cursor()
            cursor.execute(insert_query, (name, price))
            self.connect.commit()
            print("Produto foi cadastrado com sucesso")
        except sqlite3.Error as erro:
             print(f"falha ao inserir dado {erro}")
        finally:
            if self.connect:
                cursor.close()
                self.fecharconexao()

    def select_all_products(self):
        self.abrirconexao() 
        select_query = """SELECT * FROM products """
        products = []
        try:
            cursor = self.connect.cursor()
            cursor.execute(select_query)
            products = cursor.fetchall()
        except sqlite3.Error as erro:
             print(f"falha ao listar os dados{erro}")
        finally:
            if self.connect:
                cursor.close()
                self.fecharconexao()
            return products
            
            
    def atualizar_produto(self, name, price, id):
        self.abrirconexao()
        update_query = f"UPDATE products SET name = ?, price = ? WHERE id = ?"
        try:
            cursor = self.connect.cursor()
            cursor.execute(update_query,(name, price, id))
            self.connect.commit()
            print("Produto foi atualizado com sucesso")
        except sqlite3.Error as erro:
            print(f"falha ao atualizar dados {erro}")
        finally:
            if self.connect:
                cursor.close()
                self.fecharconexao()

    def deletar_produto(self, id):
        self.abrirconexao()
        delete_query = f"DELETE FROM products WHERE id = ?"
        try:
            cursor = self.connect.cursor()
            cursor.execute(delete_query, id)
            self.connect.commit()
            print("Produto deletado com sucesso")
        except sqlite3.Error as erro:
            print(f"falha a deletar produto {erro}")
        finally:
            if self.connect:
                cursor.close()
                self.fecharconexao()

    def fazer_busca(self, nome):
        self.abrirconexao()
        busca_query = f"SELECT * FROM products WHERE name LIKE ? ORDER BY name ASC"
        nomesBuscados = []
        try:
            cursor = self.connect.cursor()
            cursor.execute(busca_query, (nome,))
            nomesBuscados = cursor.fetchall()
        except Exception as e:
            print("Não foi possível fazer a busca, " + str(e))

        finally:
            self.fecharconexao()
            return nomesBuscados
        