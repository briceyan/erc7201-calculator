# ERC-7201 Slot Calculator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> Note: Most of this project's code was written using [aider](https://aider.chat) with the [DeepSeek](https://deepseek.com) AI model.

A web service that calculates and formats storage slots for [ERC-7201](https://eips.ethereum.org/EIPS/eip-7201) namespaces.

## Features

- Calculate storage slots for any valid namespace
- Get results as:
  - Formatted Solidity code (web interface)
  - Plain text (API response)
- Copy code snippets with one click
- See equivalent cURL and Foundry Cast commands

## Usage

### Web Interface

Visit [erc7201.cc](https://erc7201.cc) and enter a namespace like `example.main` to see the calculated storage slot and formatted Solidity code.

### API

```bash
# Get slot calculation as plain text
curl -L erc7201.cc/example.main

# Using Foundry Cast
cast index-erc7201 example.main
```

### Examples

```bash
# Basic example
curl -L erc7201.cc/example.main

# OpenZeppelin-style namespace
curl -L erc7201.cc/openzeppelin.storage.Ownable
```

## Development

### Prerequisites

- Python 3.10+
- [Poetry](https://python-poetry.org/) (recommended) or pip

### Installation

```bash
git clone https://github.com/briceyan/erc7201-calculator.git
cd erc7201-calculator

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies with uv (recommended)
uv pip install -r requirements.txt

# Or alternatively with pip:
# pip install -r requirements.txt
```

### Running Locally

```bash
flask --app api.index run --debug
```

Then open http://localhost:5000 in your browser.




## Contributing

Pull requests are welcome! Please open an issue first to discuss any major changes.

## License

MIT
