from setuptools import setup

versionfile = 'poet/version.py'
with open(versionfile, 'rb') as f:
    exec(compile(f.read(), versionfile, 'exec'))

setup(
    name='homebrew-pypi-poet',
    version=__version__,  # noqa
    url='https://github.com/tdsmith/homebrew-pypi-poet',
    license='MIT',
    author='Tim D. Smith',
    author_email='poet@tim-smith.us',
    description='Writes Homebrew stanzas for pypi packages',
    packages=['poet'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['jinja2', 'pypi-simple < 1', 'setuptools'],
    entry_points={'console_scripts': [
        'poet=poet:main',
        'poet_lint=poet.lint:main',
    ]}
)
