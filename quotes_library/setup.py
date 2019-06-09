import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='quotes_library',
     version='0.1',
     scripts=['quotes_script'] ,
     author="Dhiren Serai",
     author_email="dhirensr@gmail.com",

     description="A package for getting quotes which can be used in any application.",
     long_description_content_type="text/markdown",

     url="https://github.com/javatechy/dokr",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],
        install_requires=[
        "beautifulsoup4",
		"requests"
        ],
     keywords = ['quotes', 'pyquotes', 'brainyquotes'],

 )
