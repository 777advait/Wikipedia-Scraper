import setuptools
from shutil import rmtree

setuptools.setup( 
    name='Wikipedia-Scraper', 
    version='1.0', 
    author='Advait Jadhav', 
    description='A basic wikipedia scraper which grabs information from wikipedia.org based on user input.',
    packages=setuptools.find_packages(), 
    entry_points={ 
        'console_scripts': [ 
            'wikiscraper = wikiscraper.__main__:main' 
        ] 
    }, 
    classifiers=[ 
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ], 
)

dirs = ['build', 'dist', 'Wikipedia_Scraper.egg-info']

for dir in dirs:
    rmtree(dir)