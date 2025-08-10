import ir.nodes

class PythonGenerator:
    def __init__(self, nodes):
        self.nodes = nodes
        self.lines = []

    def generate(self):
        in_with_block = False
        for node in self.nodes:
            if isinstance(node, ir.nodes.OpenFile) and node.path and node.mode == "1":
                self.lines.append(node.to_code(0))
                in_with_block = True
            elif isinstance(node, ir.nodes.PrintStatement):
                indent = "    " if in_with_block else ""
                self.lines.append(f'{indent}print({node.value})')
            elif isinstance(node, ir.nodes.CloseFile):
                pass  # unnötig bei `with`
            elif isinstance(node, ir.nodes.DoUntilLoop):
                self.lines.append(node.to_code(0))
            elif isinstance(node, ir.nodes.Assignment):
                self.lines.append(node.to_code(0))
            elif isinstance(node, ir.nodes.ForEachLoop):
                self.lines.append(node.to_code(0))
            elif isinstance(node, ir.nodes.IfMultiLine):
                self.lines.append(node.to_code(0))
            elif isinstance(node, ir.nodes.DictionaryAccess):
                self.lines.append(node.to_code(0))
            elif isinstance(node, ir.nodes.FunctionCall):
                self.lines.append(node.to_code(0))
            elif isinstance(node, ir.nodes.Import):
                self.lines.append(node.to_code(0))
            elif isinstance(node, ir.nodes.ForEachFile):
                self.lines.append(node.to_code(0))
            elif isinstance(node, ir.nodes.Procedure):
                self.lines.append(node.to_code(0))
            elif isinstance(node, ir.nodes.DoUntilStreamEnd):
                self.lines.append(node.to_code(0))
        return "\n".join(self.lines)
