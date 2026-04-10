from pathlib import Path
import logging
import slangpy as spy
from pyglm import glm
from spm.package_manager import SlangPackageManager

from glm_slang.conversion import to_slang, from_slang

from common import (
    GlmSlangTest,
    _assert_quat_close,
    _assert_vec3_close,
    _assert_mat3_close,
)

logger = logging.getLogger(__name__)

package_manager = SlangPackageManager()
test_module = package_manager.module_map[GlmSlangTest.name()]


# Test cases for quaternion functions.
def test_identity():
    q = from_slang(test_module.test_identity())
    q_expected = glm.quat(1.0, 0.0, 0.0, 0.0)
    assert q == q_expected, f"Expected {q_expected}, got {q}"


# Test multiplication of two quaternions.
def test_mul():
    a = glm.normalize(glm.quat(1.0, 2.0, 3.0, 4.0))
    b = glm.normalize(glm.quat(5.0, 6.0, 7.0, 8.0))
    q_expected = a * b
    logger.info(f"Testing multiplication: a={a}, b={b}, expected={q_expected}")
    a_slang = to_slang(a)
    b_slang = to_slang(b)
    q_slang = test_module.test_mul(a_slang, b_slang)
    q = from_slang(q_slang)
    logger.info(f"Result from slang: {q}")
    _assert_quat_close(q, q_expected)


def test_conj():
    q = glm.normalize(glm.quat(1.0, 2.0, -3.0, 4.0))
    q_expected = glm.conjugate(q)
    logger.info(f"Testing conjugate: q={q}, expected={q_expected}")
    q_slang = test_module.test_conj(to_slang(q))
    q_actual = from_slang(q_slang)
    logger.info(f"Result from slang: {q_actual}")
    _assert_quat_close(q_actual, q_expected)


def test_inv():
    q = glm.normalize(glm.quat(1.0, -2.0, 3.0, -4.0))
    q_expected = glm.quat(glm.inverse(q))
    logger.info(f"Testing inverse: q={q}, expected={q_expected}")
    q_slang = test_module.test_inv(to_slang(q))
    q_actual = from_slang(q_slang)
    logger.info(f"Result from slang: {q_actual}")
    _assert_quat_close(q_actual, q_expected)


def test_from_axis_angle():
    axis = glm.normalize(glm.vec3(1.0, -2.0, 3.0))
    angle = 0.7
    axis_angle = axis * angle

    q_expected = glm.angleAxis(angle, axis)
    logger.info(
        f"Testing fromAxisAngle: axis={axis}, angle={angle}, axis_angle={axis_angle}, expected={q_expected}"
    )
    q_slang = test_module.test_from_axis_angle(to_slang(axis_angle))
    q_actual = from_slang(q_slang)
    logger.info(f"Result from slang: {q_actual}")
    _assert_quat_close(q_actual, q_expected)


def test_as_axis_angle():
    axis = glm.normalize(glm.vec3(-1.0, 2.0, 0.5))
    angle = 1.1
    q = glm.angleAxis(angle, axis)

    axis_angle_expected = glm.axis(q) * glm.angle(q)
    logger.info(f"Testing asAxisAngle: q={q}, expected={axis_angle_expected}")
    axis_angle_slang = test_module.test_as_axis_angle(to_slang(q))
    axis_angle_actual = from_slang(axis_angle_slang)
    logger.info(f"Result from slang: {axis_angle_actual}")
    _assert_vec3_close(axis_angle_actual, axis_angle_expected)


def test_rotate():
    axis = glm.normalize(glm.vec3(2.0, 1.0, -1.0))
    angle = 0.9
    q = glm.angleAxis(angle, axis)
    v = glm.vec3(1.0, -0.5, 2.0)

    v_expected = glm.vec3(q * v)
    logger.info(f"Testing rotate: q={q}, v={v}, expected={v_expected}")
    v_slang = test_module.test_rotate(to_slang(q), to_slang(v))
    v_actual = from_slang(v_slang)
    logger.info(f"Result from slang: {v_actual}")
    _assert_vec3_close(v_actual, v_expected)


def test_as_mat3():
    axis = glm.normalize(glm.vec3(0.2, -0.4, 0.9))
    angle = 1.3
    q = glm.angleAxis(angle, axis)

    m_expected = glm.mat3_cast(q)
    logger.info(f"Testing asMat3: q={q}, expected={m_expected}")
    m_slang = test_module.test_as_mat3(to_slang(q))
    m_actual = from_slang(m_slang)
    logger.info(f"Result from slang: {m_actual}")
    _assert_mat3_close(m_actual, m_expected)
