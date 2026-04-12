import logging

from pyglm import glm
from spm_slang.package_manager import SlangPackageManager

from glm_slang.conversion import from_slang, to_slang
from . import GlmSlangTest

from .common import (
    _assert_mat2_close,
    _assert_mat3_close,
    _assert_mat4_close,
    _assert_quat_close,
    _assert_vec2_close,
    _assert_vec3_close,
    _assert_vec4_close,
)

logger = logging.getLogger(__name__)

package_manager = SlangPackageManager()
test_module = package_manager.module_map[GlmSlangTest.name()]


def test_float2():
    v_py = glm.vec2(1.0, -2.0)
    logger.info(f"Created float2 in glm: {v_py}")
    v_slang = test_module.test_float2(to_slang(v_py))
    logger.info(f"Received float2 from Slang: {v_slang}")
    v_py_converted = from_slang(v_slang)
    _assert_vec2_close(v_py_converted, v_py)


def test_float3():
    v_py = glm.vec3(1.0, -2.0, 3.0)
    logger.info(f"Created float3 in glm: {v_py}")
    v_slang = test_module.test_float3(to_slang(v_py))
    logger.info(f"Received float3 from Slang: {v_slang}")
    v_py_converted = from_slang(v_slang)
    _assert_vec3_close(v_py_converted, v_py)


def test_float4_as_vec4():
    v_py = glm.vec4(1.0, -2.0, 3.0, -4.0)
    logger.info(f"Created float4 (vec4) in glm: {v_py}")
    v_slang = test_module.test_float4(to_slang(v_py))
    logger.info(f"Received float4 (vec4) from Slang: {v_slang}")
    v_py_converted = from_slang(v_slang, glm.vec4)
    _assert_vec4_close(v_py_converted, v_py)


def test_float4_as_quat():
    q_py = glm.quat(1.0, 2.0, 3.0, 4.0)
    logger.info(f"Created float4 (quat) in glm: {q_py}")
    q_slang = test_module.test_float4(to_slang(q_py))
    logger.info(f"Received float4 (quat) from Slang: {q_slang}")
    q_py_converted = from_slang(q_slang, glm.quat)
    _assert_quat_close(q_py_converted, q_py)


def test_float2x2():
    m_py = glm.mat2(
        1.0,
        2.0,
        3.0,
        4.0,
    )
    logger.info(f"Created float2x2 in glm: {m_py}")
    m_slang = test_module.test_float2x2(to_slang(m_py))
    logger.info(f"Received float2x2 from Slang: {m_slang}")
    m_py_converted = from_slang(m_slang)
    _assert_mat2_close(m_py_converted, m_py)


def test_float3x3():
    m_py = glm.mat3(
        1.0,
        2.0,
        3.0,
        4.0,
        5.0,
        6.0,
        7.0,
        8.0,
        9.0,
    )
    logger.info(f"Created float3x3 in glm: {m_py}")
    m_slang = test_module.test_float3x3(to_slang(m_py))
    logger.info(f"Received float3x3 from Slang: {m_slang}")
    m_py_converted = from_slang(m_slang)
    _assert_mat3_close(m_py_converted, m_py)


def test_float4x4():
    m_py = glm.mat4(
        1.0,
        2.0,
        3.0,
        4.0,
        5.0,
        6.0,
        7.0,
        8.0,
        9.0,
        10.0,
        11.0,
        12.0,
        13.0,
        14.0,
        15.0,
        16.0,
    )
    logger.info(f"Created float4x4 in glm: {m_py}")
    m_slang = test_module.test_float4x4(to_slang(m_py))
    logger.info(f"Received float4x4 from Slang: {m_slang}")
    m_py_converted = from_slang(m_slang)
    _assert_mat4_close(m_py_converted, m_py)
