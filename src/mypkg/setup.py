from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),

    #########################################################
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob("launch/*.launch.py")),
    ],
    #########################################################




    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='phubadine',
    maintainer_email='phubadine.m@kkumail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],

    # ทางเข้า
    entry_points={
        'console_scripts': [
            "first_publisher = mypkg.first_node:main", 
            "twist_publisher = mypkg.twist_pub:main",
            "first_subscription = mypkg.first_sub:main",
            "twist_subscription = mypkg.twist_sub:main",
            "turtlebot_control = mypkg.turtlebot_control:main"
        ],
    },
)
