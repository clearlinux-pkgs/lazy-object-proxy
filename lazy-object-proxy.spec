#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lazy-object-proxy
Version  : 1.4.3
Release  : 38
URL      : https://files.pythonhosted.org/packages/07/3f/a3d687f83c7d44970f70ff0400677746c8860b11f0c08f6b4e07205f0cdc/lazy-object-proxy-1.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/07/3f/a3d687f83c7d44970f70ff0400677746c8860b11f0c08f6b4e07205f0cdc/lazy-object-proxy-1.4.3.tar.gz
Summary  : A fast and thorough lazy object proxy.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: lazy-object-proxy-license = %{version}-%{release}
Requires: lazy-object-proxy-python = %{version}-%{release}
Requires: lazy-object-proxy-python3 = %{version}-%{release}
Requires: pip
Requires: setuptools
Requires: virtualenv
BuildRequires : buildreq-distutils3
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : tox
BuildRequires : util-linux
BuildRequires : virtualenv

%description
========
Overview
========
.. start-badges
.. list-table::
:stub-columns: 1
* - docs
- |docs|
* - tests
- | |travis| |appveyor| |requires|
| |coveralls| |codecov|
* - package
- | |version| |wheel| |supported-versions| |supported-implementations|
| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-lazy-object-proxy/badge/?style=flat
:target: https://readthedocs.org/projects/python-lazy-object-proxy
:alt: Documentation Status

%package license
Summary: license components for the lazy-object-proxy package.
Group: Default

%description license
license components for the lazy-object-proxy package.


%package python
Summary: python components for the lazy-object-proxy package.
Group: Default
Requires: lazy-object-proxy-python3 = %{version}-%{release}

%description python
python components for the lazy-object-proxy package.


%package python3
Summary: python3 components for the lazy-object-proxy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the lazy-object-proxy package.


%prep
%setup -q -n lazy-object-proxy-1.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572186849
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lazy-object-proxy
cp %{_builddir}/lazy-object-proxy-1.4.3/LICENSE %{buildroot}/usr/share/package-licenses/lazy-object-proxy/145bfd0484ce08e6fd2c5b7d07e10e7e18da1216
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lazy-object-proxy/145bfd0484ce08e6fd2c5b7d07e10e7e18da1216

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
