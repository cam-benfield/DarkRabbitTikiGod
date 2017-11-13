try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config {
'description' : 'Dark Rabbit Tiki God Game',
'author' : 'Cameryn Rhosyn',
'url' : 'github.com/camrhosyn',
'download_url' : 'https://github.com/camrhosyn/DarkRabbitTikiGod',
'author_email' : 'camerynrhosyn@gmail.com',
'version' : '1.0.2',
'install_requires' : ['nose'],
'packages' : ['NAME'],
'scripts' : [],
'name' : 'darkrabbittikigod'
}

setup(**config)
