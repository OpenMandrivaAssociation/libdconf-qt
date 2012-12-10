%define major 0
%define libname %mklibname dconf-qt %{major}
%define develname %mklibname dconf-qt -d

%define gitver 110722

Summary:	QML plugin and Qt bindings for dconf
Name:		libdconf-qt
Version:	0.0.0
Release:	0.%{gitver}.1
License:	GPLv3,LGPLv3
Url:		http://launchat.net/dconf-qt
Group:		System/Libraries
Source0:	%{name}-%{version}.%{gitver}.tar.bz2
# PATCH-FIX-UPSTREAM 01_fix_pc_generation.patch - fix .pc generation, taken from Ubuntu release
Patch0: 01_fix_pc_generation.patch
# PATCH-FIX-UPSTREAM 02_link_again_dconf_dbus.patch - link again dconf dbus, taken from Ubuntu
Patch1: 02_link_again_dconf_dbus.patch
# PATCH-FEATURE-OPENSUSE ugly-cmake-hack.patch - cmake carnage to 'use' libdir
Patch2: ugly-cmake-hack.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(QtDeclarative)
BuildRequires:	pkgconfig(dconf-dbus-1)
BuildRequires:	pkgconfig(glib-2.0)

%description
Qt bindings and QML plugin for dconf.

%package -n %{libname}
Summary:	QML plugin and Qt bindings for dconf
Group:		System/Libraries

%description -n %{libname}
Qt bindings and QML plugin for dconf - system shared libraries.

%package -n %{develname}
Summary:	QML plugin and Qt bindings for dconf
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Qt bindings and QML plugin for dconf - development files.

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

%files -n %{libname}
%doc COPYING-GPL3 COPYING-LGPL3
%{_libdir}/*.so.%{major}*
%{_libdir}/qt4/plugins/imports/

%files -n %{develname}
%{_includedir}/dconf-qt/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc



%changelog
* Tue Jan 24 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.0.0-0.110722.1
+ Revision: 767453
- imported package libdconf-qt


* Sun Oct 16 2011 nmarques@opensuse.org
- Fix licenses
* Sun Oct 16 2011 nmarques@opensuse.org
- Initial package taken from Ubuntu Oneiric release, no official
  release.
- 01_fix_pc_generation.patch: fix .pc generation, taken from
  Ubuntu release.
- 02_link_again_dconf_dbus.patch: link again to dconf dbus, taken
  from Ubuntu release.
- ugly-cmake-hack.patch: force libdir.
