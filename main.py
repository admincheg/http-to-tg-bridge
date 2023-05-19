#!/usr/bin/env python3

import os
import telegram
from flask import Flask, json, request
from werkzeug.exceptions import BadRequest
from dotenv import load_dotenv

load_dotenv()

_api_tokens = [ os.getenv("BOT_API_TOKEN","IdiNahooooi") ]
_api = Flask(__name__)
_bot_token = os.getenv("BOT_TELEGRAM_TOKEN")
_bot = telegram.Bot(token=_bot_token)
_bot_groupids = os.getenv("BOT_GROUP_CHATS").split(",")

@_api.route('/fire/<apikey>', methods=['POST'])
def fire(apikey):
    if apikey in _api_tokens:
        if request.is_json:
            try:
                for group in _bot_groupids:
                    _bot.send_message(group, text=request.get_json())
                return "{}", 200
            except BadRequest:
                return '{"error":"malformed data, check your json"}', 400
        return '{"error":"Data should be json-formatted"}', 415
    return '{"error":"access deined"}', 403

@_api.route('/health', methods=['GET'])
def health():
    return '', 200

if __name__ == '__main__':
    _api.run(host="0.0.0.0")
