%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	LDAP Authentication with PHP for Active Directory
Name:		php-adldap
Version:	3.3.2
Release:	2
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://downloads.sourceforge.net/adldap/adLDAP_%{version}.zip
# Source0-md5:	8b1b0d13d42623d8955e54ef7401dc11
URL:		http://adldap.sourceforge.net/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	php(bcmath)
Requires:	php(ldap)
Requires:	php(pcre)
Requires:	php(xml)
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
adLDAP is a PHP class that provides LDAP authentication and
integration with Active Directory.

Intelligent Active Directory integration with PHP was a holy grail for
most intranet developers for a long time. This project is really to
help others with getting over the same hurdles that we've experienced
in getting the whole LDAP SSL Active Directory puzzle working natively
on Linux.

Given the varied nature of organisations and sites, adLDAP may not be
_your_ complete solution, but it should be a very sound starting
point. LDAP isn't overly friendly on first glance, and it's a steep
learning curve made alot worse when coupled with Microsoft's seemingly
unending army of gotcha's.

The information you can retrieve from Active Directory is as useful as
you make it. If you don't fill out all their account information
there's not really going to be much to query.

%prep
%setup -q -n adLDAP
mv LICEN{C,S}E.txt
%undos *.php *.txt examples/*.php examples/*.htm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p adLDAP.php $RPM_BUILD_ROOT%{php_data_dir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt CHANGELOG.txt
%{php_data_dir}/adLDAP.php
%{_examplesdir}/%{name}-%{version}
