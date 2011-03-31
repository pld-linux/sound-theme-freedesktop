Summary:	freedesktop.org sound theme
Name:		sound-theme-freedesktop
Version:	0.7
Release:	1
Group:		Themes
Source0:	http://people.freedesktop.org/~mccann/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	7bcad4fa54570f80c612012bce66f60f
License:	GPLv2+ and LGPLv2+ and CC-BY-SA and CC-BY
URL:		http://freedesktop.org/wiki/Specifications/sound-theme-spec
# For details on the licenses used, see README
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.40.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The default freedesktop.org sound theme following the XDG theming
specification (http://0pointer.de/public/sound-theme-spec.html).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/sounds/freedesktop

%postun
touch --no-create %{_datadir}/sounds/freedesktop

%files
%defattr(644,root,root,755)
%doc README
%dir %{_datadir}/sounds/freedesktop
%dir %{_datadir}/sounds/freedesktop/stereo
%{_datadir}/sounds/freedesktop/index.theme
%{_datadir}/sounds/freedesktop/stereo/*.oga
