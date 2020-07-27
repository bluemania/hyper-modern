# tests/test_console.py
from unittest.mock import Mock

import pytest
import requests
from click.testing import CliRunner
from pytest_mock import MockFixture

from hyper_modern import console, example_module


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.mark.e2e
def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock) -> None:
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_hello() -> None:
    example_module.hello()


def test_main_prints_message_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(console.main)
    assert "Error" in result.output


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    return mocker.patch("hyper_modern.wikipedia.random_page")


def test_main_uses_specified_language(
    runner: CliRunner, mock_wikipedia_random_page: Mock
) -> None:
    runner.invoke(console.main, ["--language=pl"])
    mock_wikipedia_random_page.assert_called_with(language="pl")
