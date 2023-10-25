from setuptools import setup
import os
from glob import glob

package_name = 'otomo_webserver'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools', 'Flask'],
    zip_safe=False,
    maintainer='tom',
    maintainer_email='thomaswallis0@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'otomo_webserver = otomo_webserver.otomo_webserver:main'
        ],
    },
    include_package_data=True
)
