#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kscreenlocker
Version  : 5.27.3
Release  : 83
URL      : https://download.kde.org/stable/plasma/5.27.3/kscreenlocker-5.27.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.27.3/kscreenlocker-5.27.3.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.27.3/kscreenlocker-5.27.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: kscreenlocker-data = %{version}-%{release}
Requires: kscreenlocker-lib = %{version}-%{release}
Requires: kscreenlocker-license = %{version}-%{release}
Requires: kscreenlocker-locales = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules wayland
BuildRequires : extra-cmake-modules-data
BuildRequires : kglobalaccel-dev
BuildRequires : kidletime-dev
BuildRequires : kwayland-dev
BuildRequires : layer-shell-qt-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libkscreen-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : systemd-dev
BuildRequires : xcb-util-keysyms-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
kscreenlocker can be configured to support the PAM ("Pluggable Authentication
Modules") system for password checking (for unlocking the display).

%package data
Summary: data components for the kscreenlocker package.
Group: Data

%description data
data components for the kscreenlocker package.


%package dev
Summary: dev components for the kscreenlocker package.
Group: Development
Requires: kscreenlocker-lib = %{version}-%{release}
Requires: kscreenlocker-data = %{version}-%{release}
Provides: kscreenlocker-devel = %{version}-%{release}
Requires: kscreenlocker = %{version}-%{release}

%description dev
dev components for the kscreenlocker package.


%package lib
Summary: lib components for the kscreenlocker package.
Group: Libraries
Requires: kscreenlocker-data = %{version}-%{release}
Requires: kscreenlocker-license = %{version}-%{release}

%description lib
lib components for the kscreenlocker package.


%package license
Summary: license components for the kscreenlocker package.
Group: Default

%description license
license components for the kscreenlocker package.


%package locales
Summary: locales components for the kscreenlocker package.
Group: Default

%description locales
locales components for the kscreenlocker package.


%prep
%setup -q -n kscreenlocker-5.27.3
cd %{_builddir}/kscreenlocker-5.27.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679508109
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1679508109
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kscreenlocker
cp %{_builddir}/kscreenlocker-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kscreenlocker/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kscreenlocker-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kscreenlocker/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build
%make_install
popd
%find_lang kcm_screenlocker
%find_lang kscreenlocker
%find_lang kscreenlocker_greet

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kscreenlocker_greet

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_screenlocker.desktop
/usr/share/dbus-1/interfaces/kf5_org.freedesktop.ScreenSaver.xml
/usr/share/dbus-1/interfaces/org.kde.screensaver.xml
/usr/share/kconf_update/kscreenlocker.upd
/usr/share/kconf_update/ksreenlocker_5_3_separate_autologin.pl
/usr/share/knotifications5/ksmserver.notifyrc
/usr/share/kpackage/kcms/kcm_screenlocker/contents/ui/Appearance.qml
/usr/share/kpackage/kcms/kcm_screenlocker/contents/ui/LnfConfig.qml
/usr/share/kpackage/kcms/kcm_screenlocker/contents/ui/WallpaperConfig.qml
/usr/share/kpackage/kcms/kcm_screenlocker/contents/ui/main.qml
/usr/share/ksmserver/screenlocker/org.kde.passworddialog/metadata.desktop
/usr/share/qlogging-categories5/kscreenlocker.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KScreenLocker/KScreenLocker/KsldApp
/usr/include/KScreenLocker/KScreenLocker/kscreenlocker_export.h
/usr/include/KScreenLocker/KScreenLocker/ksldapp.h
/usr/lib64/cmake/KScreenLocker/KScreenLockerConfig.cmake
/usr/lib64/cmake/KScreenLocker/KScreenLockerConfigVersion.cmake
/usr/lib64/cmake/KScreenLocker/KScreenLockerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KScreenLocker/KScreenLockerTargets.cmake
/usr/lib64/cmake/ScreenSaverDBusInterface/ScreenSaverDBusInterfaceConfig.cmake
/usr/lib64/libKScreenLocker.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKScreenLocker.so.5
/usr/lib64/libKScreenLocker.so.5.27.3
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings/kcm_screenlocker.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kscreenlocker/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/kscreenlocker/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/kscreenlocker/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kscreenlocker/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kscreenlocker/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kscreenlocker/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/kscreenlocker/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kscreenlocker/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kscreenlocker/e458941548e0864907e654fa2e192844ae90fc32

%files locales -f kcm_screenlocker.lang -f kscreenlocker.lang -f kscreenlocker_greet.lang
%defattr(-,root,root,-)

