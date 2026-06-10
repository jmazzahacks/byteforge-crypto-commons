# ByteForge Crypto Commons

A Python library providing common models and utilities for cryptocurrency projects. This library serves as a foundation for building cryptocurrency-related applications by providing standardized data models and types.

## Features

- **Standardized Data Models**: Well-defined Python dataclasses for representing cryptocurrency data
- **Type Safety**: Full type hints and documentation for all models
- **Comprehensive Market Data**: Support for various market metrics and statistics
- **Flexible Design**: Optional fields for extended data while maintaining core required fields

## Installation

```bash
pip install byteforge-crypto-commons
```

## Usage

### Token State

The `TokenState` class represents the complete state of a cryptocurrency token at a specific moment in time:

```python
from crypto_commons.types.token_state import TokenState
from crypto_commons.types.quote import Quote
import datetime

# Dates/times are stored as unix-timestamp ints (seconds since the epoch)
now_ts = int(datetime.datetime.now().timestamp())

# Create a quote for USD
quote = Quote(
    base_currency="USD",
    price=50000.0,
    volume_24h=1000000000.0,
    percent_change_1h=1.5,
    percent_change_24h=5.0,
    percent_change_7d=10.0,
    percent_change_30d=20.0,
    market_cap=1000000000000.0,
    last_updated=now_ts
)

# Create a token state
token_state = TokenState(
    id=1,
    name="Bitcoin",
    symbol="BTC",
    timestamp=now_ts,
    quote_map={"USD": quote}
)
```

### Quote

The `Quote` class represents market data for a cryptocurrency in a specific currency:

```python
from crypto_commons.types.quote import Quote
import datetime

quote = Quote(
    base_currency="USD",
    price=50000.0,
    volume_24h=1000000000.0,
    percent_change_1h=1.5,
    percent_change_24h=5.0,
    percent_change_7d=10.0,
    percent_change_30d=20.0,
    market_cap=1000000000000.0,
    last_updated=int(datetime.datetime.now().timestamp())  # unix timestamp
)
```

### TokenInfo

The `TokenInfo` class represents basic information about a cryptocurrency token:

```python
from crypto_commons.types.token_info import TokenInfo
import datetime

token_info = TokenInfo(
    id=1,
    rank=1,
    name="Bitcoin",
    symbol="BTC",
    slug="bitcoin",
    status=1,
    is_active=1,
    first_historical_data=int(datetime.datetime(2010, 7, 17).timestamp()),  # unix timestamp
    last_historical_data=int(datetime.datetime.now().timestamp()),  # unix timestamp
    platform=None
)
```

## Data Models

### TokenState

Represents the complete state of a cryptocurrency token, including:
- Basic information (id, name, symbol)
- Market data through Quote objects
- Supply metrics (circulating, total, max supply)
- Status indicators (is_active, is_fiat)
- Additional metadata (tags, platform, creation date)

### TokenInfo

Represents basic information about a cryptocurrency token, including:
- Core identifiers (id, name, symbol, slug)
- Market rank and status
- Historical data availability
- Platform information (for tokens on other blockchains)
- Active status indicator

### Quote

Represents market data for a cryptocurrency in a specific currency, including:
- Price and volume data
- Market capitalization
- Percentage changes over various time periods
- Supply metrics
- Additional market statistics

### CryptocurrencyInfo

Rich token metadata (the heavier payload from a cryptocurrency `info` endpoint),
complementing the lightweight `TokenInfo`. Includes description, logo, tags,
`date_added` / `date_launched` (unix timestamps), and two nested models:
- **CryptocurrencyPlatform** — the on-chain platform a token is deployed on
  (chain identifiers plus the token's contract address); `None` for native L1s
- **CryptocurrencyUrls** — categorized URL bundle (website, explorer, source
  code, social, etc.)

## Requirements

- Python 3.8 or higher
- No third-party dependencies (stdlib only)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

- Jason Byteforge

## Project Links

- [GitHub Repository](https://github.com/jmazzahacks/byteforge-crypto-commons)
- [Issue Tracker](https://github.com/jmazzahacks/byteforge-crypto-commons/issues) 