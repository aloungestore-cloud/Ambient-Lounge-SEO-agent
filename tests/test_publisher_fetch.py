from __future__ import annotations
import unittest
from unittest.mock import MagicMock
from publisher.fetch import fetch_article


class TestFetch(unittest.TestCase):
    """Test fetch.py article retrieval."""

    def test_fetch_ok(self):
        """Mock http_get returns 200 + valid JSON → returns dict."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "ok": True,
            "title": "Test Article",
            "preview_text": "Preview text",
            "detail_text": "Detail text here",
            "url": "/blog/test-article/",
            "preview_picture_url": "https://img.example.com/preview.jpg",
        }

        mock_http_get = MagicMock(return_value=mock_response)

        result = fetch_article(
            article_url="/blog/test-article/",
            api_url="https://api.example.com/api/catalog.php",
            api_key="test-key-123",
            http_get=mock_http_get,
        )

        self.assertEqual(result["title"], "Test Article")
        self.assertEqual(result["preview_text"], "Preview text")
        self.assertEqual(result["detail_text"], "Detail text here")
        self.assertEqual(result["url"], "/blog/test-article/")
        self.assertEqual(result["preview_picture_url"], "https://img.example.com/preview.jpg")
        self.assertTrue(result["ok"])

    def test_fetch_http_error(self):
        """Mock http_get returns 404 → raises ValueError."""
        mock_response = MagicMock()
        mock_response.status_code = 404

        mock_http_get = MagicMock(return_value=mock_response)

        with self.assertRaises(ValueError):
            fetch_article(
                article_url="/blog/missing/",
                api_url="https://api.example.com/api/catalog.php",
                api_key="test-key-123",
                http_get=mock_http_get,
            )

    def test_fetch_api_error(self):
        """Mock http_get returns 200 + {"ok": false} → raises ValueError."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "ok": False,
            "error": "not found",
        }

        mock_http_get = MagicMock(return_value=mock_response)

        with self.assertRaises(ValueError):
            fetch_article(
                article_url="/blog/missing/",
                api_url="https://api.example.com/api/catalog.php",
                api_key="test-key-123",
                http_get=mock_http_get,
            )


if __name__ == "__main__":
    unittest.main()
