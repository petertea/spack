# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDataladContainer(PythonPackage):
    """DataLad extension package for working with containerized environments"""

    homepage = "https://github.com/datalad/datalad-container/"
    pypi = "datalad_container/datalad_container-1.1.5.tar.gz"

    version("1.1.7", sha256="02574c1d3d1e83c8ef3ab75b6a3523ce5acc870b0b79af12ae433ac140c5cb16")
    version("1.1.5", sha256="f6099a0124ddb2f021531d5020a583eca3cd9243e4e609b0f58e3f72e779b601")

    depends_on("python@3.7:", when="@1.1.6:", type="build")
    depends_on("py-setuptools@43:", when="@1.1.6:", type="build")
    depends_on("py-setuptools", type="build")

    depends_on("py-datalad@0.13:", type="run")
    depends_on("py-requests@1.2:", type="run")
