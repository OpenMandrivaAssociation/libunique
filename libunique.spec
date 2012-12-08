%define major 		0
%define api 1.0
%define libname		%mklibname unique %major
%define develname	%mklibname unique -d

Summary: 	Library for creating single instance applications
Name: 		libunique
Version: 	1.1.6
Release:	7
URL: 		http://live.gnome.org/LibUnique
License: 	LGPLv2+
Group: 		System/Libraries
Source0: 	http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch0:		unique-1.0.6-fix-str-fmt.patch

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

# this is a hack for glib2.0 >= 2.31.0
sed -i -e 's/-DG_DISABLE_DEPRECATED//g' \
	./unique/Makefile.*

%build
%configure2_5x \
	--disable-static \
	--enable-maintainer-flags=no

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%files -n %{libname}
%{_libdir}/libunique-%api.so.%{major}*
%_libdir/girepository-1.0/Unique-%{api}.typelib

%files -n %{develname}
%doc AUTHORS
%docdir %{_datadir}/gtk-doc/html/unique
%doc %{_datadir}/gtk-doc/html/unique/*
%{_libdir}/libunique-%api.so
%{_libdir}/pkgconfig/unique-%api.pc
%{_includedir}/unique-%api
%_datadir/gir-1.0/Unique-%api.gir


%changelog
* Sat Dec 03 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.6-7
+ Revision: 737383
- put the cart before the horse oops
- rebuild
- removed .la files this time

* Mon Nov 28 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.6-6
+ Revision: 735153
- added glib2.0 2.31.0 deprecated workaround
- rebuild
- cleaned up spec
- disabled static
- removed old ldconfig scriptlets
- removed mkrel & BuildRoot
- removed defattr

* Wed Sep 28 2011 Götz Waschk <waschk@mandriva.org> 1.1.6-5
+ Revision: 701695
- rebuild for new libpng

* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 1.1.6-4
+ Revision: 660666
- disable strict flags

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sun Sep 12 2010 Götz Waschk <waschk@mandriva.org> 1.1.6-3mdv2011.0
+ Revision: 577678
- rebuild for new g-i

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 1.1.6-2mdv2011.0
+ Revision: 563406
- rebuild for new gobject-introspection

  + Götz Waschk <waschk@mandriva.org>
    - add conflict with older gir-repository (bug #55583)

* Thu Nov 12 2009 Götz Waschk <waschk@mandriva.org> 1.1.6-1mdv2010.1
+ Revision: 465324
- update to new version 1.1.6

* Thu Nov 12 2009 Götz Waschk <waschk@mandriva.org> 1.1.4-1mdv2010.1
+ Revision: 465206
- update build deps
- new version
- add gobject introspection support

* Tue Aug 25 2009 Götz Waschk <waschk@mandriva.org> 1.1.2-1mdv2010.0
+ Revision: 420755
- update to new version 1.1.2

* Sun Mar 22 2009 Götz Waschk <waschk@mandriva.org> 1.0.8-1mdv2009.1
+ Revision: 360241
- new version
- fix source URL
- spec file fixes
- rename from unique

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 1.0.6-1mdv2009.1
+ Revision: 336473
- New version 1.0.6

* Mon Nov 24 2008 Götz Waschk <waschk@mandriva.org> 1.0.4-1mdv2009.1
+ Revision: 306202
- new version
- drop patch

* Sat Sep 06 2008 Adam Williamson <awilliamson@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 281896
- buildrequires gtk-doc, it seems
- %%{buildroot} not $RPM_BUILD_ROOT
- need to do autoreconf after patching configure.ac
- add underlink.patch (fixes an underlinking problem)
- new release 1.0.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Sep 07 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.3-1mdv2008.0
+ Revision: 81367
- add glib and gtk+ buildrequires
- Import unique

