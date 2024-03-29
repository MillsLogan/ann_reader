from setuptools import setup, find_packages

setup(name='ann_reader',
      version='0.1',
      description='A package for reading and working with .ann files',
      author='Logan Mills',
      url='github.com/millslogan/ann_reader',
      packages=['ann_reader', 'ann_reader.base_classes'],
      py_modules=['ann_loader', 'ann_reader.base_classes.document'],
      python_requires='>=3.12'
)



