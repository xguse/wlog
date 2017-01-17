"""Install setup."""
import setuptools

setuptools.setup(
    name="wlog",
    version="0.0.1",
    url="git@github.com:xguse/wlog.git",

    author="Gus Dunn",
    author_email="w.gus.dunn@gmail.com",

    description="A pyramid site project for my work log.",
    # long_description=open('README.rst').read(),

    packages=setuptools.find_packages('src'),
    package_dir={"": "src"},


    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    entry_points={
    "console_scripts": [
        "wlog = wlog.cli.main:run",
        ]
    },
)
