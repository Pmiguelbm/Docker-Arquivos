#!/bin/bash

echo "🧪 Executando Testes do Sistema Django"
echo "======================================"

# Verificar se estamos no ambiente Docker
if [ -f /.dockerenv ]; then
    echo "🐳 Executando em container Docker"
else
    echo "💻 Executando em ambiente local"
fi

echo ""

# Executar linting
echo "🔍 Executando linting..."
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
if [ $? -eq 0 ]; then
    echo "✅ Linting passou"
else
    echo "❌ Linting falhou"
    exit 1
fi

echo ""

# Formatar código
echo "🎨 Formatando código..."
black --check .
if [ $? -eq 0 ]; then
    echo "✅ Código está formatado"
else
    echo "⚠️ Código precisa ser formatado"
fi

echo ""

# Ordenar imports
echo "📦 Verificando imports..."
isort --check-only .
if [ $? -eq 0 ]; then
    echo "✅ Imports estão ordenados"
else
    echo "⚠️ Imports precisam ser ordenados"
fi

echo ""

# Executar testes
echo "🧪 Executando testes..."
python -m pytest -v --cov=file_upload --cov-report=html --cov-report=term-missing
if [ $? -eq 0 ]; then
    echo "✅ Todos os testes passaram"
else
    echo "❌ Alguns testes falharam"
    exit 1
fi

echo ""

# Executar testes de segurança
echo "🔒 Executando testes de segurança..."
python manage.py check --deploy
if [ $? -eq 0 ]; then
    echo "✅ Verificações de segurança passaram"
else
    echo "❌ Verificações de segurança falharam"
    exit 1
fi

echo ""
echo "🎉 Todos os testes foram executados com sucesso!"
echo "📊 Relatório de cobertura disponível em: htmlcov/index.html"
