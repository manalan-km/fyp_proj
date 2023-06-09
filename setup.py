from setuptools import setup
from glob import glob
import os 
package_name = 'fyp_proj'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'description'), glob('description/*')),
        (os.path.join('share',package_name,'launch'), glob('launch/*')),
        (os.path.join('share',package_name,'config'), glob('config/*')), 
        (os.path.join('share',package_name,'behaviour_tree'), glob('behaviour_tree/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='manalan',
    maintainer_email='mkumarasamymuru@deakin.edu.au',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'travel_to_points_exe = fyp_proj.nav_to_pose:main'
        ],
    },
)
