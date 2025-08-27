#!/bin/bash

# Script de monitoramento dos containers Docker

echo "🔍 Monitoramento do Sistema Django Docker"
echo "=========================================="
echo "Data/Hora: $(date)"
echo ""

# Verificar status dos containers
echo "📊 Status dos Containers:"
docker-compose ps
echo ""

# Verificar uso de recursos
echo "💾 Uso de Recursos:"
docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}\t{{.BlockIO}}"
echo ""

# Verificar logs recentes
echo "📝 Logs Recentes (últimas 10 linhas):"
echo "--- Django Web ---"
docker-compose logs --tail=10 web
echo ""
echo "--- Nginx ---"
docker-compose logs --tail=10 nginx
echo ""
echo "--- PostgreSQL ---"
docker-compose logs --tail=10 db
echo ""

# Verificar volumes
echo "💿 Status dos Volumes:"
docker volume ls --filter "name=django-docker-app"
echo ""

# Verificar conectividade
echo "🌐 Teste de Conectividade:"
if curl -s http://localhost/health/ > /dev/null; then
    echo "✅ Aplicação web respondendo"
else
    echo "❌ Aplicação web não responde"
fi

if curl -s http://localhost > /dev/null; then
    echo "✅ Nginx respondendo"
else
    echo "❌ Nginx não responde"
fi

echo ""
echo "🎯 Monitoramento concluído!"
