@echo off
echo 🧪 Executando Testes do Sistema Django
echo ======================================

REM Verificar se estamos no ambiente Docker
if exist /.dockerenv (
    echo 🐳 Executando em container Docker
) else (
    echo 💻 Executando em ambiente local
)

echo.

REM Executar linting
echo 🔍 Executando linting...
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
if errorlevel 1 (
    echo ❌ Linting falhou
    pause
    exit /b 1
) else (
    echo ✅ Linting passou
)

echo.

REM Formatar código
echo 🎨 Formatando código...
black --check .
if errorlevel 1 (
    echo ⚠️ Código precisa ser formatado
) else (
    echo ✅ Código está formatado
)

echo.

REM Ordenar imports
echo 📦 Verificando imports...
isort --check-only .
if errorlevel 1 (
    echo ⚠️ Imports precisam ser ordenados
) else (
    echo ✅ Imports estão ordenados
)

echo.

REM Executar testes
echo 🧪 Executando testes...
python -m pytest -v --cov=file_upload --cov-report=html --cov-report=term-missing
if errorlevel 1 (
    echo ❌ Alguns testes falharam
    pause
    exit /b 1
) else (
    echo ✅ Todos os testes passaram
)

echo.

REM Executar testes de segurança
echo 🔒 Executando testes de segurança...
python manage.py check --deploy
if errorlevel 1 (
    echo ❌ Verificações de segurança falharam
    pause
    exit /b 1
) else (
    echo ✅ Verificações de segurança passaram
)

echo.
echo 🎉 Todos os testes foram executados com sucesso!
echo 📊 Relatório de cobertura disponível em: htmlcov/index.html
pause
