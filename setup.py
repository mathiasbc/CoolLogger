import setuptools


setup_params = dict(
    name='coollogger',
    version='1.0.1',
    description='Keep Log files zipped and cleaned.',
    author="Mathias Bustamante",
    author_email="mathiasbc@gmail.com",
    url="https://github.com/mathiasbc/CoolLogger.git",
    download_url="https://github.com/mathiasbc/coollogger/tarball/0.0.1",
    packages=['coollogger'],
)

if __name__ == '__main__':
    setuptools.setup(**setup_params)
