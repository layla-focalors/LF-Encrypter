from setuptools import setup, find_packages

setup(
    name                = 'LF-Encrypter',
    version             = '1.1',
    description         = 'Layla-Focalors, login Encrypter',
    author              = 'Layla-Focalors',
    author_email        = 'sjhhjs2004@kakao.com',
    url                 = 'https://github.com/layla-focalors/LF-Encrypter',
    install_requires    =  ['os', 'hashlib','pymysql', 'datetime'],
    packages            = find_packages(exclude = []),
    keywords            = ['encrypt', 'sha265', 'database'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)