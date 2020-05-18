#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kpkpass
Version  : 20.04.1
Release  : 21
URL      : https://download.kde.org/stable/release-service/20.04.1/src/kpkpass-20.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.1/src/kpkpass-20.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.1/src/kpkpass-20.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: kpkpass-data = %{version}-%{release}
Requires: kpkpass-lib = %{version}-%{release}
Requires: kpkpass-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules shared-mime-info
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kpkpass-20.04.1
cd %{_builddir}/kpkpass-20.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589839899
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1589839899
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpkpass
cp %{_builddir}/kpkpass-20.04.1/COPYING.LIB %{buildroot}/usr/share/package-licenses/kpkpass/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/mime-packages/application-vnd-apple-pkpass.xml
/usr/share/qlogging-categories5/org_kde_kpkpass.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim/KPkPass/Barcode
/usr/include/KPim/KPkPass/BoardingPass
/usr/include/KPim/KPkPass/Field
/usr/include/KPim/KPkPass/Location
/usr/include/KPim/KPkPass/Pass
/usr/include/KPim/KPkPass/barcode.h
/usr/include/KPim/KPkPass/boardingpass.h
/usr/include/KPim/KPkPass/field.h
/usr/include/KPim/KPkPass/kpkpass_export.h
/usr/include/KPim/KPkPass/location.h
/usr/include/KPim/KPkPass/pass.h
/usr/lib64/cmake/KPimPkPass/KPimPkPassConfig.cmake
/usr/lib64/cmake/KPimPkPass/KPimPkPassConfigVersion.cmake
/usr/lib64/cmake/KPimPkPass/KPimPkPassTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPimPkPass/KPimPkPassTargets.cmake
/usr/lib64/libKPimPkPass.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKPimPkPass.so.5
/usr/lib64/libKPimPkPass.so.5.14.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpkpass/9a1929f4700d2407c70b507b3b2aaf6226a9543c
