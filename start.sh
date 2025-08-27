#!/bin/bash

echo "🚀 Iniciando Sistema de Upload de Arquivos Django"
echo "=================================================="

# Verificar se o Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker não está instalado. Por favor, instale o Docker primeiro."
    exit 1
fi

# Verificar se o Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose não está instalado. Por favor, instale o Docker Compose primeiro."
    exit 1
fi

echo "✅ Docker e Docker Compose encontrados"

# Parar containers existentes
echo "🛑 Parando containers existentes..."
docker-compose down

# Construir e iniciar containers
echo "🔨 Construindo e iniciando containers..."
docker-compose up --build -d

# Aguardar um pouco para o banco inicializar
echo "⏳ Aguardando inicialização do banco de dados..."
sleep 10

# Executar migrações
echo "🗄️ Executando migrações do banco de dados..."
docker-compose exec -T web python manage.py migrate

# Coletar arquivos estáticos
echo "📦 Coletando arquivos estáticos..."
docker-compose exec -T web python manage.py collectstatic --noinput

echo ""
echo "🎉 Sistema iniciado com sucesso!"
echo "=================================="
echo "🌐 Acesse a aplicação em: http://localhost"
echo "🔧 Admin Django em: http://localhost/admin"
echo ""
echo "📋 Comandos úteis:"
echo "  - Ver logs: docker-compose logs -f"
echo "  - Parar: docker-compose down"
echo "  - Reiniciar: docker-compose restart"
echo ""
echo "📁 Arquivos serão salvos em: ./uploads/"
