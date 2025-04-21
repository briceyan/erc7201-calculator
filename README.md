# ERC-7201 Slot Calculator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

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

# With Poetry:
poetry install

# With pip:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Running Locally

```bash
flask run
```

Then open http://localhost:5000 in your browser.

## Technical Details

The calculation follows the ERC-7201 specification:
1. Compute `keccak256(namespace) - 1`
2. Compute `keccak256` of that result
3. Mask off the last byte (`& ~0xff`)

See the implementation in [utils/erc7201.py](utils/erc7201.py).

## Contributing

Pull requests are welcome! Please open an issue first to discuss any major changes.

## License

MIT
