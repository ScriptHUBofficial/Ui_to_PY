from PyQt5 import uic

with open('yourname.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('ScriptHUB.ui', fout)
