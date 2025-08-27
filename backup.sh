#!/bin/bash

# Script de backup automático para o banco de dados PostgreSQL

BACKUP_DIR="./backups"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="django_db_backup_$DATE.sql"

echo "🔄 Iniciando backup do banco de dados..."
echo "Data/Hora: $(date)"
echo "Arquivo: $BACKUP_FILE"

# Criar diretório de backup se não existir
mkdir -p $BACKUP_DIR

# Executar backup
docker-compose exec -T db pg_dump -U django_user django_db > "$BACKUP_DIR/$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "✅ Backup realizado com sucesso!"
    echo "📁 Arquivo salvo em: $BACKUP_DIR/$BACKUP_FILE"
    
    # Comprimir o backup
    gzip "$BACKUP_DIR/$BACKUP_FILE"
    echo "🗜️ Backup comprimido: $BACKUP_DIR/$BACKUP_FILE.gz"
    
    # Manter apenas os últimos 7 backups
    find $BACKUP_DIR -name "*.gz" -mtime +7 -delete
    echo "🧹 Backups antigos removidos (mais de 7 dias)"
else
    echo "❌ Erro ao realizar backup!"
    exit 1
fi

echo "🎉 Backup concluído!"
