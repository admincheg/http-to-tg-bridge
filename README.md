# Simple HTTP to Telegram brige

Simple script, which accepts some JSON data at /fire/<apikey> endpoint and pass
it to specified Telegram groups. It can pass alerts to private chats,
theortically.

## Pre-flight

You should use @botfather bot in the Telegram for obtaining Bot Secret API Key.

Theoretically you can not specify additional permissions for bot.

After that you should add bot to required chats.

## Configuration

Bot can be configured by .env file or by environment variables

    BOT_TELEGRAM_TOKEN - api key obtained from @botfather
    BOT_API_TOKEN - part of URI string, which used for requests authorization
                    (because alertmanager can not use custom headers)
    BOT_GROUP_CHATS - list of chat ids separated by comma

You can rename .env.example file to .env and place your data to it.

## Build

### For local usage

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 main.py

### Docker

    docker build -t http-to-tg-bridge .
    docker run -it --env-file .env -p 5000:5000 http-to-tg-bridge

## Usage

This simple script has two endpoints:

    GET /health - simple livenes check
    POST /fire/<apikey> - endpoint for sending messages to the Telegram chats

## Example

Send simple notification

    curl -X POST -H"Content-Type: application/json" \
      http://127.0.0.1:5000/fire/strageapikey \
      -d '{"data":"information","object":{"ints":[1,2,3]}}'
