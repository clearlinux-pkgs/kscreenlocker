#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kscreenlocker
Version  : 5.18.1
Release  : 34
URL      : https://github.com/KDE/kscreenlocker/archive/v5.18.1/kscreenlocker-5.18.1.tar.gz
Source0  : https://github.com/KDE/kscreenlocker/archive/v5.18.1/kscreenlocker-5.18.1.tar.gz
Summary  : Library and components for secure lock screen architecture
Group    : Development/Tools
License  : GPL-2.0
Requires: kscreenlocker-data = %{version}-%{release}
Requires: kscreenlocker-lib = %{version}-%{release}
Requires: kscreenlocker-license = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules wayland
BuildRequires : kglobalaccel-dev
BuildRequires : kidletime-dev
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libseccomp)
BuildRequires : qtbase-dev mesa-dev
BuildRequires : systemd-dev
BuildRequires : xcb-util-keysyms-dev

%description
The KCheckPass authentication software:
-----------------------------------------

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


%prep
%setup -q -n kscreenlocker-5.18.1
cd %{_builddir}/kscreenlocker-5.18.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582079057
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1582079057
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kscreenlocker
cp %{_builddir}/kscreenlocker-5.18.1/COPYING %{buildroot}/usr/share/package-licenses/kscreenlocker/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/kcheckpass
/usr/lib64/libexec/kscreenlocker_greet

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.freedesktop.ScreenSaver.xml
/usr/share/dbus-1/interfaces/org.kde.screensaver.xml
/usr/share/kconf_update/kscreenlocker.upd
/usr/share/kconf_update/ksreenlocker_5_3_separate_autologin.pl
/usr/share/knotifications5/ksmserver.notifyrc
/usr/share/kservices5/screenlocker.desktop
/usr/share/ksmserver/screenlocker/org.kde.passworddialog/metadata.desktop

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
/usr/lib64/libKScreenLocker.so.5.18.1
/usr/lib64/qt5/plugins/screenlocker_kcm.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kscreenlocker/4cc77b90af91e615a64ae04893fdffa7939db84c
