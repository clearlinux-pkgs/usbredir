#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x97D9123DE37A484F (toso@posteo.net)
#
Name     : usbredir
Version  : 0.10.0
Release  : 18
URL      : http://spice-space.org/download/usbredir/usbredir-0.10.0.tar.xz
Source0  : http://spice-space.org/download/usbredir/usbredir-0.10.0.tar.xz
Source1  : http://spice-space.org/download/usbredir/usbredir-0.10.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0+ LGPL-2.1
Requires: usbredir-bin = %{version}-%{release}
Requires: usbredir-lib = %{version}-%{release}
Requires: usbredir-license = %{version}-%{release}
Requires: usbredir-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : libusb-dev
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(libusb-1.0)

%description
# usbredir
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. See [usb-redirection-protocol.md](docs/usb-redirection-protocol.md)
for the description / definition of this protocol.

%package bin
Summary: bin components for the usbredir package.
Group: Binaries
Requires: usbredir-license = %{version}-%{release}

%description bin
bin components for the usbredir package.


%package dev
Summary: dev components for the usbredir package.
Group: Development
Requires: usbredir-lib = %{version}-%{release}
Requires: usbredir-bin = %{version}-%{release}
Provides: usbredir-devel = %{version}-%{release}
Requires: usbredir = %{version}-%{release}

%description dev
dev components for the usbredir package.


%package lib
Summary: lib components for the usbredir package.
Group: Libraries
Requires: usbredir-license = %{version}-%{release}

%description lib
lib components for the usbredir package.


%package license
Summary: license components for the usbredir package.
Group: Default

%description license
license components for the usbredir package.


%package man
Summary: man components for the usbredir package.
Group: Default

%description man
man components for the usbredir package.


%prep
%setup -q -n usbredir-0.10.0
cd %{_builddir}/usbredir-0.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622129178
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/usbredir
cp %{_builddir}/usbredir-0.10.0/COPYING %{buildroot}/usr/share/package-licenses/usbredir/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/usbredir-0.10.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/usbredir/3704f4680301a60004b20f94e0b5b8c7ff1484a9
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/usbredirect
/usr/sbin/usbredirserver

%files dev
%defattr(-,root,root,-)
/usr/include/usbredirfilter.h
/usr/include/usbredirhost.h
/usr/include/usbredirparser.h
/usr/include/usbredirproto.h
/usr/lib64/libusbredirhost.so
/usr/lib64/libusbredirparser.so
/usr/lib64/pkgconfig/libusbredirhost.pc
/usr/lib64/pkgconfig/libusbredirparser-0.5.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libusbredirhost.so.1
/usr/lib64/libusbredirhost.so.1.0.2
/usr/lib64/libusbredirparser.so.1
/usr/lib64/libusbredirparser.so.1.0.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/usbredir/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/usbredir/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/usbredirect.1
/usr/share/man/man1/usbredirserver.1
