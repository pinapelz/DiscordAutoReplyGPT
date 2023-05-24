# DiscordAutoReply
Respond to your DMs automatically with large language models.

Requires BetterDiscord to be installed in order to run the helper plugin.
- Set your own UserID to ensure your own messages aren't propagated
- Set a channel id to listen (ideally a DM channel)

You can either choose use the OpenAI GPT-3.5 script or use the [gpt4free](https://github.com/xtekky/gpt4free) alternative (leave OpenAI API key blank)

Supplying Authorization Token will result in messages being sent through a POST request (headless)

If not then messages will be sent through recording window position and macros using pyautogui

Configure `reply_config.py` with pairs of User ID and Channel ID conditions that you want to reply to

```
python auto_reply.py
```
Then reload/load the helper plugin

> Warning, sending automated messages as a non-bot or using 3rd party plugins may be considered in violation of Discord's TOS
