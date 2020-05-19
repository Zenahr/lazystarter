from setuptools import setup

setup(
	name='lazystarter',
	version='0.0.1',
	packages=['lazystarter',],
	license='MIT',
	long_description=open('README.txt').read(),	
	install_requires=[
	],
	scripts=['bin/lazystarter'],
	entry_points = {
		'console_scripts': ['lazystarter=lazystarter.command_line:main'],
	},
	python_requires='>=3.6',
	url='https://github.com/Zenahr/lazystarter',
)
