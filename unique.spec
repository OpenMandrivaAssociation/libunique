%define major 		0
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Summary: 	Library for creating single instance applications
Name: 		unique
Version: 	1.0.6
Release:	%mkrel 1
URL: 		http://live.gnome.org/LibUnique
License: 	LGPLv2+
Group: 		System/Libraries
Source0: 	http://www.gnome.org/~ebassi/source/%{name}-%{version}.tar.gz
Patch0:		unique-1.0.6-fix-str-fmt.patch
Buildroot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	dbus-glib-devel >= 0.70
BuildRequires:	gtk+2-devel >= 2.11.0
BuildRequires:	glib2-devel >= 2.12.0
BuildRequires:	gtk-doc

%description
Unique is a library for creating single instance applications.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for creating single instance applications

%description -n %{libname}
Unique is a library for creating single instance applications.

%package -n %{develname}
Group:		Development/C
Summary:	Header files for development with %name
Provides:	%{name}-devel = %{version}
Requires:	%{libname} = %{version}

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
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib%{name}*.so.%{major}*

%files -n %{develname}
%doc AUTHORS
%docdir %{_datadir}/gtk-doc/html/%{name}
%doc %{_datadir}/gtk-doc/html/%{name}/*
%defattr(-,root,root)
%{_libdir}/lib%{name}*.so
%{_libdir}/lib%{name}*.*a
%{_libdir}/pkgconfig/%{name}*.pc
%{_includedir}/%{name}-*

