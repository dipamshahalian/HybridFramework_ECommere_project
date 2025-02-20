@REM @echo on
cd C:\Users\Alian-172\Desktop\HybridFramework_ECommere_project
@REM .venv\Scripts\activate
pytest -v -s -m "sanity" testCases/  --browser chrome
@REM pytest -v -s -m "sanity" testCases/  --browser firefox
@REM pause
