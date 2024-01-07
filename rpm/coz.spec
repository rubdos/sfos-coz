Name: coz
Version: 0.2.2
Release: 0
Summary: Coz: Finding Code that Counts with Causal Profiling
License: MIT
Source: %{version}/%{name}-%{version}.tar.gz

Requires: libelfin

BuildRequires: git
BuildRequires: cmake
BuildRequires: libelfin-devel

%description
Coz is a profiler for native code (C/C++/Rust) that unlocks optimization opportunities missed by traditional profilers. Coz employs a novel technique called causal profiling that measures optimization potential. It predicts what the impact of optimizing code will have on overall throughput or latency.

Profiles generated by Coz show the "bang for buck" of optimizing a line of code in an application. In the below profile, almost every effort to optimize the performance of this line of code directly leads to an increase in overall performance, making it an excellent candidate for optimization efforts.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
pushd coz
mkdir -p build
pushd build

%cmake \
    .. \
    -DCMAKE_BUILD_TYPE=Release
%make_build DESTDIR=%{buildroot}

%install
pushd coz/build
export PREFIX=%{_prefix}
%make_install

rm %{buildroot}%{_prefix}/licenses/LICENSE.md

%files
%{_libdir}/libcoz.so
%{_bindir}/coz

%package devel
Summary: libelfin development files

%description devel
libelfin development files

%files devel
%{_prefix}/include/coz.h
%{_libdir}/cmake/coz-profilerConfig.cmake
%{_libdir}/cmake/coz-profilerConfigVersion.cmake
%{_libdir}/cmake/coz-profilerTargets-release.cmake
%{_libdir}/cmake/coz-profilerTargets.cmake
