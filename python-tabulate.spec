%global modname tabulate

Name:           python-%{modname}
Version:        0.8.0
Release:        1%{?dist}
Summary:        Pretty-print tabular data in Python, a library and a command-line utility

License:        MIT
URL:            https://pypi.python.org/pypi/tabulate
Source0:        https://bitbucket.org/astanin/%{name}/get/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
The main use cases of the library are:

* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# Test deps
BuildRequires:  python2-nose
BuildRequires:  python2-numpy

%description -n python2-%{modname}
The main use cases of the library are:

* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# Test deps
BuildRequires:  python3-nose
BuildRequires:  python3-numpy

%description -n python3-%{modname}
The main use cases of the library are:

* printing small tables without hassle: just one function call, formatting is
  guided by the data itself
* authoring tabular data for lightweight plain-text markup: multiple output
  formats suitable for further editing or transformation
* readable presentation of mixed textual and numeric data: smart column
  alignment, configurable number formatting, alignment by a decimal point

Python 3 version.

%prep
%autosetup -n astanin-%{name}-3830da89c6c1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{modname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/%{modname}*.egg-info/
%{python2_sitelib}/%{modname}.py*

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}*.egg-info/
%{python3_sitelib}/%{modname}.py
%{python3_sitelib}/__pycache__/%{modname}.*

%changelog
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
