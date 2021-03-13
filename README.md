# forsen-discord-bot
Discord bot that tells you wether forsen is live or not, OMEGALUL.

## Installation
You'll need to make your own discord application (and bot), as well as an Twitch application. See
https://discord.com/developers/docs/intro and https://dev.twitch.tv/docs/ for documentation and how
to make applications and bots. 

When this is done, you'll have to make a file that contains the environment variables, namely
DISCORD_TOKEN, CLIENT_ID and CLIENT_SECRET, which you can find in the developer portals for discord
and twitch. Call this file .env and place it in the same folder as the python files. You want this
syntax inside the .env file (without curly brackets):

DISCORD_TOKEN={your discord token}
CLIENT_ID={your twitch app id}
CLIENT_SECRET={your twitch app secret}

In your terminal run:
<pre>
pip3 install -r requirements.txt
</pre>

You will also need to install ffmpeg and add to path. See https://www.ffmpeg.org/
For macOS use brew:
<pre>
brew install ffmpeg
</pre>

For debian based use apt:
<pre>
sudo apt install ffmpeg
</pre>

For windows you'll have to download from the site linked to, paste it to your C: drive and add to PATH.

You'll need to add the bot to your discord server before use.
At last, run
<pre>
python3 bot.py
</pre>

## Commands
As per now, there are only two commands. The prefix is "=". 
- =forsen: if you are in a voice channel, the bot will join this channel and tell you wether forsen is
live or not. Else, it will tell you in the chat channel.
- =forsenquote: gives you a random forsen quote.

