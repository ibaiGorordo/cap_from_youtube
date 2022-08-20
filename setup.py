from setuptools import setup, find_packages

setup(
    name='cap_from_youtube',
    version='0.0.1',
    license='MIT',
    description=
    'Get an OpenCV video capture from an YouTube video URL',
    author='Ibai Gorordo',
    url='https://github.com/ibaiGorordo/cap_from_youtube',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'yt_dlp',
    ],
)