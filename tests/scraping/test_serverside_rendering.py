"""Test the serverside rendering package."""

from palabox.scraping.serverside_rendering import scrap_one_website


def test_scrap_one_website() -> None:
    """Test scrap_one_website."""
    result = scrap_one_website()
    assert isinstance(result, str)
    assert result == ""
