
# Configuration for which users in what channels to reply to

"""
Add a tuple to the REPLY_TO list to add a new channel to reply to
You can get these values by right clicking on a channel and clicking "Copy ID" after enabling Developer Mode in Discord

(USER_ID, CHANNEL_ID)

When a message is received from a user matching USER_ID in a channel matching CHANNEL_ID, a response will be sent to that channel
"""

REPLY_TO = [
    ("USER_ID", "CHANNEL_ID"),
    ("USER_ID", "CHANNEL_ID"),
]