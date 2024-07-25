from setuptools import setup


setup(
    name="wrapture-test",
    install_requires="wrapture",
    entry_points={"wrapture": ["test = lib"]},
    py_modules=["lib"],
)