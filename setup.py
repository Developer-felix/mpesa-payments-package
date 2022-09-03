"""
Auther : Onjomba Felix
Phone : +254717713943
license : MIT
"""

from distutils.core import setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'mpesa_payments',         # How you named your package folder (MyLib)
  packages = ['mpesa_payments'],   # Chose the same as "name"
  version = '1.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Mpesa Payments Package For B2C and C2B',   # Give a short description about your library
  author = 'Felix Onjomba',                   # Type in your name
  author_email = 'onjombafelix1@gmail.com',       # Type in your E-Mail
  url = 'https://github.com/Developer-Felix/mpesa-payments-package',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Developer-Felix/mpesa-payments-package/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Mpesa Payments', 'Mpesa', 'Payments','B2C','C2B'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)