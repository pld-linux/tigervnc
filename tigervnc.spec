# TODO:
# - tigervnc.init

%define		snap	r4159

Summary:	TigerVNC - application based on the VNC version 3.3.3r2
Summary(pl.UTF-8):	TigerVNC - aplikacja bazująca na VNC w wersji 3.3.3r2
Name:		tigervnc
Version:	1.0.90
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Networking
#Source0:	http://dl.sourceforge.net/tigervnc/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	bd83717c960fb9e585387948b5cb41e2
Source1:	%{name}.desktop
URL:		http://www.tigervnc.com/
BuildRequires:	cpp
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRequires:	xorg-xserver-server-source >= 1.9
# xserver BRs, should match xorg-xserver-server.spec
BuildRequires:	Mesa-libGL-devel >= 7.8.1
# for glx headers
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.5
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	pixman-devel >= 0.16.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel  >= 1.0.99.4
BuildRequires:	xorg-lib-libXfont-devel >= 1.4.2
BuildRequires:	xorg-lib-libXi-devel >= 1.2.99.1
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXres-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-lib-libXtst-devel >= 1.0.99.2
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86misc-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-lib-libxkbui-devel >= 1.0.2
BuildRequires:	xorg-lib-xtrans-devel >= 1.2.2
BuildRequires:	xorg-proto-bigreqsproto-devel >= 1.1.0
BuildRequires:	xorg-proto-damageproto-devel >= 1.1
BuildRequires:	xorg-proto-fixesproto-devel >= 4.1
BuildRequires:	xorg-proto-fontcacheproto-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel >= 1.4.10
BuildRequires:	xorg-proto-inputproto-devel >= 1.9.99.902
BuildRequires:	xorg-proto-kbproto-devel >= 1.0.3
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-randrproto-devel >= 1.2.99.3
%{?with_record:BuildRequires:	xorg-proto-recordproto-devel}
BuildRequires:	xorg-proto-renderproto-devel >= 0.11
BuildRequires:	xorg-proto-resourceproto-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel >= 1.1.0
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xcmiscproto-devel >= 1.2.0
BuildRequires:	xorg-proto-xextproto-devel >= 1:7.0.99.3
BuildRequires:	xorg-proto-xf86bigfontproto-devel >= 1.2.0
BuildRequires:	xorg-proto-xf86dgaproto-devel >= 2.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel >= 2.1.0
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xf86vidmodeproto-devel >= 2.2.99.1
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.10
Provides:	vnc-client
Conflicts:	vnc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VNC is a great client/server software package allowing remote network
access to graphical desktops. TightVNC is optimized to work over slow
network connections such as low-speed modem links. While oroginal VNC
may be verry slow when your connection is not fast enough, with
TightVNC you can work remotely almost in real time in most
environments.

%description -l pl.UTF-8
VNC jest wspaniałym programem klient/serwer umożliwiającym zdalny
dostęp do graficznych pulpitów. TightVNC jest zoptymalizowany do pracy
przy wolniejszych połączeniach sieciowych takich jak połączenia
modemowe. Oryginalne VNC może pracować wolno kiedy połączenie nie jest
wystarczająco szybkie, natomiast z TightVNC możesz pracować zdalnie
niemal w czasie rzeczywistym.

%package server
Summary:	VNC X server - tightvnc version
Summary(pl.UTF-8):	X serwer VNC - wersja tightvnc
Group:		X11/Applications/Networking
Requires:	xorg-app-rgb
# for vncpasswd tool
Requires:	%{name}-utils = %{version}-%{release}
# for mcookie
Requires:	util-linux
Obsoletes:	vnc-server

%description server
This package contains VNC X server in tightvnc version.

%description server -l pl.UTF-8
Ten pakiet zawiera X serwer VNC w wersji tightvnc.

%package utils
Summary:	Additional utilities for tightvnc
Summary(pl.UTF-8):	Dodatkowe narzędzia do tightvnc
Group:		X11/Applications/Networking
Obsoletes:	vnc-utils

%description utils
This package contains additional tightvnc utilities: vncconnect and
vncpasswd. vncconnect tells Xvnc server to connect to a listening
tightvnc viewer. vncpasswd generates password file (both on server and
viewer side).

%description utils -l pl.UTF-8
Ten pakiet zawiera dodatkowe narzędzia do tightvnc: vncconnect i
vncpasswd. vncconnect służy do połączenia serwera Xvnc z nasłuchującym
vncviewerem. vncpasswd służy to tworzenia pliku z hasłem (zarówno po
stronie serwera, jak i przeglądarki).

%prep
%setup -q -n %{name}
%{__sed} -i -e 's|^po/Makefile.in||' configure.ac

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%{configure} \
	--with-system-jpeg

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_sysconfdir}}

cd unix
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/vncviewer
%{_mandir}/man1/vncviewer.1*
%{_desktopdir}/tightvnc.desktop
%{_pixmapsdir}/tightvnc.png

%files server
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tightvncserver.conf
%attr(755,root,root) %{_bindir}/x0vncserver
%attr(755,root,root) %{_bindir}/vncserver
%{_datadir}/vnc
%{_mandir}/man1/x0vncserver.1*
%{_mandir}/man1/vncserver.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vncconnect
%attr(755,root,root) %{_bindir}/vncpasswd
%{_mandir}/man1/vncconnect.1*
%{_mandir}/man1/vncpasswd.1*
