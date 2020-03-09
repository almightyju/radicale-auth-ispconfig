#!/usr/bin/env python

from setuptools import setup

setup(name='radicale-auth-ispconfig',
      version='0.1',
      description='Auth users against ispconfig 3 mail user for Radicale 2',
      author='Julian Preece',
      url='https://github.com/almightyju/radicale-auth-ispconfig/',
      license='GNU GPL v3',
      install_requires=['radicale >= 2.0', 'PyMySQL'],
      packages=['radicale_auth_ispconfig'],
     )