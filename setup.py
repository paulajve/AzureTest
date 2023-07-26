from setuptools import setup

    setup(
        name='factorial',
        version='1.0.0',
        author='Bard',
        author_email='bard@example.com',
        description='A Python package for calculating factorials.',
        url='https://github.com/bard/factorial',
        packages=['factorial'],
        install_requires=[],
        entry_points={
            'console_scripts': ['factorial=factorial.factorial:main'],
        },
    )
