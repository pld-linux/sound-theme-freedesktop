Summary:	freedesktop.org sound theme
Summary(pl.UTF-8):	Motyw dźwiękowy freedesktop.org
Name:		sound-theme-freedesktop
Version:	0.7
Release:	1
Group:		Themes
License:	GPL v2+, LGPL v2+, CC-BY-SA, CC-BY
Source0:	http://people.freedesktop.org/~mccann/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	7bcad4fa54570f80c612012bce66f60f
URL:		http://freedesktop.org/wiki/Specifications/sound-theme-spec
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

%description -l pl.UTF-8
Domyślny motyw dźwiękowy freedesktop.org zgodny ze specyfikacją
motywów XDG (http://0pointer.de/public/sound-theme-spec.html).

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
%doc NEWS README
%dir %{_datadir}/sounds/freedesktop
%dir %{_datadir}/sounds/freedesktop/stereo
%{_datadir}/sounds/freedesktop/index.theme
%{_datadir}/sounds/freedesktop/stereo/*.oga
