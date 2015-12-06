#
# Conditional build:
%bcond_with	tests	# make check (requires BES server)
#
Summary:	GDAL data handler module for the OPeNDAP data server
Summary(pl.UTF-8):	Moduł obsługujący dane GDAL dla serwera danych OPeNDAP
Name:		opendap-gdal_handler
Version:	0.9.4
Release:	3
License:	LGPL v2.1+
Group:		Daemons
Source0:	http://www.opendap.org/pub/source/gdal_handler-%{version}.tar.gz
# Source0-md5:	746669e2cf0dee72bd76d9d70a4c2d08
URL:		http://opendap.org/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
%{?with_tests:BuildRequires:	bes >= 3.13.0}
BuildRequires:	bes-devel >= 3.13.0
BuildRequires:	gdal-devel >= 1.10
BuildRequires:	libdap-devel >= 3.13.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
Requires:	bes >= 3.13.0
Requires:	gdal >= 1.10
Requires:	libdap >= 3.13.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GDAL data handler module for the OPeNDAP data server. It
should be able to serve any file that can be read using the GDAL
library.

%description -l pl.UTF-8
Ten pakiet zawiera moduł obsługujący dane GDAL dla serwera danych
OPeNDAP. Powinien być w stanie zaserwować dowolny plik, który można
odczytać przy użyciu biblioteki GDAL.

%prep
%setup -q -n gdal_handler-%{version}

%build
# rebuild autotools for -as-needed to work
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/bes/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bes/modules/gdal.conf
%attr(755,root,root) %{_libdir}/bes/libgdal_module.so
%dir %{_datadir}/hyrax/data/gdal
%{_datadir}/hyrax/data/gdal/*.bz2
%{_datadir}/hyrax/data/gdal/*.jp2
%{_datadir}/hyrax/data/gdal/*.jpg
%{_datadir}/hyrax/data/gdal/*.lgo
%{_datadir}/hyrax/data/gdal/*.tif
%{_datadir}/hyrax/data/gdal/*.TIF
%{_datadir}/hyrax/data/gdal/*.txt
%doc %{_datadir}/hyrax/data/gdal/README
