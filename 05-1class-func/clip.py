"""
    >>> clip('banana ', 6)
    'banana'
    >>> clip('banana ', 7)
    'banana'
    >>> clip('banana ', 5)
    'banana'
    >>> clip('banana split', 6)
    'banana'
    >>> clip('banana split', 7)
    'banana'
    >>> clip('banana split', 10)
    'banana'
    >>> clip('banana split', 11)
    'banana'
    >>> clip('banana split', 12)
    'banana split'
"""

# BEGIN CLIP

def clip(text, max_len=80):
    """Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        # 0부터 80까지 공백을 찾아라
        space_before = text.rfind(' ', 0, max_len) # 시작점
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len) # 마지막
            if space_after >= 0:
                end = space_after
    if end is None:  # no spaces were found
        end = len(text)
    return text[:end].rstrip()

# END CLIP
