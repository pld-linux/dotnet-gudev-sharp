#
#
Summary:	.NET bindings for udev-glib
Summary(pl.UTF-8):	Wiązania udev-glib dla .NET
Name:		dotnet-gudev-sharp
Version:	0.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	gudev-sharp-%{version}.tar.gz
# Source0-md5:	403822d81683ebe2c2a0ce5287f78631
Patch0:		%{name}-monodir.patch
URL:		http://github.com/mono/gudev-sharp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	mono-csharp >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	udev-glib-devel >= 146
Requires:	udev-glib >= 146
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to udev-glib library.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do biblioteki udev-glib.

%package devel
Summary:	GUdev# development files
Summary(pl.UTF-8):	Pliki programistyczne GUdev#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel

%description devel
GUdev# development files.

%description devel -l pl.UTF-8
Pliki programistyczne GUdev#.

%prep
%setup -q -n mono-gudev-sharp-3867909/
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/mono/gac/gudev-sharp

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/gudev-sharp-1.0
%{_prefix}/lib/mono/gudev-sharp-1.0/gudev-sharp.dll
%{_pkgconfigdir}/gudev-sharp-1.0.pc
