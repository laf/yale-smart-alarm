import setuptools

setuptools.setup(
    name='yalesmartalarm',
    py_modules=['yalesmartalarmc'],
    version='0.1.0',
    description='Talk to the Yale API for Yale Smart Alarms',
    long_description='Talk to the Yale API for Yale Smart Alarms',
    long_description_content_type="text/markdown",
    author='Neil Lathwood',
    email='gh+n@laf.io',
    url='https://github.com/laf/yale-smart-alarm',
    download_url='https://github.com/laf/yale-smart-alarm',
    keywords=['Yale', 'Smart Alarm', 'Yale Smart Alarm'],
    package_data={'': ['data/*.json']},
    install_requires=['requests>=2.0.0'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
)
