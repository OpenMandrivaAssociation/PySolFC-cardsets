%define thegame PySolFC
%define name %{thegame}-cardsets
%define arcname %{thegame}-Cardsets
%define arcwithver %{arcname}-%{version}
%define version 2.0
%define release %mkrel 1
%define pysol_ver 2.0
%define instdir /usr/share/%{thegame}

Summary: A collection of free cardsets adapted for use with PySol
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{arcwithver}.tar.bz2
License: GPL
Group: Games/Cards
URL: http://www.oberhumer.com/opensource/pysol/	
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: %{thegame} >= %pysol_ver

%description
A collection of 70 free cardsets adapted for use with PySolFC.

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



