%define module  WWW-Wikipedia
%define name	perl-%{module}
%define version 1.94
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    Automated interface to the Wikipedia
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/WWW/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRequires:  perl-libwww-perl
BuildRequires:  perl(CGI)
BuildRequires:  perl(Text::Autoformat)
Buildarch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
WWW::Wikipedia provides an automated interface to the Wikipedia 
http://www.wikipedia.org, which is a free, collaborative, online 
encyclopedia. This module allows you to search for a topic and return the 
resulting entry. It also gives you access to related topics which are also 
available via the Wikipedia for that entry.

%prep
%setup -q -n %{module}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/*
%_mandir/*/*
%perl_vendorlib/WWW


