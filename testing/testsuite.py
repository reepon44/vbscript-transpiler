import subprocess
import unittest
import os

class TestFunctionResults(unittest.TestCase):

    def test_mid(self):
        test_values = ["Test", "ÄäÖöÜü", "#+-_.,;:%&$", "1234567890", "Zeile\nZeile", "Lorem Ipsum"]
        # Normal Testcase
        for value in test_values:
            with self.subTest(input=value):
                self.assertEqual(run_vbscript(f'Wscript.Echo Mid("{value}", 1)', "mid"), mid(value, 1))
        with self.subTest():
            # Length longer than string
            self.assertEqual(run_vbscript('Wscript.Echo Mid("Test", 1, 8)', "mid"), mid("Test", 1, 8))
            # No length specified
            self.assertEqual(run_vbscript('Wscript.Echo Mid("Test", 1)', "mid"), mid("Test", 1))
            # Numbers as input instead of strings
            self.assertEqual(run_vbscript('Wscript.Echo Mid(1, 1)', "mid"), mid(1, 1))
            # Negative startindex
            # Result: VBScript throws exceptio, Python runs
            # There is no way to catch the exception through cscript in VBS - disabling test case
            self.assertEqual(run_vbscript('Wscript.Echo Mid("Test", -1, 5)', "mid"), mid("Test", -1, 5))


    def test_trim(self):
        self.assertEqual(run_vbscript('Wscript.Echo trim("Test")', 'trim'), trim("Test"))
    
    def test_split(self):
        self.assertEqual(run_vbscript('Wscript.Echo split("test;string", ";")', "split"), split("test;string", ";"))

def run_vbscript(vbs_code: str, name: str) -> str:
    """Führt VBScript-Code aus und gibt die Ausgabe zurück."""
    script_dir = os.path.dirname(__file__)
    temp_path  = "\\skripte\\"
    with open(f"{script_dir+temp_path}{name}.vbs", mode='w', encoding='utf-8') as temp_file:
        temp_file.write(vbs_code)

    #with open("C:\\Bachelorarbeit\\testing\\skripte\\mid.vbs", 'r', encoding='utf-8') as script_file:
    result = subprocess.check_output(["cscript.exe", "//NoLogo", f"{script_dir+temp_path}{name}.vbs"], stderr=subprocess.STDOUT, text=True)
    return result

def mid(string: str, start, length=None):
    # "\n" is just because of Wscript.echo
    # will be absent in later implementation
    if not isinstance(string, str):
       string = str(string)
    if not length:
        return (string[start-1:]+"\n")
    return (string[start-1:(start+length-1)]+"\n")

def trim(string: str) -> str:
    return (string.strip()+"\n")

def split(string: str, sep):
    return string.split(sep)

if __name__ == "__main__":
    unittest.main()
