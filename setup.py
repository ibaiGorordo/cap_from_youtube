from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='cap_from_youtube',
    version='0.0.8',
    license='MIT',
    description='Get an OpenCV video capture from an YouTube video URL',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ibai Gorordo',
    url='https://github.com/ibaiGorordo/cap_from_youtube',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'yt_dlp',
    ],
)