# Secure Password Generator

A modern web application that generates secure passwords with customizable options.

## Features

- Configurable password length (8-64 characters)
- Include/exclude uppercase letters
- Include/exclude lowercase letters
- Include/exclude numbers
- Include/exclude symbols
- Option to exclude similar characters (1, l, I, 0, O)
- Copy to clipboard functionality
- Secure password generation using Python's `secrets` module

## Installation

1. Clone this repository
2. Install the requirements:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Run the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to the specified URL at startup.

## Security Features

- Uses Python's `secrets` module for cryptographically strong random number generation
- Ensures at least one character from each selected type (if enabled)
- Randomizes character positions to prevent predictable patterns
- No password storage - generated passwords exist only in memory temporarily
