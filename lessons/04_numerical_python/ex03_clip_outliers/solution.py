"""Exercise solution.

You should only edit this file.
"""

from __future__ import annotations


def clip_outliers(
    x: list[float],
    low_pct: float = 5.0,
    high_pct: float = 95.0,
) -> list[float]:
    """Return a percentile-clipped copy of x.

    - low_pct and high_pct are in [0, 100] with low_pct <= high_pct.
    - Values strictly below the low_pct percentile are replaced with
      the low_pct percentile value; same for high.
    - Use numpy and boolean masking (np.where); no Python loops.
    - If x is empty or low_pct > high_pct, raise ValueError.
    """
    raise NotImplementedError
