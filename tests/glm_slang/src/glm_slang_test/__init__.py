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
        return spy.Module.load_from_file(
            device=self._device,
            path="glm_test.slang",
            link=self._dependencies,
        )


SlangPackageManager.register_package(GlmSlangTest)
