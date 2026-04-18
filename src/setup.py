from setuptools import setup
import setup_translate

pkg = 'Extensions.PlanerFS'
setup(name='enigma2-plugin-extensions-planerfs',
       version='1.0',
       description='PlanerFS',
       package_dir={pkg: 'PlanerFS'},
       packages=[pkg],
       package_data={pkg: ['skin/*.png', 'skin/HD/*.png', 'skin/HD/*.xml', 'skin/fHD/*.png', 'skin/fHD/*.xml', 'schichtpicons/*.png', '*.png', '*.xml', '*.txt', 'locale/*/LC_MESSAGES/*.mo', 'LICENSE']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
