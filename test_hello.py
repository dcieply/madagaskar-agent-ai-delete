import io
import unittest
from contextlib import redirect_stdout

import hello


class TestHello(unittest.TestCase):
    def test_greet_returns_greeting(self):
        self.assertEqual(hello.greet(), "Witaj z Madagaskaru!")

    def test_main_prints_greeting(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            hello.main()
        self.assertEqual(buffer.getvalue(), "Witaj z Madagaskaru!\n")


if __name__ == "__main__":
    unittest.main()
