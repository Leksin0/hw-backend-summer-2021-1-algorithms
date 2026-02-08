from typing import TypeVar
from collections import defaultdict

__all__ = (
    "flip_kv_vk",
    "flip_kv_vk_safe",
)


KT = TypeVar("KT")
KV = TypeVar("KV")


def flip_kv_vk(d: dict[KT, KV]) -> dict[KV, KT]:
    flipped = {val: key for key, val in d.items()}
    return flipped


def flip_kv_vk_safe(d: dict[KT, KV]) -> dict[KV, list[KT]]:
    flipped = defaultdict(list)
    for key, val in d.items():
        flipped[val].append(key)
    return dict(flipped)
