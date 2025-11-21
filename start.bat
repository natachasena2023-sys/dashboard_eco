@echo off
echo ============================================
echo     Iniciando Dashboard Eco (Streamlit)
echo ============================================

cd /d "%~dp0"

echo Activando entorno virtual...
call .venv\Scripts\activate

echo Limpiando cache de Streamlit...
streamlit cache clear

echo Ejecutando aplicación...
streamlit run main.py

pause
