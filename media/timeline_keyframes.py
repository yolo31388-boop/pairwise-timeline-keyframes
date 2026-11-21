import math

def bezier(p0, p1, p2, p3, t):
    """贝塞尔求值。"""
    raise NotImplementedError("TODO: bezier")

def remap_time(t, speed):
    """时间重映射。"""
    raise NotImplementedError("TODO: remap_time")

def nested_time(parent, child, offset):
    """嵌套时间。"""
    raise NotImplementedError("TODO: nested_time")

def audio_position(t, speed):
    """音频位置。"""
    raise NotImplementedError("TODO: audio_position")

def frame_to_time(frame, fps):
    """帧转时间。"""
    raise NotImplementedError("TODO: frame_to_time")

def trim_offset(key_time, trim_start):
    """裁剪偏移。"""
    raise NotImplementedError("TODO: trim_offset")

def undo_handles(value, handles):
    """撤销控制柄。"""
    raise NotImplementedError("TODO: undo_handles")

def cache_key(content_hash):
    """缓存键。"""
    raise NotImplementedError("TODO: cache_key")

def snap_time(t, quantum):
    """时间吸附。"""
    raise NotImplementedError("TODO: snap_time")

def subframe_sample(a, b, t):
    """子帧采样。"""
    raise NotImplementedError("TODO: subframe_sample")

def key_count(keys):
    """关键帧数量。"""
    raise NotImplementedError("TODO: key_count")

def clamp_handles(value, low, high):
    """控制柄钳制。"""
    raise NotImplementedError("TODO: clamp_handles")

def is_monotonic(values):
    """单调性。"""
    raise NotImplementedError("TODO: is_monotonic")

def timeline_id(seed, index):
    """时间线 id。"""
    raise NotImplementedError("TODO: timeline_id")

def clip_duration(start, end):
    """片段时长。"""
    raise NotImplementedError("TODO: clip_duration")
