Summary:	Raptor RDF Parser Toolkit
Summary(pl):	Raptor - zestaw narzêdzi do analizy RDF
Name:		libraptor
# the real name is raptor, but it conflicts with already existing raptor game
%define	rname	raptor
Version:	0.9.11
Release:	1
License:	LGPL or GPL or MPL
Group:		Libraries
Source0:	http://www.redland.opensource.ac.uk/dist/source/%{rname}-%{version}.tar.gz
# Source0-md5:	3ccb466690e126a01ddfe5fb759d01f7
URL:		http://www.redland.opensource.ac.uk/raptor/
# WWW library can be one of: curl(default),xml,libwww,none
BuildRequires:	curl-devel
# XML library can be libxml or expat
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Raptor is the RDF Parser Toolkit for Redland written in C consisting
of two parsers for the RDF/XML and N-Triples syntaxes for RDF. Raptor
is designed to work efficiently when used with Redland but is entirely
separate.

%description -l pl
Raptor to zestaw narzêdzi do analizy RDF dla Redland napisany w C,
sk³adaj±cy siê z dwóch analizatorów dla sk³adni RDF/XML i N-Triplets
dla RDF. Raptor zosta³ zaprojektowany, by pracowaæ wydajnie, je¶li
jest u¿ywany z Redland, ale jest ca³kowicie oddzielny.

%package devel
Summary:	libraptor library header files
Summary(pl):	Pliki nag³ówkowe biblioteki libraptor
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	curl-devel
Requires:	libxml2-devel

%description devel
libraptor library header files.

%description devel -l pl
Pliki nag³ówkowe biblioteki libraptor.

%package static
Summary:	Static libraptor library
Summary(pl):	Statyczna biblioteka libraptor
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraptor library.

%description static -l pl
Statyczna biblioteka libraptor.

%package rapper
Summary:	Raptor RDF parser test program without Redland RDF support
Summary(pl):	Testowy program parsera Raptor RDF bez wsparcia dla Redland RDF
Group:		Applications
Requires:	%{name} = %{version}

%description rapper
Raptor RDF parser test program without Redland RDF support.

%description rapper -l pl
Testowy program parsera Raptor RDF bez wsparcia dla Redland RDF.

%prep
%setup -q -n %{rname}-%{version}

%build
%configure \
	--enable-release
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.txt NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/raptor-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man1/raptor-config.1*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files rapper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rapper
%{_mandir}/man1/rapper.1*
