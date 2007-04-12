%define name gsf-sharp
%define version 0.8.1
%define release %mkrel 1

Summary: GSF C# bindings for mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Development/Other
Url: http://www.go-mono.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildRequires: libgsf-devel >= 1.11.0
BuildRequires: gtk-sharp2
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

