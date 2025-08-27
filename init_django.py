#!/usr/bin/env python
import os
import sys
import time
import psycopg2
from psycopg2 import OperationalError

def wait_for_db():
    """Aguarda o banco de dados estar pronto"""
    print("🔄 Aguardando banco de dados...")
    
    # Configurações do banco
    db_config = {
        'host': os.getenv('POSTGRES_HOST', 'db'),
        'port': os.getenv('POSTGRES_PORT', '5432'),
        'database': os.getenv('POSTGRES_DB', 'django_db'),
        'user': os.getenv('POSTGRES_USER', 'django_user'),
        'password': os.getenv('POSTGRES_PASSWORD', 'django_password'),
    }
    
    max_attempts = 30
    attempt = 0
    
    while attempt < max_attempts:
        try:
            print(f"📡 Tentativa {attempt + 1}/{max_attempts} de conectar ao banco...")
            conn = psycopg2.connect(**db_config)
            conn.close()
            print("✅ Banco de dados está pronto!")
            return True
        except OperationalError as e:
            print(f"❌ Erro de conexão: {e}")
            attempt += 1
            if attempt < max_attempts:
                print("⏳ Aguardando 2 segundos antes da próxima tentativa...")
                time.sleep(2)
    
    print("❌ Falha ao conectar ao banco de dados após várias tentativas")
    return False

def run_migrations():
    """Executa as migrações do Django"""
    print("🗄️ Executando migrações...")
    os.system("python manage.py migrate")

def collect_static():
    """Coleta arquivos estáticos"""
    print("📦 Coletando arquivos estáticos...")
    os.system("python manage.py collectstatic --noinput")

def main():
    """Função principal"""
    print("🚀 Iniciando Django...")
    
    # Aguarda o banco estar pronto
    if not wait_for_db():
        sys.exit(1)
    
    # Executa migrações
    run_migrations()
    
    # Coleta arquivos estáticos
    collect_static()
    
    print("✅ Django inicializado com sucesso!")

if __name__ == "__main__":
    main()
