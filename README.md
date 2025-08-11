# vbscript-transpiler

## Vorbereitung
Für die Verwendung des Transpilers muss ein Python-Interpreter installiert sein. Der Transpiler wurde mit Python der Version 3.13.3 entwickelt. Diese Version sollte mindestens
verwendet werden, um Probleme durch Versionsunterschiede zu vermeiden.

Die notwendigen Module können über die requirements.txt aus dem Stammverzeichnis des Repositories installiert werden.
Das erfolgt mit dem Befehl "pip install -r requirements.txt". Wird pip nicht im Stammverzeichnis des Repository ausgefürt musst der Pfad für die requirements.txt angegeben werden.

Wenn die Visualisierung des AST gewünscht ist muss Graphviz [https://graphviz.org/] installiert werden.

## Grammatik

Die Grammatik liegt in dem Verzeichnis Grammar. Wurde die Grammatik angepasst, kann neuer Quellcode für den Lexer, Parser, Visitor etc. generiert werden
Dafür ist eine aktuelle Java Installation notwendig.
Die Grammatik kann mit dem Befehl 

"java -Xmx500M -cp "antlr-4.13.2-complete.jar" org.antlr.v4.Tool -Dlanguage=Python3 .\grammar\VBScript.g4 -visitor -o .\gen"

generiert werden. Der Quellcode wird im Verzeichnis gen/grammar erzeugt und muss in den gen Ordner kopiert werden.

## Transpiler

Der Transpiler kann mit der main.py ausgeführt werden. Als Parameter werden --file oder --code und --output akzeptiert. Mit --file oder --code
kann der zu übersetzende Code als Datei oder direkt im Befehl mitgegeben werden. Der Paramaeter --output steuert, in welche Datei der übersetzte Code
geschrieben wird.

## Bibliotheken

Bei Übersetzung von Funktionen und Methoden die einen Import erforder, muss dieser in den Tabellen in ir/vbScriptMapping.py gepflegt werden.