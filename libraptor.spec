Summary:	-
Summary(pl):	-
Name:		libraptor
# the real name is raptor, but it conflicts with already existing raptor game
%define	rname	raptor
Version:	0.9.10
Release:	1
License:	LGPL or GPL or MPL
Group:		Libraries
Source0:	http://www.redland.opensource.ac.uk/dist/source/%{rname}-%{version}.tar.gz
URL:		http://www.redland.opensource.ac.uk/raptor/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package devel
Summary:	-
Summary(pl):	-
Group:		Development/Libraries

%description devel

%package static
Summary:	-
Summary(pl):	-
Group:		Development/Libraries

%description static

%prep
%setup -q -n %{rname}-%{version}

%build
%configure
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

%files devel
%defattr(644,root,root,755)

%files static
%defattr(644,root,root,755)
