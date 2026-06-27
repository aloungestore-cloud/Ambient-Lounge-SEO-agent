from __future__ import annotations
import unittest
from unittest.mock import MagicMock
from publisher.generate import generate_post


class TestGenerate(unittest.TestCase):
    """Test generate.py post generation from article."""

    def test_generate_returns_string(self):
        """Mock claude_client.messages.create with text response → returns string."""
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="тест пост")]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_response

        article = {
            "title": "Заголовок статьи",
            "preview_text": "Краткое описание",
        }

        result = generate_post(article, mock_client)

        self.assertEqual(result, "тест пост")
        self.assertIsInstance(result, str)

    def test_generate_empty_raises(self):
        """Mock claude_client.messages.create with empty text → raises ValueError."""
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="")]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_response

        article = {
            "title": "Заголовок статьи",
            "preview_text": "Краткое описание",
        }

        with self.assertRaises(ValueError) as context:
            generate_post(article, mock_client)

        self.assertIn("empty response from Claude", str(context.exception))

    def test_generate_uses_title(self):
        """Article title should appear in the prompt sent to Claude."""
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="генерированный пост")]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_response

        article = {
            "title": "МОЙ ЗАГОЛОВОК",
            "preview_text": "Описание статьи",
        }

        result = generate_post(article, mock_client)

        # Verify the call was made
        mock_client.messages.create.assert_called_once()

        # Extract the call arguments (both positional and keyword)
        call_args, call_kwargs = mock_client.messages.create.call_args
        messages = call_kwargs.get("messages", [])

        # The prompt should be in the messages
        # messages is a list like [{"role": "user", "content": "..."}]
        prompt_text = ""
        if isinstance(messages, list) and len(messages) > 0:
            msg = messages[0]
            if isinstance(msg, dict):
                prompt_text = msg.get("content", "")

        self.assertIn("МОЙ ЗАГОЛОВОК", prompt_text, "Title should be in the prompt")


if __name__ == "__main__":
    unittest.main()
