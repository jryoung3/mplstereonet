from setuptools import setup

setup(
    name = 'mplstereonetedit',
    version = '0.7-dev',
    description = "Stereonets for matplotlib",
    author = 'Joe Kington',
    author_email = 'joferkington@gmail.com',
    license = 'MIT',
    url = 'https://github.com/joferkington/mplstereonet/',
    packages = ['mplstereonet'],
    install_requires = [
        'matplotlib >= 1.1',
        'numpy >= 1.1']
)
