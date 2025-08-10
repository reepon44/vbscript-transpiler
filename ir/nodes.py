from .vbscriptMapping import VB_TO_PY_OBJ_MAP, VB_TO_PY_FUNC_MAP, VB_TO_PY_IMP_MAP
from gen.VBScriptParser import VBScriptParser
from pathlib import Path

def indent_multiline(code: str, indent_level: int) -> str:
    indent_str = "    " * indent_level
    return "\n".join(indent_str + line if line.strip() else line for line in code.splitlines())

def contains_readline_call(node):
    if isinstance(node, Procedure):
        return (
            node.obj_name.lower() == "file" and
            node.proc_name.lower() == "readline"
        )
    if isinstance(node, Assignment):
        if isinstance(node.value, str):
            if "readline" in node.value.lower():
                return True
        return contains_readline_call(node.value)
    if hasattr(node, "__dict__"):
        for attr in vars(node).values():
            if isinstance(attr, list):
                for item in attr:
                    if contains_readline_call(item):
                        return True
            elif isinstance(attr, (Assignment, Procedure)):
                if contains_readline_call(attr):
                    return True
    return False


class OpenFile:
    def __init__(self, var_name, path, mode, body):
        self.var_name = var_name
        self.path = path
        self.mode = mode
        self.body = body
    
    #def to_code(self, indent):
    #    indent_str = "    " * indent
    #    inner_indent = indent + 1
    #    if self.mode == '1':
    #        control_seq = f'with open("{self.path}", "r") as {self.var_name}:\n'
    #        body_seq = ""
    #        for node in self.body:
    #            if isinstance(node, Procedure) and self.var_name == node.obj_name and node.proc_name.lower() == 'Close':
    #                pass
    #            else :
    #                body_seq += node.to_code((inner_indent)) + "\n"
    #        return control_seq+body_seq
    #    elif self.mode == '8':
    #        control_seq = f'with open("{self.path}", "a") as {self.var_name}:\n'
    #        body_seq = ""
    #        for node in self.body:
    #            if isinstance(node, Procedure) and self.var_name == node.obj_name and node.proc_name.lower() == 'Close':
    #                pass
    #            else :
    #                body_seq += node.to_code(inner_indent) + "\n"
    #        return indent_str+control_seq+body_seq
    def to_code(self, indent):
        modes = {
            '1' : "r",
            '2' : "w",
            '8' : "a"
        }
        return f"{self.var_name} = open('{self.path.replace('\\', '\\\\')}', '{modes.get(self.mode)}')"

class ForEachLine:
    def __init__(self, file_var, line_var, body):
        self.file_var = file_var
        self.line_var = line_var
        self.body = body

class PrintStatement:
    def __init__(self, value):
        self.value = value

class CloseFile:
    def __init__(self, var_name):
        self.var_name = var_name

class Assignment:
    def __init__(self, var_name, value):
        self.var_name = var_name
        self.value = value

    def to_code(self, indent):
        indent_str = "    " * indent
        #if isinstance(self.value, FunctionCall):
        #    return f"{self.var_name} = {self.value.to_code(0)}"
        #elif isinstance(self.value, list):
        #    values = ""
        #    for value in self.value:
        #        values += value
        #    return f"{self.var_name} = {values}"
        #if self.value.lower() == "true":
        #    return f"{self.var_name} = True"
        #elif self.value.lower() == "false":
        #    return f"{self.var_name} = False"
        #return f"{self.var_name} = {self.value}"
        if isinstance(self.value, (FunctionCall | Procedure | DictionaryAccess)):
            value = self.value.to_code(0)
        elif isinstance(self.value, list):
            value = ""
            for values in self.value:
                value += values
        else:
            value = f"{self.value}"
        if isinstance(self.var_name, (FunctionCall | Procedure | DictionaryAccess)):
            var = self.var_name.to_code(0)
        elif isinstance(self.var_name, str):
            var = f"{self.var_name}"
        if isinstance(value, str):
            if value.lower() == "nothing":
                value = "None"
            value = value.replace('\\', '\\\\')
        return f"{var} = {value}"

class Procedure:
    def __init__(self, obj_name, proc_name, arg):
        self.obj_name = obj_name
        self.proc_name = proc_name
        self.arg = arg
        self.obj_map = VB_TO_PY_OBJ_MAP
    
    def to_code(self, indent):
        if self.arg is not None:
            try:
                py_obj, py_func = VB_TO_PY_OBJ_MAP.get((self.obj_name.lower(), self.proc_name.lower()))
            except:
                try:
                    py_obj, py_func = VB_TO_PY_OBJ_MAP.get((None, self.proc_name.lower()))
                except:
                    return f"# Unknown function {self.obj_name}.{self.proc_name}"
            if py_obj == "shutil" and py_func == "copy":
                return f"{py_obj}.{py_func}({self.obj_name}, {self.arg[0]})"
            if py_obj and py_func:
                if isinstance(self.arg, (FunctionCall | Procedure)):
                    return f"{py_obj}.{py_func}({self.arg.to_code()})"
                else : return f"{py_obj}.{py_func}({self.arg})"
            elif (not py_obj) and py_func:
                if py_func == "close":
                    return f"{self.obj_name}.close()"
                if self.arg:
                    for instance in self.arg:
                        if isinstance(instance, str):
                            return f"{py_func}({instance})"
                        else : return f"{py_func}({instance.to_code(indent)})"
                else:
                    return f"{py_func}()"
        else:
            return f"{self.obj_name}.{self.proc_name}()"

class DoUntilLoop:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

