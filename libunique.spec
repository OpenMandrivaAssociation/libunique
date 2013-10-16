%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.0
%define major	0
%define libname	%mklibname unique %{api} %{major}
%define girname	%mklibname unique-gir %{api}
%define devname	%mklibname unique -d

Summary: 	Library for creating single instance applications
Name: 		libunique
Version: 	1.1.6
Release:	11
Url: 		http://live.gnome.org/LibUnique
License: 	LGPLv2+
Group: 		System/Libraries
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/libunique/%{url_ver}/%{name}-%{version}.tar.bz2
Patch0:		unique-1.0.6-fix-str-fmt.patch

BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
Unique is a library for creating single instance applications.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for creating single instance applications

%description -n %{libname}
Unique is a library for creating single instance applications.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{libname} < 1.1.6-9

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Header files for development with %{name}
Provides:	unique-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
This package includes the developement files for %{name}.

%prep
%setup -q
%patch0 -p0

# this is a hack for glib2.0 >= 2.31.0
sed -i -e 's/-DG_DISABLE_DEPRECATED//g' \
	./unique/Makefile.*

%build
%configure2_5x \
	--disable-static \
	--enable-maintainer-flags=no

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libunique-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Unique-%{api}.typelib

%files -n %{devname}
%doc AUTHORS
%docdir %{_datadir}/gtk-doc/html/unique
%doc %{_datadir}/gtk-doc/html/unique/*
%{_libdir}/libunique-%{api}.so
%{_libdir}/pkgconfig/unique-%{api}.pc
%{_includedir}/unique-%{api}
%{_datadir}/gir-1.0/Unique-%{api}.gir

