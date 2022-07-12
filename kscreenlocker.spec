#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kscreenlocker
Version  : 5.25.3
Release  : 70
URL      : https://download.kde.org/stable/plasma/5.25.3/kscreenlocker-5.25.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.25.3/kscreenlocker-5.25.3.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.25.3/kscreenlocker-5.25.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
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
BuildRequires : ki18n-dev
BuildRequires : kidletime-dev
BuildRequires : kwayland-dev
BuildRequires : layer-shell-qt-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : systemd-dev
BuildRequires : xcb-util-keysyms-dev

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
%setup -q -n kscreenlocker-5.25.3
cd %{_builddir}/kscreenlocker-5.25.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657634751
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
export SOURCE_DATE_EPOCH=1657634751
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kscreenlocker
cp %{_builddir}/kscreenlocker-5.25.3/COPYING %{buildroot}/usr/share/package-licenses/kscreenlocker/4cc77b90af91e615a64ae04893fdffa7939db84c
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
/usr/lib64/libKScreenLocker.so.5.25.3
/usr/lib64/qt5/plugins/plasma/kcms/systemsettings/kcm_screenlocker.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kscreenlocker/4cc77b90af91e615a64ae04893fdffa7939db84c

%files locales -f kcm_screenlocker.lang -f kscreenlocker.lang -f kscreenlocker_greet.lang
%defattr(-,root,root,-)

