Name:           python-txzookeeper
Version:        0.9.6
Release:        1%{?dist}
Summary:        Twisted api for Apache Zookeeper

Group:          Application/
License:        LGPL
URL:            http://launchpad.net/txzookeeper
Source0:        http://pypi.python.org/packages/source/t/txzookeeper/txzookeeper-%{version}.tar.gz

BuildArch:      noarch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  python-devel
Requires:       python-zookeeper python-twisted

%description
Twisted API for Apache Zookeeper. Includes a distributed lock, and several
queue implementations.


%prep
%setup -q -n txzookeeper-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O2 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%{python_sitelib}/*



%changelog
* Thu May 31 2012 Francisco Souza <f@souza.cc> - 0.9.5
- Initial packaging