#    def unpack_body(self):
#        stmts = []
#        for line in self.body:
#            for stmt in line:
#                stmts.append()
    
    def to_code(self, indent):
        if (self.condition.lower() == "true"):
            py_condition = f"not (True)"
        elif (self.condition.lower() == "false"):
            py_condition = f"not (False)"
        else:
            py_condition= f"not ({self.condition})"
        py_body = "\n".join(indent_multiline(stmt.to_code(indent+1), indent+1) for stmt in self.body)
        indent = " " * (4*indent) 
        return f"while {py_condition}:\n{py_body}"

class ForEachLoop:
    def __init__(self, iterable, variable, body):
        self.iterable = iterable
        self.variable = variable
        self.body = body
    
    def to_code(self, indent):
        py_condition = f"for {self.variable} in {self.iterable}:\n"
        py_body = "\n".join(indent_multiline(stmt.to_code(indent), indent+1) for stmt in self.body)
        return (py_condition+py_body)
    
class IfMultiLine:
    def __init__(self, condition, ifBody, elseBody=None, elifBody=None, elifConditions=None):
        self.condition = condition
        self.ifBody = ifBody
        self.elseBody = elseBody
        self.elifBody = elifBody
        self.elifConditions = elifConditions
    
    def to_code(self, indent):
        indent_str = "    " * indent
        inner_indent = indent + 1
        if isinstance(self.condition, Comparison):
            py_condition = f"if {self.condition.to_code()} :\n"
        elif (self.condition.lower() == "true"):
            py_condition = f"if True :\n"
        elif (self.condition.lower() == "false"):
            py_condition = f"if False :\n"
        else:
            py_condition = f"if {self.condition} :\n"
        if_body = "\n".join(indent_multiline(stmt.to_code(indent), indent) for stmt in self.ifBody)
        if self.elseBody:
            else_body = "\n".join(indent_multiline(stmt.to_code(inner_indent), indent+1) for stmt in self.elseBody)
            return f"{py_condition}{indent_str}{if_body}\n{indent_str}else:\n{else_body}"
        elif self.elifBody:
            elif_body = "\n".join(indent_multiline(stmt.to_code(indent), indent) for stmt in self.elifBody)
            return f"{py_condition}{if_body}\nelif {self.elifConditions[0].to_code()} :\n{elif_body}"
        return f"{py_condition}{if_body}"
    
class ListVariable:
    def __init__(self, values):
        self.values = values
    
    def to_code(self):
        return ", ".join(self.values)

class FunctionCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args
    
    def to_code(self, indent):
        if self.name == "Array":
            return f"[{self.args.to_code()}]"
        else :
            try:
                func = VB_TO_PY_FUNC_MAP.get(self.name.lower())
            except:
                return f"# Error while trying to get translation for function {func.get("name")}"
            if self.args:
                if func and func.get("type") == "function":
                    if isinstance(self.args, str):
                        return f"{func.get("name")}({self.args})"
                    else:
                        return f"{func.get("name")}({self.args.to_code()})"
                elif func and func.get("type") == "method":
                    return f"{self.args.to_code()}.{func.get("name")}()"
                else : return f" Unknown function {self.name}"
            else:
                if func:
                    return f"{func.get("name")}()"

class DictionaryAccess:
    def __init__(self, name, key):
        self.name = name
        self.key = key
    
    def to_code(self, indent):
        if isinstance(self.key, ListVariable):
            return f"{self.name}[{self.key.to_code()}]"
        return f"{self.name}[{self.key}]"

class Addition:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def to_code(self):
        return f"{self.left.to_code()} + {self.right.to_code()}"
    
class Import:
    def __init__(self, path, alias=None):
        self.path = path
        self.alias = alias
    
    def to_code(self, indent):
        sys = "import sys\n"
        imp = VB_TO_PY_IMP_MAP.get(self.path)
        if imp["path"]:
            append = f"sys.path.append('{imp["path"].replace('\\', '\\\\')}')\n"
            return sys+append+f"import {imp["file"]}"
        elif not (imp["path"]) and imp["file"]:
            return f"import {imp["file"]}"


class ForEachFile:
    def __init__(self, iterable, variable, body):
        self.iterable = iterable
        self.variable = variable
        self.body = body

    def to_code(self, indent):
        indent_str = "    " * indent
        inner_indent = indent + 1
        inner_inner_indent = indent + 2

        if "." in self.iterable:
            filelist = self.iterable.split('.')[0]
        py_condition = indent_str + (f"for {self.variable} in {filelist}.iterdir():\n") + ("    " * inner_indent) + f"if {self.variable}.is_file():\n"
        py_body = "\n".join(indent_multiline(stmt.to_code(indent), inner_inner_indent) for stmt in self.body)
        return (py_condition+py_body)
    
class Comparison:
    def __init__(self, leftValue, rightValue):
        self.leftValue = leftValue
        self.rightValue = rightValue
    # Caling node should handle indent
    def to_code(self):
        if isinstance(self.leftValue, (FunctionCall, Procedure, DictionaryAccess)):
            self.leftValue = self.leftValue.to_code(0)
        return f"{self.leftValue} == {self.rightValue}"
    
class DoUntilStreamEnd:
    def __init__(self, file, body):
        self.file = file
        self.body = body
    
    def to_code(self, indent):
        check_body = [stmt for stmt in self.body if not contains_readline_call(stmt)]
        py_condition = f"for line in {self.file}:\n"
        py_body = "\n".join(indent_multiline(stmt.to_code(indent+1), indent+1) for stmt in check_body)
        return f"{py_condition}{py_body}"