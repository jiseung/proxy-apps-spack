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
#     spack install amr-exp-parabolic
#
# You can edit this file again by typing:
#
#     spack edit amr-exp-parabolic
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class AmrExpParabolic(MakefilePackage):
    """ simplified block-structured adaptive mesh refinement algorithm in two and three dimensions with subcycling in time. The algorithm solves a linear advection diffusion equation with a simple numerical method. This proxy app is intended to capture the communication pattern of an explicit AMR algorithm but does not represent an accurate characterization of floating point effort or relative costs of communication to computation."""

    homepage = "https://ccse.lbl.gov/ExaCT/index.html"
    url      = "https://ccse.lbl.gov/ExaCT/AMR_Exp_Parabolic.tgz"

    variant('ndebug', default=False, description='Turn off debugging')
    variant('mpi', default=True, description='Build with MPI support')
    variant('openmp', default=False, description='Build with OpenMP support')
    variant('prof', default=False, description='Use profiler')
    variant('mkverbose', default=True, description='Verbosity of building process')

    depends_on('mpi', when='+mpi')
    depends_on('openmp', when='+openmp')


    # def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter('Makefile')
        # makefile.filter('CC = .*', 'CC = cc')
        # if '+ndebug' in spec:
        # if '+mic' in spec:
        # if '-k_use_automatic' not in spec:
        # if '-mkverbose' not in spec:
