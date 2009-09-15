%define upstream_name    WWW-Wikipedia
%define upstream_version 1.96

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:    Automated interface to the Wikipedia
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRequires:  perl-libwww-perl
BuildRequires:  perl(CGI)
BuildRequires:  perl(Text::Autoformat)
Buildarch: noarch
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}

%description
WWW::Wikipedia provides an automated interface to the Wikipedia 
http://www.wikipedia.org, which is a free, collaborative, online 
encyclopedia. This module allows you to search for a topic and return the 
resulting entry. It also gives you access to related topics which are also 
available via the Wikipedia for that entry.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
