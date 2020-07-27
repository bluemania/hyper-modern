# tests/test_wikipedia.py
from unittest.mock import Mock

from hyper_modern import wikipedia


def test_random_page_uses_given_language(mock_requests_get: Mock) -> None:
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]


def test_random_page_returns_page(mock_requests_get: Mock) -> None:
    page = wikipedia.random_page()
    assert isinstance(page, wikipedia.Page)
