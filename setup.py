import logging

from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

mapping_module = Extension(
    'mapanalyzerext', sources=['MapAnalyzer/cext/src/ma_ext.c'], extra_compile_args=["-DNDEBUG", "-O2"]
)
logger = logging.getLogger(__name__)

requirements = [  # pragma: no cover
        "wheel",
        "numpy~=1.22.3",
        "Cython",
        "burnysc2",
        "matplotlib",
        "scipy",
        "loguru",
        "tqdm",
        "scikit-image",
]
setup(  # pragma: no cover
        name="sc2mapanalyzer",
        # version=f"{__version__}",
        version="0.0.88",
        install_requires=requirements,
        setup_requires=["wheel", "numpy~=1.22.3"],
        cmdclass={"build_ext": build_ext},
        ext_modules=[mapping_module],
        packages=["MapAnalyzer", "MapAnalyzer.cext"],
        extras_require={
                "dev": [
                        "pytest",
                        "pytest-html",
                        "monkeytype",
                        "mypy",
                        "mpyq",
                        "pytest-asyncio",
                        "hypothesis",
                        "pytest-benchmark",
                        "sphinx",
                        "sphinx-autodoc-typehints",
                        "pytest-cov",
                        "coverage",
                        "codecov",
                        "mutmut",
                        "radon",
                ]
        },
)
