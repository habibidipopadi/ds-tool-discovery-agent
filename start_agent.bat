@echo off
cd /d %~dp0
call .venv\Scripts\activate
python -m src.agent.run_forever > crawler.log 2>&1