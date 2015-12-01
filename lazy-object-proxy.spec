#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lazy-object-proxy
Version  : 1.2.1
Release  : 1
URL      : https://pypi.python.org/packages/source/l/lazy-object-proxy/lazy-object-proxy-1.2.1.tar.gz
Source0  : https://pypi.python.org/packages/source/l/lazy-object-proxy/lazy-object-proxy-1.2.1.tar.gz
Summary  : A fast and thorough lazy object proxy.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: lazy-object-proxy-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================
lazy-object-proxy
===============================

%package python
Summary: python components for the lazy-object-proxy package.
Group: Default

%description python
python components for the lazy-object-proxy package.


%prep
%setup -q -n lazy-object-proxy-1.2.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
