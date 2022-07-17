from PyQt5 import uic

with open("mains.py", "w", encoding="utf-8") as fout:
    uic.compile.Ui('ScriptHUB.ui', fout)
