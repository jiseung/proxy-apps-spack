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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install pennant
#
# You can edit this file again by typing:
#
#     spack edit pennant
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Pennant(MakefilePackage):
    """PENNANT is an unstructured mesh physics mini-app designed for advanced architecture research. It contains mesh data structures and a few physics algorithms adapted from the LANL rad-hydro code FLAG, and gives a sample of the typical memory access patterns of FLAG."""

    homepage = "https://github.com/lanl/PENNANT"
    url      = "https://github.com/lanl/PENNANT/archive/pennant_v0.9.tar.gz"

    version('0.9', '4f21ba3836b2721436277308c2e33f45')
    version('0.8', 'a1afff4914fef8140c3024a02d7c993c')
    version('0.7', 'd642a030d5388f65f799504803794a4e')
    version('0.6', '8ab2d4b47ec9870643bfe6f262cd47a4')
    version('0.5', '534547878c698b9926e2886c74e10831')
    version('0.4', '0f67d8da0a92bd42d92a4823d3e4dbe1')

    variant('mpi', default=True, description='Build with MPI support')
    variant('openmp', default=True, description='Build with OpenMP support')
    variant('debug', default=False, description='Enable debug')

    depends_on('mpi', when='+mpi')

    def edit(self, spec, prefix):
        makefile = FileFilter('Makefile')

        debug = '-g'
        opt = '-O3'

        if self.compiler.name == 'icpc':
            opt += ' -fast -fno-alias'
        if self.compiler.name == 'pgCC':
            compiler = 'pgCC'
            opt += ' -fastsse'

        makefile.filter('CXX .*', 'CXX := c++')
        makefile.filter('CXXFLAGS_DEBUG .*', 'CXXFLAGS_DEBUG := {0}'.format(debug))
        makefile.filter('CXXFLAGS_OPT .*', 'CXXFLAGS_OPT := {0}'.format(opt))
        makefile.filter('CXXFLAGS_OPENMP .*', 'CXXFLAGS_OPENMP := {0}'.format(self.compiler.openmp_flag))
        
        if '+mpi' in spec:
            makefile.filter('CXX .*', 'CXX := {0}'.format(spec['mpi'].mpicxx))

        if '+mpi' not in spec:
            makefile.filter('CXX := mpicxx', '#')
            makefile.filter('-DUSE_MPI', '#')
            makefile.filter('CXX .*', 'CXX := c++')

        if '+openmp' not in spec:
            makefile.filter('.*CXXFLAGS_OPENMP.*', '#')
        
        if '+debug' in spec:
            makefile.filter('.*(CXXFLAGS_OPT).*', 'CXXFLAGS := $(CXXFLAGS_DEBUG)')

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install('build/pennant', prefix.bin)
