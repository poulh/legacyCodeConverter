from setuptools import setup, find_packages

setup(
    name='Legacy Code Converter',
    version='1.0',
    description='Convert legacy code to a modern language using OpenAI API',
    author='Poul Hornsleth',
    author_email='phornsleth@asquaredsoftware.com',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'lcc = lcc:main',
        ],
    },
)
