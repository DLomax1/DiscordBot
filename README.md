# Rick and Morty Discord Bot

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Discord.py Version](https://img.shields.io/badge/discord.py-1.7.3-blue)
![License](https://img.shields.io/badge/License-MIT-blue)

## Overview

The Rick and Morty Discord Bot is a bot designed to serve the Rick and Morty fan community by providing information about the series. This bot interacts with the [Rick and Morty API](https://rickandmortyapi.com/) to fetch and display details about locations, episodes, and characters from the show. It enhances the community's experience by making it easy for users to access information about their favorite series.

## Features

- Retrieve detailed information about Rick and Morty locations.
- Access episode details, including name, air date, and episode code.
- Get information about specific Rick and Morty characters, including their name, status, species, and an image.
- Discover random characters, locations, and episodes with the bot's "Rchar," "Rloca," and "Repi" commands.
- Error handling to provide users with helpful responses in case of issues.

## Prerequisites

Before running the bot, make sure you have the following:

- Python 3.8 or higher.
- The `discord.py` library (v1.7.3).
- The `aiohttp` library for asynchronous HTTP requests.
- A valid Discord bot token obtained by [creating a Discord bot](https://discord.com/developers/applications).

## Installation

1. Clone this repository to your local machine using Git:

    ```bash
    git clone https://github.com/your-username/rick-and-morty-discord-bot.git
    ```

2. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project directory and add your Discord bot token:

    ```env
    DISCORD_TOKEN=your-bot-token-here
    ```

4. Run the bot using Python:

    ```bash
    python bot.py
    ```

## Usage

- Invite the bot to your Discord server by [creating a Discord bot invite link](https://discord.com/developers/applications).
- Use the bot's commands by typing `![command]` in your server's text channels. For example, `!location 1` retrieves information about location 1 from Rick and Morty.

## Commands

- `!location [location_id]` - Retrieve information about a location.
- `!episode [episode_id]` - Get details about an episode.
- `!character [character_id]` - Access information about a character.
- `!Rchar` - Get details about a random character.
- `!Rloca` - Get details about a random location.
- `!Repi` - Get details about a random episode.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- Thanks to the [Rick and Morty API](https://rickandmortyapi.com/) for providing the data for this bot.

