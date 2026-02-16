import unittest # unittesting
import sys # import sys()
from io import StringIO #

class TestHelloWorld(unittest.TestCase):
    def testExample(self):
        """Test that test.py prints 'HELLO WORLD'"""
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Execute the test.py code
        # python3 -c "exec(open('test.py').read())"
        exec(open('test.py').read())
        
        # Reset stdout
        sys.stdout = sys._stdout_
        
        # Check the output
        self.assertEqual(captured_output.getvalue().strip(), "HELLO WORLD")


if __name__ == '__main__':
    unittest.__main__()
