%define		_state		stable
%define		orgname		bomber
%define		qtver		4.8.0

Summary:	bomber
Name:		kde4-bomber
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	bceead58f2e21884917d47f2a1728a2b
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-bomber
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bomber.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
touch $RPM_BUILD_ROOT/var/games/kbounce.scores
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang bomber	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f bomber.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bomber
%{_desktopdir}/kde4/bomber.desktop
%{_datadir}/apps/bomber
%{_datadir}/config.kcfg/bomber.kcfg
%{_iconsdir}/hicolor/*x*/apps/bomber.png
%{_iconsdir}/hicolor/scalable/apps/bomber.svgz
