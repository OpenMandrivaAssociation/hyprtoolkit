%define major 2
%define libname %mklibname hyprtoolkit
%define devname %mklibname hyprtoolkit -d

Name:		hyprtoolkit
Version:        0.2.0
Release:	1
Source0:        https://github.com/hyprwm/hyprtoolkit/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:        A modern C++ Wayland-native GUI toolkit
URL:            https://github.com/hyprwm/hyprtoolkit
License:        BSD-3-Clause
Group:		System/Libraries

BuildSystem:  cmake
BuildOption:  --no-warn-unused-cli

BuildRequires:  pkgconfig(iniparser)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(hyprutils) >= 0.9.0
BuildRequires:  pkgconfig(hyprlang) >= 0.6.0
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprgraphics) >= 0.2.0
BuildRequires:  pkgconfig(aquamarine) >= 0.9.5
BuildRequires:  pkgconfig(hyprwayland-scanner) >= 0.4.0
BuildRequires:  pkgconfig(pangocairo)

%description
Hyprtoolkit is designed to be a small, simple, and modern C++ toolkit for making wayland GUI apps, with a few goals:

Simple C++ API for making a GUI app
Smooth animations
Easy usage
Simple system theming

%package -n %{libname}
Summary:	A modern C++ Wayland-native GUI toolkit
Group:		System/Libraries

%description -n %{libname}
Hyprtoolkit is designed to be a small, simple, and modern C++ toolkit for making wayland GUI apps, with a few goals:

Simple C++ API for making a GUI app
Smooth animations
Easy usage
Simple system theming

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1

%files
%doc README.md
%license LICENSE

%files -n %{libname}
%{_libdir}/*.so.*%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
