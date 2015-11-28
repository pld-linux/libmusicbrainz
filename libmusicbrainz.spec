Summary:	A software library for accesing MusicBrainz servers
Summary(pl.UTF-8):	Biblioteka umożliwiająca korzystanie z serwerów MusicBrainz
Name:		libmusicbrainz
Version:	2.1.5
Release:	6
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.musicbrainz.org/pub/musicbrainz/%{name}-%{version}.tar.gz
# Source0-md5:	d5e19bb77edd6ea798ce206bd05ccc5f
Patch0:		%{name}-gcc43.patch
URL:		http://www.musicbrainz.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	python-devel
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
Provides:	musicbrainz
Obsoletes:	musicbrainz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%description -l pl.UTF-8
Biblioteka kliencka MusicBrainz pozwala aplikacjom na wysyłanie
zapytań do serwerów MusicBrainz, generowanie sygnatur z plików WAV
oraz tworzenie indeksów z płyt CD audio.

%package devel
Summary:	Headers for developing programs that will use libmusicbrainz
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania programów używających libmusicbrainz
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	expat-devel
Requires:	libstdc++-devel
Provides:	musicbrainz-devel
Obsoletes:	musicbrainz-devel

%description devel
This package contains the headers that programmers will need to
develop applications which will use libmusicbrainz.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne programistom do rozwijania aplikacji
używających biblioteki libmusicbrainz.

%package static
Summary:	Static libmusicbrainz libraries
Summary(pl.UTF-8):	Biblioteki statyczne libmusicbrainz
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	musicbrainz-static

%description static
Static libmusicbrainz libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libmusicbrainz.

%package -n python-musicbrainz
Summary:	Python bindings for libmusicbrainz
Summary(pl.UTF-8):	Wiązania Pythona do libmusicbrainz
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
%pyrequires_eq	python-libs

%description -n python-musicbrainz
Python bindings for libmusicbrainz.

%description -n python-musicbrainz -l pl.UTF-8
Wiązania Pythona do libmusicbrainz.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

cd python
LD_LIBRARY_PATH=../lib/.libs python setup.py build
cd ..

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd python
LD_LIBRARY_PATH=../lib/.libs python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2
cd ..

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/libmusicbrainz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmusicbrainz.so.4

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libmusicbrainz.so
%{_libdir}/libmusicbrainz.la
%{_includedir}/musicbrainz
%{_pkgconfigdir}/libmusicbrainz.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmusicbrainz.a

%files -n python-musicbrainz
%defattr(644,root,root,755)
%{py_sitescriptdir}/musicbrainz.py[co]
%{py_sitescriptdir}/python_musicbrainz-*.egg-info
