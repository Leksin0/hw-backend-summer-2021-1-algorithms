__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    d = seconds // 86400
    h = seconds % 86400 // 3600
    m = seconds % 3600 // 60
    s = seconds % 60
    return ((f"{d:02d}d" if d > 0 else "") + (f"{h:02d}h" if d > 0 or h > 0 else "") +
            (f"{m:02d}m" if d > 0 or h > 0 or m > 0 else "") + f"{s:02d}s")
