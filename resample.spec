Summary:	Free sampling-rate conversion and filter design utilities
Summary(pl):	Wolnodostêpne narzêdzia do zmiany czêstotliwo¶ci próbkowania i filtrowania
Name:		resample
Version:	1.8.1
Release:	1
License:	LGPL
Group:		Libraries
#Source0Download: http://www-ccrma.stanford.edu/~jos/resample/Free_Resampling_Software.html
Source0:	http://ccrma.stanford.edu/~jos/resample/%{name}-%{version}.tar.gz
# Source0-md5:	c3c1c64e4bb9b0bdc6062b8ad619aef1
URL:		http://www-ccrma.stanford.edu/~jos/resample/
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free sampling-rate conversion and filter design utilities.

%description -l pl
Wolnodostêpne narzêdzia do zmiany czêstotliwo¶ci próbkowania i
filtrowania.

%prep
%setup -q

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/resample
%attr(755,root,root) %{_bindir}/windowfilter
%{_mandir}/man1/resample.1*
%{_mandir}/man1/windowfilter.1*
