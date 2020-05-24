from setuptools import setup

setup(
	name='lazystarter',
	version='0.0.1015',
	packages=['lazystarter',],
	license='MIT',
	long_description=open('README.txt').read(),	
	install_requires=[
	],
	scripts=['lazystarter/__init__.py'],
	entry_points = {
		'console_scripts': ['lazystarter=lazystarter.command_line:main'],
	},
	python_requires='>=3.6',
	url='https://github.com/Zenahr/lazystarter',
)
