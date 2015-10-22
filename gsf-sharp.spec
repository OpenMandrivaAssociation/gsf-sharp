%define _disable_lto 1

Summary:	GSF C sharp bindings for mono
Name:		gsf-sharp
Version:	0.8.1
Release:	18
License:	LGPLv2+
Group:		Development/Other
Url:		http://www.go-mono.com
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	monodoc
BuildRequires:	pkgconfig(gapi-2.0)
BuildRequires:	pkgconfig(gtk-sharp-2.0)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(mono)

%description
GSF# bindings for mono. Useful for reading and writing structured
files (eg MS OLE and Zip).

%package devel
Summary:	The pkgconfig for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
The pkgconfig for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/mono/gac/%{name}
%{_prefix}/lib/mono/gtk-sharp/%{name}.dll*
%{_libdir}/libgsfglue.so
%{_datadir}/gapi-2.0/gsf-api.xml

%files devel
%{_libdir}/pkgconfig/%{name}.pc
