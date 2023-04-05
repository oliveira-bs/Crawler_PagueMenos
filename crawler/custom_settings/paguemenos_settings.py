from typing import Any


def settings(concurrent_requests: int = 32,
             concurrent_requests_per_ip: int = 32,
             download_delay: float = 0.514,
             feed_export_encoding: str = 'utf-8',
             randomize_download_delay: bool = True,
             redirect_enabled: bool = True, retry_enabled: bool = False,
             robotstxt_obey: bool = False, user_agent: str = 'Mozilla/5.0 \
(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/107.0.0.0 Safari/537.36',
             retry_times: int = 0) -> dict[str, Any]:
    """Configure some parameters considered important to run the crawler \
    project."""

    setup_defaults = {
        'CONCURRENT_REQUESTS': concurrent_requests,
        'CONCURRENT_REQUESTS_PER_IP': concurrent_requests_per_ip,
        'DOWNLOAD_DELAY': download_delay,
        'FEED_EXPORT_ENCODING': feed_export_encoding,
        'RANDOMIZE_DOWNLOAD_DELAY': randomize_download_delay,
        'REDIRECT_ENABLED': redirect_enabled,
        'RETRY_ENABLED': retry_enabled,
        'ROBOTSTXT_OBEY': robotstxt_obey,
        'USER_AGENT': user_agent,
        'RETRY_TIMES': retry_times,
    }
    return setup_defaults
