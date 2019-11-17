Summary:	freedesktop.org sound theme
Summary(pl.UTF-8):	Motyw dźwiękowy freedesktop.org
Name:		sound-theme-freedesktop
Version:	0.8
Release:	2
Group:		Themes
License:	GPL v2+, LGPL v2+, CC-BY-SA, CC-BY
Source0:	https://people.freedesktop.org/~mccann/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	d7387912cfd275282d1ec94483cb2f62
URL:		https://freedesktop.org/wiki/Specifications/sound-theme-spec
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.40.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The default freedesktop.org sound theme following the XDG theming
specification:
<https://freedesktop.org/wiki/Specifications/sound-theme-spec>.

%description -l pl.UTF-8
Domyślny motyw dźwiękowy freedesktop.org zgodny ze specyfikacją
motywów XDG:
<https://freedesktop.org/wiki/Specifications/sound-theme-spec>.

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
%doc CREDITS NEWS README
%dir %{_datadir}/sounds/freedesktop
%dir %{_datadir}/sounds/freedesktop/stereo
%{_datadir}/sounds/freedesktop/index.theme
%{_datadir}/sounds/freedesktop/stereo/*.oga
