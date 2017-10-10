import os
from setuptools import find_packages, setup

# with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
#     README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pivotal_fetcher',
    version='5.1.1',
    packages=find_packages(),
    install_requires=[
        'beautifultable==0.3.0',
        'requests',
    ],
    include_package_data=True,
    license='MIT License',  # example license
    description='Fetches Pivotal Tracker Stories.',
    # long_description=README,
    url='https://github.com/xxihawkxx/pivotal_fetcher',
    author='Chetan Bhatt',
    author_email='ichetanbhatt@gmail.com',
    classifiers=[
        # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
    ],
    entry_points={
            'console_scripts': [
                'pt_fetch=pivotal_fetcher:accepted',
            ],
        },

)