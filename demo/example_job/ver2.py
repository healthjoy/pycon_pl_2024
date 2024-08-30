from random import randint

from .constants import CANDIDATES_COUNT, MAX_N


def get_eligible_candidates() -> list[int]:
    """Generate the list of identities to be used as eligible candidates"""
    return [randint(0, MAX_N * 2) for _ in range(CANDIDATES_COUNT)]


def get_eligible_ids_count(ids: list[int]) -> int:
    """Filter identities and calculate the matched eligible identities count"""
    candidates = get_eligible_candidates()
    matched_ids = [id_ for id_ in ids if id_ in candidates]
    return len(matched_ids)
