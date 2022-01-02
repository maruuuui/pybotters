from typing import Callable
import time


def _bitbank_nonce() -> Callable[[], str]:
    prev = 0

    def nonce() -> str:
        nonlocal prev
        n = int(time.time())
        if n <= prev:
            prev += 1
            return str(prev)

        prev = n
        return str(prev)

    return nonce


bitbank_nonce = _bitbank_nonce()
