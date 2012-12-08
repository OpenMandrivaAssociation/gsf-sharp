%define name gsf-sharp
%define version 0.8.1
%define release %mkrel 9

Summary: GSF C# bindings for mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: LGPLv2+
Group: Development/Other
Url: http://www.go-mono.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: libgsf-devel >= 1.11.0
BuildRequires: gtk-sharp2
BuildRequires: gtk-sharp2-devel
BuildRequires: monodoc

%description
GSF# bindings for mono. Useful for reading and writing structured
files (eg MS OLE and Zip).

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
perl -pi -e "s^%_libdir^%_prefix/lib^" %buildroot%_libdir/pkgconfig/*.pc
rm -f %buildroot%_libdir/libgsf*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%_prefix/lib/mono/gac/%name
%_prefix/lib/mono/gtk-sharp/%name.dll*
%_libdir/pkgconfig/%name.pc
%_libdir/libgsfglue.so
%_datadir/gapi-2.0/gsf-api.xml



%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-7mdv2011.0
+ Revision: 664928
- mass rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-6mdv2011.0
+ Revision: 522766
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8.1-5mdv2010.0
+ Revision: 425045
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.8.1-4mdv2009.1
+ Revision: 351228
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.8.1-3mdv2009.0
+ Revision: 221103
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Nov 04 2007 Adam Williamson <awilliamson@mandriva.org> 0.8.1-2mdv2008.1
+ Revision: 105673
- buildrequires gtk-sharp2-devel
- rebuild for 2008
- new license policy, correct license


* Wed Jan 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.1-1mdv2007.0
+ Revision: 103535
- Import gsf-sharp

* Wed Jan 03 2007 Götz Waschk <waschk@mandriva.org> 0.8.1-1mdv2007.1
- new version

* Fri Jul 07 2006 Götz Waschk <waschk@mandriva.org> 0.8-0.62317.1mdv2007.0
- drop patch
- new snapshot

* Thu Mar 02 2006 Götz Waschk <waschk@mandriva.org> 0.7-0.57499.1mdk
- build with libgsf 1.14.0
- new snapshot

* Fri Jan 13 2006 Götz Waschk <waschk@mandriva.org> 0.7-0.53936.2mdk
- fix build on x86_64

* Mon Dec 05 2005 Götz Waschk <waschk@mandriva.org> 0.7-0.53936.1mdk
- drop patch
- new version

* Wed Oct 12 2005 Götz Waschk <waschk@mandriva.org> 0.4-0.50131.2mdk
- patch for new libgsf

* Sat Oct 08 2005 Götz Waschk <waschk@mandriva.org> 0.4-0.50131.1mdk
- gtk-sharp2
- new version

* Tue May 03 2005 Götz Waschk <waschk@mandriva.org> 0.3-0.43876.1mdk
- fix pkgconfig for x86_64
- new snapshot

* Tue May 03 2005 Götz Waschk <waschk@mandriva.org> 0.3-0.43326.2mdk
- directory fix for x86_64

* Thu Apr 21 2005 Götz Waschk <waschk@mandriva.org> 0.3-0.43326.1mdk
- new version

* Fri Jan 21 2005 Götz Waschk <waschk@linux-mandrake.com> 0-0.39304.1mdk
- initial package

