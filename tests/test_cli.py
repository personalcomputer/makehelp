from click.testing import CliRunner

from makehelp.main import cli


def test_cli_help():
    result = CliRunner().invoke(cli, ["--help"])
    assert result.exit_code == 0