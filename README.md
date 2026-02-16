# Twitter Bot

A Python-based Twitter automation bot that uses both Tweepy API and Selenium-based automation to interact with Twitter.

## Project Overview

This project provides two approaches for automating Twitter interactions:

1. **Tweepy API Approach** - Direct API integration using Twitter's official API
2. **Selenium Automation Approach** - Browser-based automation using Selenium WebDriver

## Features

- **Tweet Posting**: Automatically post tweets to your Twitter account
- **API Integration**: Uses Tweepy library for official Twitter API access
- **Browser Automation**: Selenium-based automation for browser interactions
- **Credential Management**: Secure credential handling through configuration files

## Files

- `bot.py` - Main bot implementation using Tweepy API
- `test.py` - Selenium-based automation for browser testing
- `keys.txt` - Configuration file for API credentials (do not commit to version control)
- `.gitignore` - Git configuration to prevent sensitive files from being committed

## Requirements

- Python 3.x
- tweepy
- selenium
- webdriver-manager (for Brave/Chrome automation)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Kendrick80/Twitter-Bot.git
cd Twitter-Bot
```

2. Install required dependencies:
```bash
pip install tweepy selenium webdriver-manager
```

3. Set up your credentials in `keys.txt`:
```
bearer_token=YOUR_BEARER_TOKEN
consumer_key_secret=YOUR_CONSUMER_KEY_SECRET
access_token=YOUR_ACCESS_TOKEN
access_token_secret=YOUR_ACCESS_TOKEN_SECRET
client_secret_id=YOUR_CLIENT_SECRET_ID
client_secret=YOUR_CLIENT_SECRET
```

## Configuration

### Getting Twitter API Credentials

1. Visit [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a new app or use an existing one
3. Generate API keys and access tokens
4. Add your credentials to `keys.txt`

### For Selenium Automation (test.py)

Update the following variables in `test.py`:
- `USERNAME` - Your Twitter username
- `PASSWORD` - Your Twitter password
- `TWEET_TEXT` - The text you want to tweet

## Usage

### Using Tweepy (bot.py)

```bash
python bot.py
```

This will post a tweet using the Tweepy API.

### Using Selenium Automation (test.py)

```bash
python test.py
```

This will automate browser interaction to post a tweet.

## Security Notes

⚠️ **Important**: 
- Never commit `keys.txt` to version control
- The `.gitignore` file is configured to exclude `keys.txt`
- Keep your credentials private and secure
- Do not share your bearer tokens or access tokens

## Browser Support

The Selenium automation (`test.py`) is configured for:
- Brave Browser (default)
- Chrome Browser (can be modified)

Update the `chrome_options.binary_location` path if using a different browser or installation location.

## Troubleshooting

### API Connection Issues
- Verify your credentials in `keys.txt`
- Ensure your API keys have the correct permissions
- Check your Twitter API rate limits

### Selenium Issues
- Ensure Brave/Chrome browser is installed at the specified path
- Verify WebDriver compatibility with your browser version
- Check for Twitter UI changes that may affect element selectors

## Future Enhancements

- Add more automation features (likes, retweets, follows)
- Implement scheduled tweet posting
- Add hashtag and mention tracking
- Create a configuration GUI
- Add error handling and logging

## License

This project is provided as-is for educational and personal use.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## Contact

For questions or issues, please open an issue on GitHub.