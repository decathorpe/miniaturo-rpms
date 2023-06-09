# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate libopenraw

Name:           rust-libopenraw
Version:        0.1.2
Release:        %autorelease
Summary:        Rust API bindings for libopenraw

License:        MPL-2.0
URL:            https://crates.io/crates/libopenraw
Source0:        %{crates_source}
Source1:        https://gitlab.freedesktop.org/libopenraw/libopenraw-rs/-/raw/0497d9c/COPYING

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Rust API bindings for libopenraw.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYING
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep
cp -pav %{SOURCE1} .

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
