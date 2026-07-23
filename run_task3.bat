@echo off
echo ==============================================
echo Running Task 3 Notebook Generator...
echo ==============================================
python generate_notebook_task3.py

echo.
echo ==============================================
echo Generating Task 3 Machine Learning Pipeline and PDF Report...
echo ==============================================
python generate_task3_report.py

echo.
echo ==============================================
echo Task 3 Complete! Check notebook/ and report/ folders.
echo ==============================================
pause
