import setuptools
from setuptools import setup

setup(name='gym_gridworld',
      version='0.0.1',
      author='André Teixeira',
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      description='A variation of the OpenAI gym Frozen Lake, mimicking the minimalistic GridWorld',
      url='https://github.com/andremht/gym_gridworld',
      packages=setuptools.find_packages(),
      install_requires=['gym>=0.2.3']
)
