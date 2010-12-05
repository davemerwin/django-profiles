from distutils.core import setup

setup(name='django-profiles',
      version='0.3',
      description='User-profile application for Django',
      author='James Bennett, Dave Merwin',
      author_email='james@b-list.org, dave@davemerwin.com',
      url='https://github.com/davemerwin/django-profiles',
      download_url='https://github.com/davemerwin/django-profiles/archives/master',
      packages=['profiles'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
