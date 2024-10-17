%define upstream_name    WWW-Wikipedia
%define upstream_version 2.00 

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Automated interface to the Wikipedia
License:	Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(CGI)
BuildRequires:	perl(Text::Autoformat)
BuildArch:	noarch

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

%files
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/WWW

%changelog
* Tue Apr 05 2011 Sandro Cazzaniga <kharec@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 650737
- new version 2.00

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.990.0-1
+ Revision: 638972
- update to new version 1.99

* Mon Dec 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.980.0-1mdv2011.0
+ Revision: 612273
- update to new version 1.98

* Mon Jul 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.970.0-1mdv2011.0
+ Revision: 551206
- update to 1.97

* Tue Sep 15 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.960.0-1mdv2010.0
+ Revision: 442636
- update to 1.96

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.950.0-1mdv2010.0
+ Revision: 401882
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.95-1mdv2010.0
+ Revision: 370248
- update to new version 1.95

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.94-4mdv2009.0
+ Revision: 258793
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.94-3mdv2009.0
+ Revision: 246716
- rebuild

* Tue Feb 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.94-1mdv2008.1
+ Revision: 175318
- update to new version 1.94

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.93-1mdv2008.1
+ Revision: 118151
- update to new version 1.93


* Tue Mar 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.92-1mdv2007.1
+ Revision: 142368
- new version

  + Nicolas LÃ©cureuil <neoclust@mandriva.org>
    - import perl-WWW-Wikipedia-1.9-2mdk

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.9-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Thu Apr 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.9-1mdk
- New release 1.9

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.8-4mdk
- Fix BuildRequires

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.8-3mdk
- Fix BuildRequires

* Sat Oct 01 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.8-2mdk
- Buildrequires fix

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.8-1mdk
- New release 1.8

* Fri Aug 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-1mdk
- new release 
- fix sources url for rpmbuildupdate
- fix url

* Fri Apr 29 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.5-1mdk
- initial release

