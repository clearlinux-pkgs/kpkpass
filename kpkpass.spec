#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kpkpass
Version  : 23.04.2
Release  : 55
URL      : https://download.kde.org/stable/release-service/23.04.2/src/kpkpass-23.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.2/src/kpkpass-23.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.2/src/kpkpass-23.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
Requires: kpkpass-data = %{version}-%{release}
Requires: kpkpass-lib = %{version}-%{release}
Requires: kpkpass-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

%package data
Summary: data components for the kpkpass package.
Group: Data

%description data
data components for the kpkpass package.


%package dev
Summary: dev components for the kpkpass package.
Group: Development
Requires: kpkpass-lib = %{version}-%{release}
Requires: kpkpass-data = %{version}-%{release}
Provides: kpkpass-devel = %{version}-%{release}
Requires: kpkpass = %{version}-%{release}

%description dev
dev components for the kpkpass package.


%package lib
Summary: lib components for the kpkpass package.
Group: Libraries
Requires: kpkpass-data = %{version}-%{release}
Requires: kpkpass-license = %{version}-%{release}

%description lib
lib components for the kpkpass package.


%package license
Summary: license components for the kpkpass package.
Group: Default

%description license
license components for the kpkpass package.


%prep
%setup -q -n kpkpass-23.04.2
cd %{_builddir}/kpkpass-23.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686511587
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1686511587
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpkpass
cp %{_builddir}/kpkpass-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kpkpass/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kpkpass-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kpkpass/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kpkpass-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kpkpass/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kpkpass-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kpkpass-%{version}/autotests/data/boardingpass-v1.pkpass.license %{buildroot}/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kpkpass-%{version}/autotests/data/boardingpass-v2.pkpass.license %{buildroot}/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kpkpass-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kpkpass/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/mime-packages/application-vnd-apple-pkpass.xml
/usr/share/qlogging-categories5/org_kde_kpkpass.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim5/KPkPass/Barcode
/usr/include/KPim5/KPkPass/BoardingPass
/usr/include/KPim5/KPkPass/Field
/usr/include/KPim5/KPkPass/Location
/usr/include/KPim5/KPkPass/Pass
/usr/include/KPim5/KPkPass/barcode.h
/usr/include/KPim5/KPkPass/boardingpass.h
/usr/include/KPim5/KPkPass/field.h
/usr/include/KPim5/KPkPass/kpkpass_export.h
/usr/include/KPim5/KPkPass/kpkpass_version.h
/usr/include/KPim5/KPkPass/location.h
/usr/include/KPim5/KPkPass/pass.h
/usr/lib64/cmake/KPim5PkPass/KPim5PkPassConfig.cmake
/usr/lib64/cmake/KPim5PkPass/KPim5PkPassConfigVersion.cmake
/usr/lib64/cmake/KPim5PkPass/KPim5PkPassTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5PkPass/KPim5PkPassTargets.cmake
/usr/lib64/cmake/KPimPkPass/KPim5PkPassTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPimPkPass/KPim5PkPassTargets.cmake
/usr/lib64/cmake/KPimPkPass/KPimPkPassConfig.cmake
/usr/lib64/cmake/KPimPkPass/KPimPkPassConfigVersion.cmake
/usr/lib64/libKPim5PkPass.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5PkPass.so.5.23.2
/usr/lib64/libKPim5PkPass.so.5
/usr/lib64/libKPim5PkPass.so.5.23.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpkpass/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kpkpass/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kpkpass/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kpkpass/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d
