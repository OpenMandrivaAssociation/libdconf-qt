%define major 0
%define libname %mklibname dconf-qt %{major}
%define devname %mklibname dconf-qt -d

%define gitver 110722

Summary:	QML plugin and Qt bindings for dconf
Name:		libdconf-qt
Version:	0.0.0
Release:	0.%{gitver}.2
License:	LGPLv3+
Group:		System/Libraries
Url:		http://launchat.net/dconf-qt
Source0:	%{name}-%{version}.%{gitver}.tar.bz2
# PATCH-FIX-UPSTREAM 01_fix_pc_generation.patch - fix .pc generation, taken from Ubuntu release
Patch0:		01_fix_pc_generation.patch
# PATCH-FIX-UPSTREAM 02_link_again_dconf_dbus.patch - link again dconf dbus, taken from Ubuntu
Patch1:		02_link_again_dconf_dbus.patch
# PATCH-FEATURE-OPENSUSE ugly-cmake-hack.patch - cmake carnage to 'use' libdir
Patch2:		ugly-cmake-hack.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtDeclarative)
BuildRequires:	pkgconfig(dconf-dbus-1)
BuildRequires:	pkgconfig(glib-2.0)

%description
Qt bindings and QML plugin for dconf.

%files
%{_qt_importdir}/QConf

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	QML plugin and Qt bindings for dconf
Group:		System/Libraries
Suggests:	%{name}

%description -n %{libname}
Qt bindings and QML plugin for dconf - system shared libraries.

%files -n %{libname}
%doc COPYING-GPL3 COPYING-LGPL3
%{_libdir}/libdconf-qt.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	QML plugin and Qt bindings for dconf
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Qt bindings and QML plugin for dconf - development files.

%files -n %{devname}
%{_includedir}/dconf-qt/
%{_libdir}/libdconf-qt.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
export BUILD_GLOBAL=true
%cmake \
	-Dlibdir=%{_libdir} \

%make

%install
%makeinstall_std -C build

mkdir -p %{buildroot}%{_qt_importdir}
mv %{buildroot}%{_libdir}/qt4/plugins/imports/* %{buildroot}%{_qt_importdir}/

