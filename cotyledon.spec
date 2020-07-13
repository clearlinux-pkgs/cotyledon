#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cotyledon
Version  : 1.7.3
Release  : 8
URL      : https://files.pythonhosted.org/packages/69/73/297dd1993288be157e5e48b7d22de4e708a2d2513e376b328c900be272d9/cotyledon-1.7.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/69/73/297dd1993288be157e5e48b7d22de4e708a2d2513e376b328c900be272d9/cotyledon-1.7.3.tar.gz
Summary  : Cotyledon provides a framework for defining long-running services.
Group    : Development/Tools
License  : Apache-2.0
Requires: cotyledon-license = %{version}-%{release}
Requires: cotyledon-python = %{version}-%{release}
Requires: cotyledon-python3 = %{version}-%{release}
Requires: setproctitle
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setproctitle
BuildRequires : setuptools
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================
Cotyledon
===============================
.. image:: https://img.shields.io/pypi/v/cotyledon.svg
:target: https://pypi.python.org/pypi/cotyledon/
:alt: Latest Version

%package license
Summary: license components for the cotyledon package.
Group: Default

%description license
license components for the cotyledon package.


%package python
Summary: python components for the cotyledon package.
Group: Default
Requires: cotyledon-python3 = %{version}-%{release}

%description python
python components for the cotyledon package.


%package python3
Summary: python3 components for the cotyledon package.
Group: Default
Requires: python3-core
Provides: pypi(cotyledon)

%description python3
python3 components for the cotyledon package.


%prep
%setup -q -n cotyledon-1.7.3
cd %{_builddir}/cotyledon-1.7.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582913570
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cotyledon
cp %{_builddir}/cotyledon-1.7.3/LICENSE %{buildroot}/usr/share/package-licenses/cotyledon/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cotyledon/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
