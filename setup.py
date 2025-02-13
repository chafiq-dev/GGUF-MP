from setuptools import setup, find_packages

setup(
    name='NeuroKit',
    version='0.1.0',
    description='A neural model management tool with advanced PyTorch integration.',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'torch',
        'pyyaml',
        'psutil',
        'jsonschema'
    ],
    entry_points={
        'console_scripts': [
            'neurokit=neurokit.__main__:main'
        ]
    },
)
