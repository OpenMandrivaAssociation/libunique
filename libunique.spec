%define major 		0
%define api 1.0
%define libname		%mklibname unique %major
%define develname	%mklibname unique -d

Summary: 	Library for creating single instance applications
Name: 		libunique
Version: 	1.1.6
Release:	%mkrel 2
URL: 		http://live.gnome.org/LibUnique
License: 	LGPLv2+
Group: 		System/Libraries
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch0:		unique-1.0.6-fix-str-fmt.patch
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gtk+2-devel >= 2.11.0
BuildRequires:	glib2-devel >= 2.12.0
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc

%description
Unique is a library for creating single instance applications.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for creating single instance applications
Conflicts: gir-repository < 0.6.5-3

%description -n %{libname}
Unique is a library for creating single instance applications.

%package -n %{develname}
Group:		Development/C
Summary:	Header files for development with %name
Provides:	unique-devel = %{version}
Requires:	%{libname} = %{version}
Conflicts: gir-repository < 0.6.5-3

%description -n %{develname}
Unique is a library for creating single instance applications.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libunique-%api.so.%{major}*
%_libdir/girepository-1.0/Unique-%{api}.typelib

%files -n %{develname}
%doc AUTHORS
%docdir %{_datadir}/gtk-doc/html/unique
%doc %{_datadir}/gtk-doc/html/unique/*
%defattr(-,root,root)
%{_libdir}/libunique-%api.so
%{_libdir}/libunique-%api.*a
%{_libdir}/pkgconfig/unique-%api.pc
%{_includedir}/unique-%api
%_datadir/gir-1.0/Unique-%api.gir
