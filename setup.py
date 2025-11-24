# SPDX-License-Identifier: BSD-2-Clause
#
# This file is part of pyosmium. (https://osmcode.org/pyosmium/)
#
# Copyright (C) 2024 Sarah Hoffmann <lonvia@denofr.de> and others.
# For a full list of authors see the git log.
import os
import platform
import re
import subprocess
import sys

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext

BASEDIR = os.path.split(os.path.abspath(__file__))[0]


def get_versions():
    """ Read the version file.

        The file cannot be directly imported because it is not installed
        yet.
    """
    version_py = os.path.join(BASEDIR, "src/npyosmium/version.py")
    v = {}
    with open(version_py) as version_file:
        # Execute the code in version.py.
        exec(compile(version_file.read(), version_py, 'exec'), v)

    return v

class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):
    def run(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError("CMake must be installed to build the following extensions: " +
                               ", ".join(e.name for e in self.extensions))

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
                      '-DPYTHON_EXECUTABLE=' + sys.executable]

        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]

        if platform.system() == "Windows":
            cmake_args += ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(cfg.upper(), extdir)]
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
            nbr_cpus = os.cpu_count() or 2 # fallback if None is returned
            build_args += ['--', f'-j{nbr_cpus}']

        env = os.environ.copy()
        env['CXXFLAGS'] = '{} -DVERSION_INFO=\\"{}\\"'.format(env.get('CXXFLAGS', ''),
                                                              self.distribution.get_version())

        if 'LIBOSMIUM_PREFIX' in env:
            cmake_args += ['-DOSMIUM_INCLUDE_DIR={}/include'.format(env['LIBOSMIUM_PREFIX'])]
        elif os.path.exists(os.path.join(BASEDIR, 'contrib', 'libosmium', 'include', 'osmium', 'version.hpp')):
            cmake_args += ['-DOSMIUM_INCLUDE_DIR={}/contrib/libosmium/include'.format(BASEDIR)]

        if 'PROTOZERO_PREFIX' in env:
            cmake_args += ['-DPROTOZERO_INCLUDE_DIR={}/include'.format(env['PROTOZERO_PREFIX'])]
        elif os.path.exists(os.path.join(BASEDIR, 'contrib', 'protozero', 'include', 'protozero', 'version.hpp')):
            cmake_args += ['-DPROTOZERO_INCLUDE_DIR={}/contrib/protozero/include'.format(BASEDIR)]

        if 'PYBIND11_PREFIX' in env:
            cmake_args += ['-DPYBIND11_PREFIX={}'.format(env['PYBIND11_PREFIX'])]
        elif os.path.exists(os.path.join(BASEDIR, 'contrib', 'pybind11')):
            cmake_args += ['-DPYBIND11_PREFIX={}/contrib/pybind11'.format(BASEDIR)]

        if 'BOOST_PREFIX' in env:
            cmake_args += ['-DBOOST_ROOT={}'.format(env['BOOST_PREFIX'])]

        if 'CMAKE_CXX_STANDARD' in env:
            cmake_args += ['-DCMAKE_CXX_STANDARD={}'.format(env['CMAKE_CXX_STANDARD'])]

        cmake_args += [f"-DWITH_LZ4={env.get('CMAKE_WITH_LZ4', 'ON')}"]

        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)
        subprocess.check_call(['cmake', ext.sourcedir] + cmake_args, cwd=self.build_temp, env=env)
        subprocess.check_call(['cmake', '--build', '.'] + build_args, cwd=self.build_temp)

versions = get_versions()


setup(
    scripts=['tools/npyosmium-get-changes', 'tools/npyosmium-up-to-date'],
    ext_modules=[CMakeExtension('cmake_example')],
    cmdclass=dict(build_ext=CMakeBuild),
    zip_safe=False,
)
