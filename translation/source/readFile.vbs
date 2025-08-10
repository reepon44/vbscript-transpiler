' Ein einfaches VBScript zur Testzwecken

Set fso = CreateObject("Scripting.FileSystemObject")
Set file = fso.OpenTextFile("C:\temp\test.txt", 1)

Do Until file.AtEndOfStream
    line = file.ReadLine
    WScript.Echo line
Loop

file.Close
Set file = Nothing
Set fso = Nothing
