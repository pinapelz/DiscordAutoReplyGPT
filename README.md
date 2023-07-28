# DiscordAutoReply GPT
Respond to Discord messages automatically with the power of LLMs.

## Install Helper Plugin
Requires BetterDiscord to be installed in order to run the helper plugin (Websocket Server).
- Add `Replier.plugin.js` into the BetterDiscord plugins folder

- Click the Cog icon and configure the plugin with your Discord Channel ID

- Input a Channel ID if you want to limit the Reply server to only be able to see messages from a particular channel (i.e You run the websocket server on a different machine and don't want the owner of that machine to see messages outside of a particular channel)

## Edit Config
Configure `config.json` with information regarding where your WebSocket server is running (*Leave the default parameters if you haven't changed anything*)
- `OPENAI_API_KEY` - Add your OpenAI API Key if you want to use GPT-3.5 to respond to messages

    - Leaving this blank will result in the server to use [gpt4free](https://github.com/xtekky/gpt4free) to respond to messages

    - *Note: You can't specify a `CONTEXT_MESSAGE` if you're using [gpt4free](https://github.com/xtekky/gpt4free)*

Supplying Authorization Token will result in messages being sent through a POST request (headless)

- If no Authorization Token is supplied then messages will be sent through recording window position and macros using pyautogui

- You will be prompted to configure the macro area after a connection has been established with the WebSocket server

Configure `reply_config.py` with pairs of User ID and Channel ID conditions that you want to reply to. You can also configure a `CONTEXT_MESSAGE` which can help you specify how you want the AI to respond (OpenAI GPT only).

```bash
pip install -r requirements.txt
python auto_reply.py
```
With your server running, reload the helper plugin by clicking the edit button (pencil icon) and then clicking the save button (floppy disk icon).

> Warning, sending automated messages as a non-bot or using 3rd party plugins may be considered in violation of Discord's TOS
