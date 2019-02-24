%global modname tabulate

Name:           python-%{modname}
Version:        0.8.3
Release:        6%{?dist}
Summary:        Pretty-print tabular data in Python, a library and a command-line utility

License:        MIT
URL:            https://pypi.python.org/pypi/tabulate
Source0:        https://files.pythonhosted.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
The main use cases of the library are:
* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point

%if 0%{?rhel}
%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python-setuptools
BuildRequires:  numpy

%description -n python2-%{modname}
The main use cases of the library are:
* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point%endif
This package builds for Python 2 version.
%endif

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# Test deps
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  python%{python3_pkgversion}-numpy
%if 0%{?fedora}
BuildRequires:  python%{python3_pkgversion}-pandas
%endif
BuildRequires:  python%{python3_pkgversion}-wcwidth
# widechars support
%if 0%{?fedora}
Recommends:     python%{python3_pkgversion}-wcwidth
%endif

%description -n python%{python3_pkgversion}-%{modname}
The main use cases of the library are:
* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point
This package builds for Python %{python3_version} version.


%prep
%autosetup -n tabulate-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
sed -i 's/"python"/"python3"/g' test/test_cli.py
%{__python3} setup.py test


%if 0%{?rhel}
%files -n python2-%{modname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{modname}*.egg-info/
%{python2_sitelib}/%{modname}.py*
%{_bindir}/tabulate
%endif

%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE
%doc README.rst
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*


%changelog
* Thu Feb 21 2019 Raphael Groner <projects.rg@smart.ms> - 0.8.3-6
- fix merge conflicts

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.3-3
- Remove py2 subpackage

* Sat Jan 26 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.3-2
- Fix FTBFS

* Sat Jan 26 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.8.3-1
- Update to latest upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Steve Traylen <steve.traylen@cern.ch> - 0.8.2-1
- Update to 0.8.2, Correct source URL.

* Tue Oct 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Update to 0.8.1
- Run more tests

* Sun Oct 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.5-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.5-2
- Drop multiple versions of bins

* Tue Nov 24 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.5-1
- Initial package
