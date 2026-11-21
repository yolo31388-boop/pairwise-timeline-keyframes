import pytest
import math
from media import timeline_keyframes as mod

CASES = [
    ("bez", 'm.bezier(0, 0, 1, 1, 0.5) == approx(0.5)'),
    ("remap", 'm.remap_time(10, 2) == approx(5.0)'),
    ("nested", 'm.nested_time(10, 5, 0) == 15'),
    ("audio", 'm.audio_position(2, 3) == approx(6.0)'),
    ("frame", 'm.frame_to_time(25, 25) == approx(1.0)'),
    ("trim", 'm.trim_offset(10, 2) == 8'),
    ("undo", 'm.undo_handles(1, [0.2, 0.8]) == (1, [0.2, 0.8])'),
    ("cache", "m.cache_key('abc') == 'abc'"),
    ("snap", 'm.snap_time(1.24, 0.5) == approx(1.0)'),
    ("sub", 'm.subframe_sample(1, 2, 0.5) == approx(1.5)'),
    ("count", 'm.key_count([1, 2]) == 2'),
    ("clamp", 'm.clamp_handles(1.5, 0, 1) == 1.0'),
    ("mono", 'm.is_monotonic([1, 2, 3]) is True'),
    ("id", 'm.timeline_id(3, 2) == "3:2"'),
    ("dur", 'm.clip_duration(2, 10) == 8')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
