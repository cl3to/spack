# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cppad(CMakePackage):
    """A Package for Differentiation of C++ Algorithms."""

    homepage = "https://www.coin-or.org/CppAD/"
    url = "http://www.coin-or.org/download/source/CppAD/cppad-20170114.gpl.tgz"
    git = "https://github.com/coin-or/CppAD.git"

    version("develop", branch="master")
    version(
        "20180000.0", sha256="1c355713e720fc5226ff3d6db2909922d46cd7ee0d36ee7985882f86905f655a"
    )
    version("20170114", sha256="fa3980a882be2a668a7522146273a1b4f1d8dabe66ad4aafa8964c8c1fd6f957")

    def cmake_args(self):
        # This package does not obey CMAKE_INSTALL_PREFIX
        args = [
            self.define("cppad_prefix", self.prefix),
            self.define("cmake_install_docdir", "share/cppad/doc"),
        ]
        return args
