Summary:	freedesktop.org sound theme
Name:		sound-theme-freedesktop
Version:	0.3
Release:	1
Group:		Themes
Source0:	http://cgit.freedesktop.org/sound-theme-freedesktop/snapshot/%{name}-%{version}.tar.bz2
# Source0-md5:	b7a8de703be9d755fd6f1f48e8b0dfe8
License:	GPLv2+ and LGPLv2+ and CC-BY-SA and CC-BY
URL:		http://freedesktop.org/wiki/Specifications/sound-theme-spec
# For details on the licenses used, see README
BuildRequires:	autoconf
BuildRequires:	automake
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
make

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
%{_datadir}/sounds/freedesktop/stereo/*.ogg
