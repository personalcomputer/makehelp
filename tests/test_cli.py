import io
import os
import tempfile
import unittest
from unittest.mock import patch

from makehlp.main import main


class TestCLI(unittest.TestCase):
    def test_cli_help(self):
        with patch("sys.stdout", new=io.StringIO()) as fake_out:
            with patch("sys.argv", ["makehlp", "--help"]):
                try:
                    main()
                except SystemExit as e:
                    self.assertEqual(e.code, 0)

            self.assertIn("usage:", fake_out.getvalue().lower())

    def test_specific_target(self):
        # Create a temporary Makefile for testing
        makefile_content = """
.PHONY: test
test: # Test target
\techo "Running tests"
"""
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
            tmp.write(makefile_content)
            makefile_path = tmp.name

        try:
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                with patch("sys.argv", ["makehlp", "--file", makefile_path, "test"]):
                    main()

                output = fake_out.getvalue()
                self.assertIn("Test target", output)
                self.assertIn('echo "Running tests"', output)
        finally:
            os.unlink(makefile_path)

    def test_list_targets(self):
        # Create a temporary Makefile for testing
        makefile_content = """
.PHONY: test build
test: # Run tests
\techo "Running tests"

build: # Build the project
\techo "Building project"
"""
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
            tmp.write(makefile_content)
            makefile_path = tmp.name

        try:
            with patch("sys.stdout", new=io.StringIO()) as fake_out:
                with patch("sys.argv", ["makehlp", "--file", makefile_path]):
                    main()

                output = fake_out.getvalue()
                self.assertIn("test", output)
                self.assertIn("build", output)
                self.assertIn("Run tests", output)
                self.assertIn("Build the project", output)
        finally:
            os.unlink(makefile_path)
