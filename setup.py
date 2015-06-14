
from setuptools import setup, find_packages
import paginator

PACKAGE = paginator

setup(
    name=PACKAGE.__NAME__,
    version=PACKAGE.__version__,
    license=PACKAGE.__license__,
    author=PACKAGE.__author__,
    author_email='mardix@pylot.io',
    description="Paginator for SQLAlchemy query object, list or iterable ",
    long_description=PACKAGE.__doc__,
    url='http://github.com/mardix/paginator.py/',
    download_url='http://github.com/mardix/paginator.py/tarball/master',
    py_modules=['paginator'],
    include_package_data=True,
    install_requires=[
        "six"
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
