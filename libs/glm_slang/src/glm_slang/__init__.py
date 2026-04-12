from pathlib import Path
import slangpy as spy
from spm_slang.package import SlangPackage
from spm_slang.package_manager import SlangPackageManager

SHADER_PATH = Path(__file__).parent / "slang"


class GlmSlang(SlangPackage):
    @staticmethod
    def name() -> str:
        return "glm_slang"

    @staticmethod
    def shader_paths() -> list[str]:
        return [str(SHADER_PATH)]

    @staticmethod
    def dependencies() -> list[type[SlangPackage]]:
        return []

    def build(self) -> spy.Module:
        module = spy.Module.load_from_file(
            device=self._device,
            path="glm.slang",
            link=self._dependencies,
        )
        return module


SlangPackageManager.register_package(GlmSlang)
