from __future__ import annotations

import numpy as np


def prefix_survival(confidence: np.ndarray) -> np.ndarray:
    """Return cumulative prefix survival probabilities for one request."""
    confidence = np.asarray(confidence, dtype=float)
    if confidence.ndim != 1:
        raise ValueError("confidence must be a 1D array")
    if np.any((confidence < 0) | (confidence > 1)):
        raise ValueError("confidence values must lie in [0, 1]")
    return np.cumprod(confidence)


def throughput(expected_accepts: float, batch_size: int, sps_table: dict[int, float]) -> float:
    """Expected token throughput: accepted tokens times steps per second."""
    if batch_size in sps_table:
        sps = sps_table[batch_size]
    else:
        keys = np.array(sorted(sps_table))
        vals = np.array([sps_table[int(k)] for k in keys])
        sps = float(np.interp(batch_size, keys, vals))
    return float(expected_accepts * sps)


def schedule_prefixes(confidences: list[np.ndarray], sps_table: dict[int, float]) -> tuple[list[int], float]:
    """Greedy hardware-aware prefix scheduler inspired by DSpark Algorithm 1.

    Parameters
    ----------
    confidences:
        One confidence vector per active request.
    sps_table:
        Engine steps-per-second table keyed by verification batch size.

    Returns
    -------
    selected_lengths, best_throughput
    """
    R = len(confidences)
    survival = [prefix_survival(c) for c in confidences]
    candidates = []
    for r, a in enumerate(survival):
        for j, val in enumerate(a, start=1):
            candidates.append((float(val), r, j))
    candidates.sort(reverse=True)

    lengths = [0] * R
    best_lengths = lengths.copy()
    batch_size = R
    expected_accepts = float(R)
    best = throughput(expected_accepts, batch_size, sps_table)

    for val, r, j in candidates:
        if j <= lengths[r]:
            continue
        if j != lengths[r] + 1:
            continue
        lengths[r] = j
        batch_size += 1
        expected_accepts += val
        current = throughput(expected_accepts, batch_size, sps_table)
        if current > best:
            best = current
            best_lengths = lengths.copy()
        else:
            break
    return best_lengths, best
