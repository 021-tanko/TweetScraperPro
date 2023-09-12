setup(
	name=NAME,
	version=about['__version__'],
	description=DESCRIPTION,
	long_description=long_description,
	long_description_content_type="text/markdown",
	author=AUTHOR,
	author_email=EMAIL,
	python_requires=REQUIRES_PYTHON,
	url=URL,
	packages=['tweetscraperpro', 'tweetscraperpro.storage'],
	entry_points={
		'console_scripts':[
			'tweetscraperpro = tweetscraperpro.cli:run_as_command',
		],
	},
	install_requires=REQUIRED,
	license='MIT',
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		],
)
