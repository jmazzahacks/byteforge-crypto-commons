"""
Smoke tests for the crypto_commons data models.

The models are pure dataclasses with no logic, so these tests verify the
things that can still silently break: that every model imports and constructs
with its required fields, that collection fields use isolated mutable defaults,
that optional fields default as documented, and that the unix-timestamp
convention (no `datetime` in stored fields) holds.
"""
from dataclasses import fields, MISSING
from typing import List

from crypto_commons.types.token_info import TokenInfo
from crypto_commons.types.token_state import TokenState
from crypto_commons.types.quote import Quote
from crypto_commons.types.cryptocurrency_info import CryptocurrencyInfo
from crypto_commons.types.cryptocurrency_platform import CryptocurrencyPlatform
from crypto_commons.types.cryptocurrency_urls import CryptocurrencyUrls


def _make_quote() -> Quote:
    return Quote(
        base_currency="USD",
        price=50000.0,
        volume_24h=1_000_000_000.0,
        percent_change_1h=1.5,
        percent_change_24h=5.0,
        percent_change_7d=10.0,
        percent_change_30d=20.0,
        market_cap=1_000_000_000_000.0,
        last_updated=1_717_000_000,
    )


ALL_MODELS = [
    TokenInfo,
    TokenState,
    Quote,
    CryptocurrencyInfo,
    CryptocurrencyPlatform,
    CryptocurrencyUrls,
]


def test_construct_token_info() -> None:
    info = TokenInfo(id=1, rank=1, name="Bitcoin", symbol="BTC", slug="bitcoin", status=1)
    assert info.id == 1
    assert info.platform is None
    assert info.first_historical_data is None


def test_construct_quote() -> None:
    quote = _make_quote()
    assert quote.base_currency == "USD"
    assert quote.cex_volume_24h is None


def test_construct_token_state() -> None:
    state = TokenState(
        id=1,
        name="Bitcoin",
        symbol="BTC",
        timestamp=1_717_000_000,
        quote_map={"USD": _make_quote()},
    )
    assert state.quote_map["USD"].price == 50000.0
    assert state.tags is None


def test_construct_cryptocurrency_info() -> None:
    info = CryptocurrencyInfo(id=1, name="Bitcoin", symbol="BTC", slug="bitcoin")
    assert info.platform is None
    assert info.urls is None
    assert info.tags == []


def test_construct_cryptocurrency_platform() -> None:
    platform = CryptocurrencyPlatform(
        id=1027,
        name="Ethereum",
        symbol="ETH",
        slug="ethereum",
        token_address="0xabc",
    )
    assert platform.token_address == "0xabc"


def test_cryptocurrency_urls_defaults_empty() -> None:
    urls = CryptocurrencyUrls()
    assert urls.website == []
    assert urls.twitter == []


def test_cryptocurrency_urls_mutable_default_is_isolated() -> None:
    first = CryptocurrencyUrls()
    first.website.append("https://example.com")
    second = CryptocurrencyUrls()
    assert second.website == []


def test_cryptocurrency_info_list_default_is_isolated() -> None:
    first = CryptocurrencyInfo(id=1, name="A", symbol="A", slug="a")
    first.tags.append("mineable")
    second = CryptocurrencyInfo(id=2, name="B", symbol="B", slug="b")
    assert second.tags == []


def test_no_datetime_in_any_model_field() -> None:
    """Convention: all date/time storage is unix-timestamp ints, never datetime."""
    for model in ALL_MODELS:
        for f in fields(model):
            assert "datetime" not in str(f.type).lower(), (
                f"{model.__name__}.{f.name} is annotated with datetime; "
                f"use a unix-timestamp int instead"
            )


def test_collection_fields_use_default_factory() -> None:
    """List/dict fields must use default_factory, never a shared mutable default."""
    for model in ALL_MODELS:
        for f in fields(model):
            type_str = str(f.type)
            is_collection = "List[" in type_str or "Dict[" in type_str
            if is_collection and f.default is not MISSING:
                assert not isinstance(f.default, (list, dict)), (
                    f"{model.__name__}.{f.name} has a mutable default; "
                    f"use field(default_factory=...)"
                )
