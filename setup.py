from setuptools import setup, find_packages

setup(
      name='CC-pruebas',
      packages=find_packages(),
      version='0.1',
      long_description=__doc__,
      zip_safe=False,
      test_suite='nose.collector',
      include_package_data=True,
      install_requires=[
                        'Flask==1.0.2',
                        'requests==2.20.1',
                        'gunicorn==19.9.0',
                        'PyMySQL==0.9.3',
                        'flask_mysqldb==0.2.0',
                        'pymongo==2.8.1',
                        ],
      tests_require=['nose'],
      )
