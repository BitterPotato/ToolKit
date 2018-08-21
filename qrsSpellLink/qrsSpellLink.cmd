@echo off
>output.tmp python "%~dp0qrsSpellLink.py" "%~dp1%~nx1"
<output.tmp (
    set /p res=
)
echo %res% | clip
del output.tmp
REM echo "%res% has been send to clip board"
REM pause
