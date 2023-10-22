import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def create_database(self):
        query = """CREATE DATABASE users_big_project"""
        await self.connector.execute(query)

    async def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS users_table(
                   user_id text PRIMARY KEY,
                   user_name text NOT NULL,
                   first_name text NOT NULL,
                   balance int NOT NULL,
                   purchase_count int NOT NULL)"""
        await self.connector.execute(query)

    async def add_data(self, user_id, user_name, first_name, balance, purchase_count):
        query = f"""INSERT INTO users_table (user_id, user_name, first_name, balance, purchase_count)
                   VALUES ('{user_id}', '{user_name}', '{first_name}', '{balance}', '{purchase_count}') 
                   ON CONFLICT DO NOTHING"""
        await self.connector.execute(query)

    async def get_info(self, user_id):
        query = f"""SELECT user_id, user_name, first_name, balance, purchase_count
                    FROM users_table
                    WHERE user_id = '{user_id}'"""
        result_list = await self.connector.fetch(query)
        return result_list

    async def add_balance(self, count, user_id):
        query = f"UPDATE users_table SET balance = balance + {count} WHERE user_id='{user_id}'"
        await self.connector.execute(query)

    async def decreased_balance(self, count, user_id):
        query = f"UPDATE users_table SET balance = balance - {count} WHERE user_id='{user_id}'"
        await self.connector.execute(query)

    async def get_balance(self, user_id):
        query = f"""SELECT balance
                            FROM users_table
                            WHERE user_id = '{user_id}'"""
        result = await self.connector.fetchval(query)
        return result
