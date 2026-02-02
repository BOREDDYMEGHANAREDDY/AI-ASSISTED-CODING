# Weather Data Fetcher

A Python application that securely fetches weather data from the OpenWeatherMap API using environment variables.

## Features

- Fetches real-time weather data for any city
- Secure API key management using environment variables
- Comprehensive error handling for network and API errors
- User-friendly weather information display
- No hardcoded sensitive information

## Setup Instructions

### 1. Install Required Packages

```bash
pip install requests python-dotenv
```

### 2. Get an API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Generate an API key
4. Copy the API key

### 3. Configure Environment Variables

**Option A: Using .env file (Recommended)**
1. Copy the `.env.example` file to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and replace `your_api_key_here` with your actual API key:
   ```
   OPENWEATHER_API_KEY=abc123def456ghi789
   ```
3. Make sure `.env` is in the same directory as the script

**Option B: Using System Environment Variables**
- Windows PowerShell:
  ```powershell
  $env:OPENWEATHER_API_KEY = 'your_api_key_here'
  ```
- Linux/Mac:
  ```bash
  export OPENWEATHER_API_KEY='your_api_key_here'
  ```

### 4. Run the Application

```bash
python apiusage.py
```

## Usage Example

```
Weather Data Fetcher Application
--------------------------------------------------
Enter city name: London
Fetching weather data for London...

==================================================
Weather Information for London, GB
==================================================
Temperature: 12°C (feels like 10°C)
Humidity: 75%
Pressure: 1013 hPa
Wind Speed: 5.2 m/s
Conditions: Partly cloudy
==================================================
```

## Error Handling

The program handles the following errors gracefully:

- **Missing API Key**: Prompts user to set the environment variable
- **Invalid City Name**: Displays error message for non-existent cities
- **Invalid API Key**: Shows 401 authentication error
- **Network Issues**: Handles connection errors and timeouts
- **JSON Parsing Errors**: Catches malformed API responses
- **Empty User Input**: Validates user input before making API calls

## Security Best Practices

✓ API key is stored in environment variables, not hardcoded
✓ `.env` file is excluded from version control via `.gitignore`
✓ Never commit sensitive information to repositories
✓ Use `.env.example` as a template for developers

## File Structure

```
LAB5.1/
├── apiusage.py          # Main application
├── .env                 # Environment variables (not in version control)
├── .env.example         # Template for environment variables
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Troubleshooting

**"Error: OPENWEATHER_API_KEY environment variable not set"**
- Solution: Create a `.env` file with your API key or set the environment variable

**"Error: City not found"**
- Solution: Check the spelling of the city name and try again

**"Error: Invalid API key"**
- Solution: Verify your API key is correct in the `.env` file

**"Error: Unable to connect to the weather API"**
- Solution: Check your internet connection and try again

## Additional Resources

- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [python-dotenv Documentation](https://python-dotenv.readthedocs.io/)
- [Requests Library Documentation](https://requests.readthedocs.io/)
