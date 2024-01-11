# https://bugzilla.redhat.com/show_bug.cgi?id=998047

Name:           python-backports
Version:        1.0
Release:        16%{?dist}
Summary:        Namespace for backported Python features

# Only code is sourced from http://www.python.org/dev/peps/pep-0382/
License:        Public Domain
URL:            https://pypi.python.org/pypi/backports
Source0:        backports.py

BuildRequires:  python2-devel

%global _description\
The backports namespace is a namespace reserved for features backported from\
the Python standard library to older versions of Python 2.\
\
Packages that exist in the backports namespace in Fedora should not provide\
their own backports/__init__.py, but instead require this package.\
\
Backports to earlier versions of Python 3, if they exist, do not need this\
package because of changes made in Python 3.3 in PEP 420\
(http://www.python.org/dev/peps/pep-0420/).\


%description %_description

%package -n python2-backports
Summary: %summary
%{?python_provide:%python_provide python2-backports}

%description -n python2-backports %_description

%prep


%build


%install
mkdir -pm 755 %{buildroot}%{python2_sitelib}/backports
install -pm 644 %{SOURCE0} %{buildroot}%{python2_sitelib}/backports/__init__.py
%if "%{python2_sitelib}" != "%{python2_sitearch}"
mkdir -pm 755 %{buildroot}%{python2_sitearch}/backports
install -pm 644 %{SOURCE0} %{buildroot}%{python2_sitearch}/backports/__init__.py
%endif

 
%files -n python2-backports
%{python2_sitelib}/backports
%if "%{python2_sitelib}" != "%{python2_sitearch}"
%{python2_sitearch}/backports
%endif


%changelog
* Wed Nov 18 2020 Tomas Orsava <torsava@redhat.com> - 1.0-16
- Update python macros to python2 versioned macros
- Issue found when rebuilding the python27 module to include CVE fixes
- Related: rhbz#1883890 rhbz#1883258

* Thu Apr 25 2019 Tomas Orsava <torsava@redhat.com> - 1.0-15
- Bumping due to problems with modular RPM upgrade path
- Resolves: rhbz#1695587

* Mon Jul 16 2018 Lumír Balhar <lbalhar@redhat.com> - 1.0-14
- First version for python27 module
