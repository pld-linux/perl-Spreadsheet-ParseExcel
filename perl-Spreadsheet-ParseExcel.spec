#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Spreadsheet
%define		pnam	ParseExcel
Summary:	Spreadsheet::ParseExcel Perl module
Summary(cs):	Modul Spreadsheet::ParseExcel pro Perl
Summary(da):	Perlmodul Spreadsheet::ParseExcel
Summary(de):	Spreadsheet::ParseExcel Perl Modul
Summary(es):	Módulo de Perl Spreadsheet::ParseExcel
Summary(fr):	Module Perl Spreadsheet::ParseExcel
Summary(it):	Modulo di Perl Spreadsheet::ParseExcel
Summary(ja):	Spreadsheet::ParseExcel Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Spreadsheet::ParseExcel ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Spreadsheet::ParseExcel
Summary(pl):	Modu³ Perla Spreadsheet::ParseExcel
Summary(pt):	Módulo de Perl Spreadsheet::ParseExcel
Summary(pt_BR):	Módulo Perl Spreadsheet::ParseExcel
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Spreadsheet::ParseExcel
Summary(sv):	Spreadsheet::ParseExcel Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Spreadsheet::ParseExcel
Summary(zh_CN):	Spreadsheet::ParseExcel Perl Ä£¿é
Name:		perl-Spreadsheet-ParseExcel
Version:	0.2602
Release:	0.2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
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
%{__perl} Makefile.PL
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
%dir %{perl_sitelib}/Spreadsheet/ParseExcel
%{perl_sitelib}/Spreadsheet/ParseExcel/*.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/x*.pl
%{_examplesdir}/%{name}-%{version}/[^x]*
