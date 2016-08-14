from setuptools import setup, find_packages

setup(
    name="seed-control-interface",
    version="0.1",
    url='http://github.com/praekelt/seed-control-interface',
    license='BSD',
    author='Praekelt Foundation',
    author_email='dev@praekeltfoundation.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django==1.9.1',
        'dj-database-url==0.3.0',
        'psycopg2==2.6.1',
        'raven==5.10.0',
        'gunicorn==19.4.5',
        'whitenoise==2.0.6',
        'pytz==2015.7',
        'python-dateutil==2.5.3',
        'django-bootstrap-form==3.2.1',
        'seed-services-client==0.2.0',
        'go-http==0.3.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
