"""
Paginator

"""

from setuptools import setup, find_packages

__NAME__ = "Paginator"
__version__ = "0.2.0"
__license__ = "MIT"
__author__ = "Mardix"
__copyright__ = "(c) 2015 Mardix"

setup(
    name=__NAME__,
    version=__version__,
    license=__license__,
    author=__author__,
    author_email='mardix@pylot.io',
    description="Paginator for SQLAlchemy query object, list or iterable ",
    long_description=__doc__,
    url='http://github.com/mardix/paginator.py/',
    download_url='http://github.com/mardix/paginator.py/tarball/master',
    py_modules=['paginator'],
    include_package_data=True,
    install_requires=[
        "six==1.9.0"
    ],
    keywords=["pagination", "paginate", "page", "flask", "jinja2", "sqlalchemy"],
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False
)
