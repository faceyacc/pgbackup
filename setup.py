from setuptools import find_packages, setup


# This is so that you don't have to hardwire the long disription of the
# package, you can just 'read' it in.
with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='pgbackup',
    version='0.1.0',
    author='Ty Facey',
    author_email='faceyt@wit.edu',
    description='A utility for backing up PostreSQL datasets',
    long_description=long_description,
    url='https://github.com/faceyacc/pgbackup',
    # This is where find the sub-packages that is in the 'src' directory
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ],
    }

)
