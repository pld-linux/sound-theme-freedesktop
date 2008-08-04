Summary:	freedesktop.org sound theme
Name:		sound-theme-freedesktop
Version:	0.1
Release:	1
Group:		Themes
Source0:	http://0pointer.de/public/%{name}.tar.gz
# Source0-md5:	35f978665f0854f29a17a0974e780b1b
License:	GPLv2+ and LGPLv2+ and CC-BY-SA and CC-BY
URL:		http://0pointer.de/public/sound-theme-freedesktop.tar.gz
# For details on the licenses used, see README
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The default freedesktop.org sound theme following the XDG theming
specification (http://0pointer.de/public/sound-theme-spec.html).

%prep
%setup -q -n freedesktop

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sounds/freedesktop
cp -av index.theme stereo/ $RPM_BUILD_ROOT%{_datadir}/sounds/freedesktop

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
