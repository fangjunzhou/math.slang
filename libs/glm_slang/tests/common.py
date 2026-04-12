from pyglm import glm
from pathlib import Path
import slangpy as spy
from spm_slang.package import SlangPackage
from spm_slang.package_manager import SlangPackageManager

from glm_slang import GlmSlang

SHADER_PATH = Path(__file__).parent / "slang"


class GlmSlangTest(SlangPackage):
    @staticmethod
    def name() -> str:
        return "glm_slang_test"

    @staticmethod
    def shader_paths() -> list[str]:
        return [str(SHADER_PATH)]

    @staticmethod
    def dependencies() -> list[type[SlangPackage]]:
        return [GlmSlang]

    def build(self) -> spy.Module:
        module = spy.Module.load_from_file(
            device=self._device,
            path="glm_test.slang",
            link=self._dependencies,
        )
        return module


SlangPackageManager.register_package(GlmSlangTest)


def _assert_vec2_close(actual: glm.vec2, expected: glm.vec2, eps: float = 1e-6):
    assert glm.all(
        glm.epsilonEqual(actual, expected, eps)
    ), f"Expected {expected}, got {actual}"


def _assert_quat_close(actual: glm.quat, expected: glm.quat, eps: float = 1e-6):
    assert glm.all(
        glm.epsilonEqual(actual, expected, eps)
    ), f"Expected {expected}, got {actual}"


def _assert_vec3_close(actual: glm.vec3, expected: glm.vec3, eps: float = 1e-6):
    assert glm.all(
        glm.epsilonEqual(actual, expected, eps)
    ), f"Expected {expected}, got {actual}"


def _assert_vec4_close(actual: glm.vec4, expected: glm.vec4, eps: float = 1e-6):
    assert glm.all(
        glm.epsilonEqual(actual, expected, eps)
    ), f"Expected {expected}, got {actual}"


def _assert_mat2_close(actual: glm.mat2, expected: glm.mat2, eps: float = 1e-6):
    for col in range(2):
        assert glm.all(
            glm.epsilonEqual(actual[col], expected[col], eps)
        ), f"Expected {expected}, got {actual}"


def _assert_mat3_close(actual: glm.mat3, expected: glm.mat3, eps: float = 1e-6):
    for col in range(3):
        assert glm.all(
            glm.epsilonEqual(actual[col], expected[col], eps)
        ), f"Expected {expected}, got {actual}"


def _assert_mat4_close(actual: glm.mat4, expected: glm.mat4, eps: float = 1e-6):
    for col in range(4):
        assert glm.all(
            glm.epsilonEqual(actual[col], expected[col], eps)
        ), f"Expected {expected}, got {actual}"
