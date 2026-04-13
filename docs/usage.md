# Usage

## Installation

Use the workspace dependencies defined in `pyproject.toml` and install with
`uv` or your preferred Python environment manager.

## Conversion helpers

Convert between `pyglm` and Slang math types with `glm_slang.conversion`.

```python
from pyglm import glm
from glm_slang.conversion import to_slang, from_slang

v = glm.vec3(1.0, 2.0, 3.0)
v_slang = to_slang(v)
v_roundtrip = from_slang(v_slang)
```

## Quaternion utilities

The Slang module provides quaternion math helpers under `glm.quat`.

```slang
import glm;

glm.quat.quat q = glm.quat.fromAxisAngle(float3(0, 1, 0) * radians(90));
float3 rotated = glm.quat.rotate(q, float3(1, 0, 0));
```
