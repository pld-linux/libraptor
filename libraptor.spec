Summary:	Raptor RDF Parser Toolkit
Summary(pl):	Raptor - zestaw narzêdzi do analizy RDF
Name:		libraptor
# the real name is raptor, but it conflicts with already existing raptor game
%define	rname	raptor
Version:	1.4.14
Release:	2
License:	LGPL v2.1+ or GPL v2+ or Apache v2.0+
Group:		Libraries
Source0:	http://download.librdf.org/source/%{rname}-%{version}.tar.gz
# Source0-md5:	1bbc9938f8f7310e20fbd5b962a43847
URL:		http://librdf.org/raptor/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.7
# WWW library can be one of: curl(default),xml,libfetch,libwww,none
BuildRequires:	curl-devel
# XML library can be libxml or expat; grddl parser requires libxml2+libxslt anyway
BuildRequires:	libxml2-devel >= 2.6.8
BuildRequires:	libxslt-devel >= 1.0.18
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.98
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
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel
Requires:	libxml2-devel >= 2.6.8
Requires:	libxslt-devel >= 1.0.18

%description devel
libraptor library header files.

%description devel -l pl
Pliki nag³ówkowe biblioteki libraptor.

%package static
Summary:	Static libraptor library
Summary(pl):	Statyczna biblioteka libraptor
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraptor library.

%description static -l pl
Statyczna biblioteka libraptor.

%package rapper
Summary:	Raptor RDF parser test program
Summary(pl):	Testowy program parsera Raptor RDF
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Obsoletes:	redland-rapper

%description rapper
Raptor RDF parser test program.

%description rapper -l pl
Testowy program parsera Raptor RDF.

%prep
%setup -q -n %{rname}-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
# avoid -s in LDFLAGS, `raptor-config --libs` would print it
# (note: don't pass empty LDFLAGS - it would be overridden)
LDFLAGS="`echo %{rpmldflags} | sed -e 's/\(^\| \)-s\>/ /'`"
# avoid using parsedate from libinn, use curl_getdate instead
%configure \
	ac_cv_header_libinn_h=no \
	--enable-release \
	--with-html-dir=%{_gtkdocdir}
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
%{_gtkdocdir}/raptor

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files rapper
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rapper
%{_mandir}/man1/rapper.1*
