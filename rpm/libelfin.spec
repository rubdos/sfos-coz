Name: libelfin
Version: 0.3.0
Release: 0
Summary: A library for parsing and analyzing ELF files and DWARF debugging information
License: MIT
Source: %{version}/%{name}-%{version}.tar.gz

Patch100: 0100-Add-tags-for-pc.patch

BuildRequires: git

%description
libelfin is a library for parsing and analyzing ELF files and DWARF debugging information.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
pushd libelfin
export PREFIX=%{_prefix}
%make_build DESTDIR=%{buildroot}

%install
pushd libelfin
export PREFIX=%{_prefix}
%make_install

%files
%{_libdir}/libdwarf++.so
%{_libdir}/libdwarf++.so.0
%{_libdir}/libelf++.so
%{_libdir}/libelf++.so.0
%{_libdir}/pkgconfig/libdwarf++.pc
%{_libdir}/pkgconfig/libelf++.pc

%package devel
Summary: libelfin development files

%description devel
libelfin development files

%files devel
%{_prefix}/include/libelfin
