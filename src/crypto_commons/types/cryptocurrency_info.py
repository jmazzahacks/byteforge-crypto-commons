from dataclasses import dataclass, field
from typing import List, Optional

from .cryptocurrency_platform import CryptocurrencyPlatform
from .cryptocurrency_urls import CryptocurrencyUrls


@dataclass
class CryptocurrencyInfo:
    """
    Rich token metadata from CMC's /v2/cryptocurrency/info endpoint.
    Complements TokenInfo (which carries the lightweight listing data
    from /v1/cryptocurrency/map) — CryptocurrencyInfo is the heavier
    payload with description, logo, tags, platform, and URLs.

    Required Fields:
        id: CMC ID of the token
        name: Full token name
        symbol: Trading ticker
        slug: URL-friendly token name

    Optional Fields:
        description: Free-form description text (multi-paragraph for
            established tokens). Primary LLM-friendly disambiguator.
        category: 'coin' or 'token'
        logo: URL to CMC-hosted logo image
        date_added: Unix timestamp when CMC first indexed this token
        date_launched: Unix timestamp the team reports as the launch
            date (often null)
        notice: Free-form notice from CMC (deprecation warnings, etc.)
        tags: CMC-assigned category tags (e.g. ['mineable', 'pow'])
        platform: On-chain platform metadata — None for native L1s,
            populated with chain + contract_address for cross-chain
            tokens
        urls: Categorized URL bundle
    """
    id: int
    name: str
    symbol: str
    slug: str
    description: Optional[str] = None
    category: Optional[str] = None
    logo: Optional[str] = None
    date_added: Optional[int] = None
    date_launched: Optional[int] = None
    notice: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    platform: Optional[CryptocurrencyPlatform] = None
    urls: Optional[CryptocurrencyUrls] = None
