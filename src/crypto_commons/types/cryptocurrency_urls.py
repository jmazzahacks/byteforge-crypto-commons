from dataclasses import dataclass, field
from typing import List


@dataclass
class CryptocurrencyUrls:
    """
    Categorized URLs CMC tracks for a token. All fields default to an
    empty list — most tokens populate only a subset.

    Optional Fields:
        website: Official project websites
        technical_doc: Whitepaper / technical doc URLs
        explorer: Block explorer links
        source_code: Source code repos (GitHub etc.)
        message_board: Forum URLs
        chat: Discord / Telegram / etc.
        announcement: Announcement channels
        reddit: Subreddit URLs
        twitter: Twitter / X profile URLs
        facebook: Facebook page URLs
    """
    website: List[str] = field(default_factory=list)
    technical_doc: List[str] = field(default_factory=list)
    explorer: List[str] = field(default_factory=list)
    source_code: List[str] = field(default_factory=list)
    message_board: List[str] = field(default_factory=list)
    chat: List[str] = field(default_factory=list)
    announcement: List[str] = field(default_factory=list)
    reddit: List[str] = field(default_factory=list)
    twitter: List[str] = field(default_factory=list)
    facebook: List[str] = field(default_factory=list)
