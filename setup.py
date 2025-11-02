from setuptools import setup

setup(
    name='lvs-cli',
    version='0.1',
    py_modules=['lvs'],  # Lista de módulos (arquivos .py) que serão incluídos
    install_requires=[
        'requests>=2.28.0',
    ],
    entry_points={
        'console_scripts': [
            'lvs = lvs:main',
        ],
    },
)