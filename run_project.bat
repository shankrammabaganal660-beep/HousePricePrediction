@echo off
echo ==============================================
echo Installing requirements...
echo ==============================================
pip install -r requirements.txt

echo.
echo ==============================================
echo Running Machine Learning Pipeline...
echo ==============================================
python ml_pipeline.py

echo.
echo ==============================================
echo Generating PDF Report and PPTX Presentation...
echo ==============================================
python generate_docs.py

echo.
echo ==============================================
echo All Done! Check the model, report, and presentation folders.
echo ==============================================
pause
