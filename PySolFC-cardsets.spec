%define thegame PySolFC
%define name %{thegame}-cardsets
%define arcname %{thegame}-Cardsets
%define arcwithver %{arcname}-%{version}
%define version 2.0
%define release %mkrel 2
%define pysol_ver 2.0
%define instdir /usr/share/%{thegame}

Summary: A collection of free cardsets adapted for use with PySolFC
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{arcwithver}.tar.bz2
License: GPL
Group: Games/Cards
URL: http://pysolfc.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: %{thegame} >= %pysol_ver
Obsoletes: pysol-cardsets

%description
A collection of 153 free cardsets adapted for use with PySolFC.

%prep
%setup -q -n %{arcwithver}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%{instdir}
cp -r cardset* %buildroot%{instdir}
cd %buildroot%{instdir}
# rm -rf cardset-2000 cardset-colossus cardset-hard-a-port cardset-hexadeck cardset-kintengu cardset-oxymoron cardset-tuxedo cardset-vienna-2k

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{instdir}/*





%changelog
* Mon Feb 15 2010 Shlomi Fish <shlomif@mandriva.org> 2.0-2mdv2010.1
+ Revision: 506354
- Correct some values and add an Obsoletes field
- import PySolFC-cardsets


* Sat Dec 05 2009 Shlomi Fish <shlomif@iglu.org.il> 2.0-1mdv
+ Updated to version 2.0.

* Mon May 26 2008 Shlomi Fish <shlomif@iglu.org.il> 1.1-1mdv
+ Adapted to PySolFC.

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 4.40-7mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Jun 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.40-7mdk
- Rebuild
- use mkrel

* Fri Jun 03 2005 Götz Waschk <waschk@mandriva.org> 4.40-6mdk
- drop prefix
- remove the cardsets already in the main package

* Fri Aug 13 2004 Götz Waschk <waschk@linux-mandrake.com> 4.40-5mdk
- rebuild

* Mon Jul 07 2003 Götz Waschk <waschk@linux-mandrake.com> 4.40-4mdk
- move files around (fixes bug 4153)

