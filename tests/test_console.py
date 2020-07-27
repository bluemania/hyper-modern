# tests/test_console.py
import click.testing
import pytest
import requests

from hyper_modern import console, example_module


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.mark.e2e
def test_main_succeeds(runner, mock_requests_get):
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_hello():
    example_module.hello()


def test_main_prints_message_on_request_error(runner, mock_requests_get):
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


@pytest.fixture
def mock_wikipedia_random_page(mocker):
    return mocker.patch("hyper_modern.wikipedia.random_page")


def test_main_uses_specified_language(runner, mock_wikipedia_random_page):
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")
