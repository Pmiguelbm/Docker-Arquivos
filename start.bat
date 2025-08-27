@echo off
echo 🚀 Iniciando Sistema de Upload de Arquivos Django
echo ==================================================

REM Verificar se o Docker está instalado
docker --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker não está instalado. Por favor, instale o Docker primeiro.
    pause
    exit /b 1
)

REM Verificar se o Docker Compose está instalado
docker-compose --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Docker Compose não está instalado. Por favor, instale o Docker Compose primeiro.
    pause
    exit /b 1
)

echo ✅ Docker e Docker Compose encontrados

REM Parar containers existentes
echo 🛑 Parando containers existentes...
docker-compose down

REM Construir e iniciar containers
echo 🔨 Construindo e iniciando containers...
docker-compose up --build -d

REM Aguardar um pouco para o banco inicializar
echo ⏳ Aguardando inicialização do banco de dados...
timeout /t 10 /nobreak >nul

REM Executar migrações
echo 🗄️ Executando migrações do banco de dados...
docker-compose exec -T web python manage.py migrate

REM Coletar arquivos estáticos
echo 📦 Coletando arquivos estáticos...
docker-compose exec -T web python manage.py collectstatic --noinput

echo.
echo 🎉 Sistema iniciado com sucesso!
echo ==================================
echo 🌐 Acesse a aplicação em: http://localhost
echo 🔧 Admin Django em: http://localhost/admin
echo.
echo 📋 Comandos úteis:
echo   - Ver logs: docker-compose logs -f
echo   - Parar: docker-compose down
echo   - Reiniciar: docker-compose restart
echo.
echo 📁 Arquivos serão salvos em: ./uploads/
pause
