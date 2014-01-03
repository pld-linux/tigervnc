%define		xversion	1.14.0

Summary:	A TigerVNC remote display system
Summary(pl.UTF-8):	System zdalnego dostępu TigerVNC
Name:		tigervnc
Version:	1.3.0
Release:	9
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://download.sourceforge.net/tigervnc/%{name}-%{version}.tar.bz2
# Source0-md5:	a5158228e64d14496821a39bf3851f1b
Source1:	%{name}.desktop
Source2:	vncserver.init
Source3:	vncserver.sysconfig
Source4:	vncserver.target
Source5:	vncserver-service-generator
Patch0:		%{name}-cookie.patch
Patch1:		%{name}-ldnow.patch
Patch3:		%{name}-as-needed.patch
Patch4:		%{name}-ipv6.patch
Patch5:		%{name}-rh692048.patch
Patch6:		no-bashizm.patch
Patch7:		format-security.patch
Patch8:		%{name}-typecast.patch
Patch9:		tigervnc-xstartup.patch
Patch10:	xserver.patch
Patch11:	tigervnc-getmaster.patch
Patch12:	tigervnc-setcursor-crash.patch
Patch13:	tigervnc-xserver-1.15.patch
Patch14:	tigervnc-zrle-crash.patch
URL:		http://www.tigervnc.com/
BuildRequires:	ImageMagick
BuildRequires:	ImageMagick-coder-png
BuildRequires:	ImageMagick-coder-svg
BuildRequires:	Mesa-libGL-devel >= 7.8.1
BuildRequires:	cpp
BuildRequires:	fltk-devel
BuildRequires:	gnutls-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	xorg-xserver-server-source >= %{xversion}
BuildRequires:	zlib-devel
# xserver BRs, should match xorg-xserver-server.spec
# for glx headers
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.5
BuildRequires:	libtool
BuildRequires:	nasm
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	perl-base
BuildRequires:	pixman-devel >= 0.16.0
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.647
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel >= 1.0.99.4
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
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.13
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
BuildRequires:	xorg-proto-presentproto-devel >= 1.0
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-randrproto-devel >= 1.3
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
BuildRequires:	xorg-proto-xproto-devel >= 7.0.22
BuildRequires:	xorg-util-util-macros >= 1.10
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	libjpeg-turbo
Provides:	vnc-client
Conflicts:	vnc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xserverver	%(LC_ALL=C rpm -q --qf '%{V}' xorg-xserver-server-source 2> /dev/null)

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
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Requires:	xorg-app-rgb
# for vncpasswd tool
Requires:	%{name}-utils = %{version}-%{release}
# for mcookie
Requires:	util-linux
Requires:	libjpeg-turbo
Requires:	systemd-units >= 38
Requires:	xkeyboard-config
Requires:	xorg-app-xauth
Requires:	xorg-app-xkbcomp
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
%setup -q
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch11 -p1
%patch12 -p1
%patch14 -p1

cp -a %{_usrsrc}/xorg-xserver-server-%{_xserverver}/* unix/xserver

%patch13 -p1

cd unix/xserver
%patch10 -p1

%build
%cmake .
%{__make}

cd unix/xserver
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
export CXXFLAGS="%{rpmcxxflags} -fpermissive"
%configure \
	--with-os-name="PLD/Linux" \
	--with-os-vendor="PLD/Team" \
	--disable-config-dbus \
	--disable-config-hal \
	--disable-config-udev \
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
	--disable-dri \
	--enable-dri2 \
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
	--disable-xfake \
	--enable-secure-rpc \
	--with-xkb-output=/var/lib/xkb \
	--disable-unit-tests

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

install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/vncserver
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/vncserver

install -d $RPM_BUILD_ROOT{%{systemdunitdir},/lib/systemd/system-generators}
install -p %{SOURCE4} $RPM_BUILD_ROOT%{systemdunitdir}/vncserver.target
install -p %{SOURCE5} $RPM_BUILD_ROOT/lib/systemd/system-generators/vncserver-service-generator
ln -s /dev/null $RPM_BUILD_ROOT%{systemdunitdir}/vncserver.service

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database_post
%update_icon_cache hicolor

%postun
[ ! -x /usr/bin/update-desktop-database ] || %update_desktop_database_postun
%update_icon_cache hicolor

%post server
/sbin/chkconfig --add vncserver
%service vncserver restart "VNC server"
NORESTART=1
%systemd_post vncserver.target

%preun server
if [ "$1" = "0" ]; then
	%service vncserver stop
	/sbin/chkconfig --del vncserver
fi
%systemd_preun vncserver.target

%postun server
%systemd_reload

%triggerpostun server -- tigervnc-server < 1.3.0-5
[ -f /etc/sysconfig/rpm ] && . /etc/sysconfig/rpm
[ ${RPM_ENABLE_SYSTEMD_SERVICE:-yes} = no ] && return 1
export SYSTEMD_LOG_LEVEL=warning SYSTEMD_LOG_TARGET=syslog
if [ "$(echo /etc/rc.d/rc[0-6].d/S[0-9][0-9]vncserver)" != "/etc/rc.d/rc[0-6].d/S[0-9][0-9]vncserver" ]; then
	/bin/systemctl --quiet enable vncserver.target || :
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.txt doc/*
%attr(755,root,root) %{_bindir}/vncviewer
%{_mandir}/man1/vncviewer.1*
%{_desktopdir}/tigervnc.desktop
%{_iconsdir}/hicolor/*/apps/tigervnc.*

%files server
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvnc
%attr(755,root,root) %{_bindir}/vncserver
%attr(755,root,root) %{_bindir}/x0vncserver
%attr(754,root,root) /etc/rc.d/init.d/vncserver
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/vncserver
%attr(755,root,root) /lib/systemd/system-generators/vncserver-service-generator
%{systemdunitdir}/vncserver.target
%{systemdunitdir}/vncserver.service
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
