##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *

class Miniamr(MakefilePackage):
    """Proxy Application. 3D stencil calculation with Adaptive Mesh Refinement (AMR)"""

    homepage = "https://mantevo.org"
    url      = "http://mantevo.org/downloads/releaseTarballs/miniapps/MiniAMR/miniAMR_1.0_all.tgz"

    version('1.0', '812e5aaaab99689a4e9381a3bbd718a6')

    variant('mpi', default=True, description='Build with MPI support')

    depends_on('mpi', when="+mpi")

    def edit(self, spec, prefix):
        if '+mpi' in spec:
            makefile = FileFilter('miniAMR_ref/Makefile.mpi')
            makefile.filter('CC   = .*', 'CC = {}'.format(spec['mpi'].mpicc))
            self.build_targets.extend(['--directory=miniAMR_ref', '--file=Makefile.mpi', 'LDLIBS=-lm'])
        else:
            self.build_targets.extend(['--directory=miniAMR_serial', '--file=Makefile.serial'])

    def install(self, spec, prefix):
        # Manual installation
        mkdir(prefix.bin)
        mkdir(prefix.doc)
        if '+mpi' in spec:
            install('miniAMR_ref/miniAMR.x', prefix.bin)
        else:
            install('miniAMR_serial/miniAMR.x', prefix.bin)
        install('miniAMR_ref/README', prefix.doc)
        install('miniAMR_ref/param.h', prefix.doc)
        install('miniAMR_ref/LICENSE', prefix.doc)
