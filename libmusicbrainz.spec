Summary:	A software library for accesing MusicBrainz servers
Summary(pl):	Biblioteka umo�liwiaj�ca korzystanie z serwer�w MusicBrainz
Name:		libmusicbrainz
Version:	2.0.1
Release:	1
Epoch:		1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.musicbrainz.org/pub/musicbrainz/%{name}-%{version}.tar.gz
URL:		http://www.musicbrainz.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	musicbrainz
Provides:		musicbrainz

%description
The MusicBrainz client library allows applications to make metadata
lookup to a MusicBrainz server, generate signatures from WAV data and
create CD Index Disk ids from audio CD roms.

%description -l pl
Biblioteka kliencka MusicBrainz pozwala aplikacjom na wysy�anie
zapyta� do serwer�w MusicBrainz, generowanie sygnatur z plik�w WAV
oraz tworzenie indeks�w z p�yt CD audio.

%package devel
Summary:	Headers for developing programs that will use libmusicbrainz
Summary(pl):	Pliki nag��wkowe do rozwijania program�w u�ywaj�cych libmusicbrainz
Group:		Development/Libraries
Requires:	%{name} = %{version}
Provides:	musicbrainz-devel
Obsoletes:	musicbrainz-devel

%description devel
This package contains the headers that programmers will need to
develop applications which will use libmusicbrainz.

%description devel -l pl
Pliki nag��wkowe potrzebne programistom do rozwijania aplikacji
u�ywaj�cych biblioteki libmusicbrainz

%package static
Summary:	Static libmusicbrainz libraries
Summary(pl):	Biblioteki statyczne libmusicbrainz
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	musicbrainz-static

%description static
Static libmusicbrainz libraries.

%description static -l pl
Staryczne biblioteki libmusicbrainz.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pkgconfigdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
