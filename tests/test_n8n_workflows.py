from __future__ import annotations
import json
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_receive_json_valid():
    with open(os.path.join(REPO, "n8n", "al-tg-receive.json"), encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict)

def test_receive_has_webhook_node():
    with open(os.path.join(REPO, "n8n", "al-tg-receive.json"), encoding="utf-8") as f:
        data = json.load(f)
    types = [n.get("type") for n in data.get("nodes", [])]
    assert "n8n-nodes-base.webhook" in types

def test_callback_json_valid():
    with open(os.path.join(REPO, "n8n", "al-tg-callback.json"), encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict)

def test_callback_has_if_node():
    with open(os.path.join(REPO, "n8n", "al-tg-callback.json"), encoding="utf-8") as f:
        data = json.load(f)
    types = [n.get("type") for n in data.get("nodes", [])]
    assert "n8n-nodes-base.if" in types
