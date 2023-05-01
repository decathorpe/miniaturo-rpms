%bcond_without check

Name:           miniaturo
Version:        0.5.0
Release:        %autorelease
Summary:        RAW image thumbnailer

SourceLicense:  GPL-3.0+
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# GPL-3.0+
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        GPL-3.0+ AND MIT AND MPL-2.0 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

URL:            https://github.com/dbrgn/miniaturo
Source:         %{url}/archive/v%{version}/miniaturo-%{version}.tar.gz
Source100:      miniaturo.thumbnailer
Source101:      miniaturo.xml

# upstream patches to support the latest version of the libopenraw crate
Patch:          https://github.com/dbrgn/miniaturo/commit/103dd19.patch
Patch:          https://github.com/dbrgn/miniaturo/commit/c5abcfa.patch

BuildRequires:  rust-packaging >= 23
Requires:       shared-mime-info

%description
A RAW image thumbnailer.

%prep
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
install -Dpm 644 %{SOURCE100} %{buildroot}%{_datadir}/thumbnailers/miniaturo.thumbnailer
install -Dpm 644 %{SOURCE101} %{buildroot}%{_datadir}/mime/packages/miniaturo.xml

%if %{with check}
%check
# * skip tests that require internet access for downloading test images
%cargo_test -- -- --skip generate_thumbnails --skip output_size
%endif

%files
%license LICENSE.md
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc README.md
%doc RELEASING.md
%{_bindir}/miniaturo
%{_datadir}/mime/packages/miniaturo.xml
%{_datadir}/thumbnailers/

%changelog
%autochangelog
