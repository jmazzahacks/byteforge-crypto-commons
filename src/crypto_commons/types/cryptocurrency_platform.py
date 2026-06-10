from dataclasses import dataclass


@dataclass
class CryptocurrencyPlatform:
    """
    The on-chain platform a token is deployed on. None on TokenInfo /
    CryptocurrencyInfo for native L1 coins (BTC, ETH itself, etc.).
    Populated for ERC-20s, SPL tokens, BEP-20s, etc.

    token_address is the canonical on-chain disambiguator when a ticker
    is shared between unrelated assets (e.g. multiple ERC-20s with
    overlapping symbols, or a famous L1 ticker reused on-chain).

    Required Fields:
        id: CMC ID of the host chain
        name: Human-readable chain name (e.g. "Ethereum")
        symbol: Chain native ticker (e.g. "ETH")
        slug: URL-friendly chain name (e.g. "ethereum")
        token_address: The on-chain contract address for this token
    """
    id: int
    name: str
    symbol: str
    slug: str
    token_address: str
