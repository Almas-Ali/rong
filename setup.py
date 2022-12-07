import setuptools

with open('README.md', 'r') as README:
    long_description = README.read()

classifiers = [
    'Development Status :: 3 - Alpha',
    'Operating System :: OS Independent',
    'Intended Audience :: Developers',
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    'Natural Language :: English',
    'Environment :: Console',
]

setuptools.setup(
    name="rong",
    version="0.0.2",
    description="rong - A console coloring utility for Python 3 (open source).",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/almas-ali/rong",
    author="Md. Almas Ali",
    author_email="almaspr3@gmail.com",
    keyword="rong, color, console, console coloring",
    license="MIT",
    classifiers=classifiers,
    packages=setuptools.find_packages(),
    install_requires=[]
)
