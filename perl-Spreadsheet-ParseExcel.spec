#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Spreadsheet
%define	pnam	ParseExcel
Summary:	Spreadsheet::ParseExcel perl module
Summary(pl):	Modu³ perla Spreadsheet::ParseExcel
Name:		perl-%{pdir}-%{pnam}
Version:	0.2602
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-56
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-OLE-Storage_Lite >= 0.08
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to get information from Excel file.

%description -l pl
Modu³ ten umo¿liwia odczyt informacji z plików w formacie xls (Microsoft Excel).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/Excel

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install sample/{README,*.pl,res_*} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install sample/Excel/*.xls $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/Excel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Spreadsheet/ParseExcel.pm
%{perl_sitelib}/Spreadsheet/ParseExcel/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
