from setuptools import setup, find_packages

setup(
    name="Xtouch2Vjoy",  # Replace with your project's name
    version="0.1.1",  # Initial version
    author="Hernan Di Tano",
    author_email="hditano[@gmail.com",
    description="This script maps MIDI Control Change (CC) and Note On/Off messages from a Behringer X-Touch Mini to vJoy virtual joystick inputs. It allows you to control vJoy axes and buttons using MIDI devices.",
    long_description=open("README.md").read(),  # Use README.md for PyPI description
    long_description_content_type="text/markdown",  # Markdown is recommended
    url="https://github.com/hditano/Xtouch2Vjoy",  # Project's homepage
    packages=find_packages(),  # Automatically find all sub-packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Update based on your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Minimum Python version
    install_requires=[
        "mido",  # Add dependencies here
        "pyvjoy",
    ],
)
