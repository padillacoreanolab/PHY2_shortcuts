@echo off
echo Starting PHY2...
%windir%\System32\cmd.exe "/C" C:\ProgramData\anaconda3\Scripts\activate.bat phy2 
echo phy2 environment activated...
@SET /p param_path=Enter Params.py file path:
START "" /min cmd.exe /c "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Anaconda Prompt (anaconda3).lnk"
%windir%\System32\cmd.exe "/K" phy template-gui %param_path%/params.py
