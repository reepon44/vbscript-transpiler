VB_TO_PY_FUNC_MAP = {
    "wscript.echo": { "type" : "function", "name" : "print", "import": None},
    "Nothing": {"type" : None, "function" : None, "import": None},
    "trim": { "type" : "method", "name" : "strip", "import": None},
    "mid": {"type" : "function", "name": "vb_Translation.mid", "import": "vb_Translation"},
    "split": {"type": "function", "name": "vb_Translation.split", "import": "vb_Translation"},
    "left": {"type": "function", "name": "vb_Translation.left", "import": "vb_Translation"},
    "join": {"type": "function", "name": "vb_Translation.join", "import": "vb_Translation"},
    "close": {"type": "method", "name": "close", "import": None},
    "log_endetext": {"type": "function", "name": "log_inc_mys1.log_endetext", "import": "log_inc_mys1"},
    "log_start": {"type": "function", "name": "log_inc_mys1.log_start", "import": "log_inc_mys1"}
}

VB_TO_PY_OBJ_MAP = {
    ("wscript", "echo"): (None, "print"),
    (None, "files"): ("shutil", "iterdir"),
    (None, "copy"):("shutil", "copy"),
    (None, "writeline"): (None, "vb_Translation.writeline"),
    (None, "close"): (None, "close"),
    (None, "getFolder"): ("pathlib", "Path")
}

VB_TO_PY_IMP_MAP = {
    'copy' : { "path" : None, "file" : "shutil"},
    'vb_Translation': {"path" : None, "file" : "vb_Translation"}
}