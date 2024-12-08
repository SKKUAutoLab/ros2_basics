from setuptools import setup

package_name = 'demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='A demo package with talker and listener nodes.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = demo.talker:main',
            'listener = demo.listener:main',
        ],
    },
)
