#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 94c6be0
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kpkpass
Version  : 24.12.2
Release  : 78
URL      : https://download.kde.org/stable/release-service/24.12.2/src/kpkpass-24.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.2/src/kpkpass-24.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.2/src/kpkpass-24.12.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.0
Requires: kpkpass-data = %{version}-%{release}
Requires: kpkpass-lib = %{version}-%{release}
Requires: kpkpass-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
BuildRequires : shared-mime-info
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KPkPass
Library to deal with Apple Wallet pass files.
## File Format
Apple Wallet files are essentially ZIP files containing a JSON description of the pass,
translated message catalogs and graphical assets to render the pass.

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kpkpass-24.12.2
cd %{_builddir}/kpkpass-24.12.2
pushd ..
cp -a kpkpass-24.12.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738960832
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1738960832
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpkpass
cp %{_builddir}/kpkpass-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kpkpass/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kpkpass-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kpkpass/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kpkpass-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kpkpass/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kpkpass-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kpkpass-%{version}/autotests/data/boardingpass-v1.pkpass.license %{buildroot}/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kpkpass-%{version}/autotests/data/boardingpass-v2.pkpass.license %{buildroot}/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kpkpass-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kpkpass/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
cp %{_builddir}/kpkpass-%{version}/readme-build-ftime.txt.license %{buildroot}/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/mime-packages/application-vnd-apple-pkpass.xml
/usr/share/qlogging-categories6/org_kde_kpkpass.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/KPkPass/Barcode
/usr/include/KPim6/KPkPass/BoardingPass
/usr/include/KPim6/KPkPass/Field
/usr/include/KPim6/KPkPass/Location
/usr/include/KPim6/KPkPass/Pass
/usr/include/KPim6/KPkPass/barcode.h
/usr/include/KPim6/KPkPass/boardingpass.h
/usr/include/KPim6/KPkPass/field.h
/usr/include/KPim6/KPkPass/kpkpass_export.h
/usr/include/KPim6/KPkPass/kpkpass_version.h
/usr/include/KPim6/KPkPass/location.h
/usr/include/KPim6/KPkPass/pass.h
/usr/lib64/cmake/KPim6PkPass/KPim6PkPassConfig.cmake
/usr/lib64/cmake/KPim6PkPass/KPim6PkPassConfigVersion.cmake
/usr/lib64/cmake/KPim6PkPass/KPim6PkPassTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6PkPass/KPim6PkPassTargets.cmake
/usr/lib64/libKPim6PkPass.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6PkPass.so.6.3.2
/usr/lib64/libKPim6PkPass.so.6
/usr/lib64/libKPim6PkPass.so.6.3.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpkpass/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kpkpass/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kpkpass/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kpkpass/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d
