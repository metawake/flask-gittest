"""
Flask-Gittest
"""

#This is the description for that library

from setuptools import setup


setup(
    name='Flask-Gittest',
    version='1.0',
    license='BSD',
    author='Alex Alexapolsky',
    author_email='your-email@example.com',
    description='A blueprint of page with git info about running web app, like status and current branch/commit',
    long_description=__doc__,
    py_modules=['flask_gittest'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)