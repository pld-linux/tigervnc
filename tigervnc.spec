# TODO:
# - tigervnc.init

%define		snap		r4159
%define		xversion	1.9

Summary:	A TigerVNC remote display system
Summary(pl.UTF-8):	System zdalnego dostępu TigerVNC
Name:		tigervnc
Version:	1.0.90
Release:	2
License:	GPL v2
Group:		X11/Applications/Networking
#Source0:	http://dl.sourceforge.net/tigervnc/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	bd83717c960fb9e585387948b5cb41e2
Source1:	%{name}.desktop
Patch0:		tigervnc-cookie.patch
Patch1:		tigervnc-ldnow.patch
Patch2:		tigervnc-rh102434.patch
Patch3:		tigervnc-rh611677-generate_modkeymap-max_keys.patch
Patch4:		tigervnc-rh611677.patch
Patch5:		tigervnc-rh633931.patch
Patch6:		tigervnc-viewer-reparent.patch
Patch7:		tigervnc-as-needed.patch
URL:		http://www.tigervnc.com/
BuildRequires:	ImageMagick
BuildRequires:	cpp
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRequires:	xorg-xserver-server-source >= %{xversion}
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
BuildRequires:	xorg-proto-recordproto-devel
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

%define		_xserverver	%(LC_ALL=C rpm -q --qf '%{V}' xorg-xserver-server-source)

%description
TigerVNC is a suite of VNC servers and clients that have a focus on
performance and remote display functionality. Originally this software
was based on the (never released) VNC 4 branch of TightVNC.

%description -l pl.UTF-8
TigerVNC to zestaw serwerów i klientów VNC, które koncentrują się
na wydajności i funkcjonalności zdalnego wyświetlania. Pierwotnie
oprogramowanie oparte było na (nigdy nie wydanej)
gałęzi VNC 4 TightVNC.

%package server
Summary:	VNC X server - TigerVNC version
Summary(pl.UTF-8):	X serwer VNC - wersja TigerVNC
Group:		X11/Applications/Networking
Requires:	xorg-app-rgb
# for vncpasswd tool
Requires:	%{name}-utils = %{version}-%{release}
# for mcookie
Requires:	util-linux
Obsoletes:	vnc-server

%description server
This package contains VNC X server in TigerVNC version.

%description server -l pl.UTF-8
Ten pakiet zawiera X serwer VNC w wersji TigerVNC.

%package utils
Summary:	Additional utilities for TigerVNC
Summary(pl.UTF-8):	Dodatkowe narzędzia do TigerVNC
Group:		X11/Applications/Networking
Obsoletes:	vnc-utils

%description utils
This package contains additional TigerVNC utilities: vncconfig and
vncpasswd. vncconfig is used to configure and control a running
instance of Xvnc, or any other X server with the VNC extension.
vncpasswd generates password file (both on server and viewer side).

%description utils -l pl.UTF-8
Ten pakiet zawiera dodatkowe narzędzia do tightvnc: vncconfig i
vncpasswd. vncconfig służy do konfigurowania i kontroli działającej
instancji Xvnc lub innego serwera X z rozszerzeniem VNC.
vncpasswd służy to tworzenia pliku z hasłem (zarówno po
stronie serwera, jak i przeglądarki).

%package -n xorg-xserver-libvnc
Summary:	TigerVNC module for X.org server
Summary(pl.UTF-8):	Moduł TigerVNC dla servera X.org
Group:		X11/Servers
%requires_eq_to	xorg-xserver-server xorg-xserver-server-source
Provides:	xorg-xserver-module(vnc)

%description -n xorg-xserver-libvnc
This package contains libvnc.so module for X.org server,
allowing others to access the desktop on your machine.

%description -n xorg-xserver-libvnc -l pl.UTF-8
Ten pakiet zawiera moduł libvnc.so dla serwera X.org,
pozwalający na zdalny dostęp do pulpitu.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%{__sed} -i -e 's|^po/Makefile.in||' configure.ac

cp -a %{_usrsrc}/xorg-xserver-server-%{_xserverver}/* unix/xserver
cd unix/xserver
patch -p1 <../xserver19.patch
%patch3 -p1

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

cd unix/xserver
%{__automake}
%{__autoconf}
%configure \
	--with-os-name="PLD/Linux" \
	--with-os-vendor="PLD/Team" \
	--disable-config-dbus \
	--disable-config-hal \
	--disable-config-udev \
	--disable-builddocs \
	--without-xmlto \
	--without-fop \
	--without-doxygen \
	--disable-devel-docs \
	--with-default-font-path="%{_fontsdir}/misc,%{_fontsdir}/TTF,%{_fontsdir}/OTF,%{_fontsdir}/Type1,%{_fontsdir}/100dpi,%{_fontsdir}/75dpi" \
	--disable-xorg \
	--disable-xnest \
	--disable-xvfb \
	--disable-dmx \
	--disable-xwin \
	--disable-xephyr \
	--disable-kdrive \
	--disable-xfbdev \
	--disable-dri2 \
	--with-pic \
	--disable-static \
	--disable-xinerama \
	--disable-composite \
	--enable-glx \
	--enable-glx-tls \
	--enable-aiglx \
	--enable-dga \
	--enable-glx-tls \
	--enable-install-libxf86config \
	--enable-record \
	--disable-xsdl \
	--disable-xfake \
	--enable-secure-rpc \
	--with-dri-driver-path=%{_libdir}/xorg/modules/dri \
	--with-xkb-output=/var/lib/xkb

%{__make}
cd -

cd media
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,22x22,24x24,32x32,48x48,scalable}/apps \
	$RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd unix/xserver/hw/vnc
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd -

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install media/icons/tigervnc_16.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/tigervnc.png
install media/icons/tigervnc_22.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/22x22/apps/tigervnc.png
install media/icons/tigervnc_24.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/24x24/apps/tigervnc.png
install media/icons/tigervnc_32.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/tigervnc.png
install media/icons/tigervnc_48.png $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/tigervnc.png
install media/icons/tigervnc.svg $RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps/tigervnc.svg

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database_post
[ ! -x /usr/bin/gtk-update-icon-cache ] || %update_icon_cache hicolor

%postun
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database_postun
[ ! -x /usr/bin/gtk-update-icon-cache ] || %update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/vncviewer
%{_mandir}/man1/vncviewer.1*
%{_desktopdir}/tigervnc.desktop
%{_iconsdir}/hicolor/*/apps/tigervnc.*

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvnc
%attr(755,root,root) %{_bindir}/vncserver
%attr(755,root,root) %{_bindir}/x0vncserver
%{_mandir}/man1/Xvnc.1*
%{_mandir}/man1/vncserver.1*
%{_mandir}/man1/x0vncserver.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vncconfig
%attr(755,root,root) %{_bindir}/vncpasswd
%{_mandir}/man1/vncconfig.1*
%{_mandir}/man1/vncpasswd.1*

%files -n xorg-xserver-libvnc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/extensions/libvnc.so
