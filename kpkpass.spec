#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kpkpass
Version  : 22.08.2
Release  : 45
URL      : https://download.kde.org/stable/release-service/22.08.2/src/kpkpass-22.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.2/src/kpkpass-22.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.08.2/src/kpkpass-22.08.2.tar.xz.sig
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
%setup -q -n kpkpass-22.08.2
cd %{_builddir}/kpkpass-22.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665711548
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1665711548
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kpkpass
cp %{_builddir}/kpkpass-%{version}/.codespellrc.license %{buildroot}/usr/share/package-licenses/kpkpass/c011fda7746c087a127999da1c4044854ee42238 || :
cp %{_builddir}/kpkpass-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kpkpass/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9 || :
cp %{_builddir}/kpkpass-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kpkpass/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kpkpass-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kpkpass/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/kpkpass-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kpkpass/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kpkpass-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kpkpass-%{version}/autotests/data/boardingpass-v1.pkpass.license %{buildroot}/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kpkpass-%{version}/autotests/data/boardingpass-v2.pkpass.license %{buildroot}/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d || :
cp %{_builddir}/kpkpass-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/kpkpass/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
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
/usr/include/KPim/KPkPass/kpkpass_version.h
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
/usr/lib64/libKPimPkPass.so.5.21.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kpkpass/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kpkpass/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/kpkpass/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/kpkpass/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kpkpass/c011fda7746c087a127999da1c4044854ee42238
/usr/share/package-licenses/kpkpass/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/kpkpass/fca67987925d2ed70e898f6dd9c7fe4b458d416d
