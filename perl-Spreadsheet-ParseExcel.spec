#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Spreadsheet
%define	pnam	ParseExcel
Summary:	Spreadsheet::ParseExcel Perl module
Summary(cs):	Modul Spreadsheet::ParseExcel pro Perl
Summary(da):	Perlmodul Spreadsheet::ParseExcel
Summary(de):	Spreadsheet::ParseExcel Perl Modul
Summary(es):	M�dulo de Perl Spreadsheet::ParseExcel
Summary(fr):	Module Perl Spreadsheet::ParseExcel
Summary(it):	Modulo di Perl Spreadsheet::ParseExcel
Summary(ja):	Spreadsheet::ParseExcel Perl �⥸�塼��
Summary(ko):	Spreadsheet::ParseExcel �� ����
Summary(nb):	Perlmodul Spreadsheet::ParseExcel
Summary(pl):	Modu� Perla Spreadsheet::ParseExcel
Summary(pt):	M�dulo de Perl Spreadsheet::ParseExcel
Summary(pt_BR):	M�dulo Perl Spreadsheet::ParseExcel
Summary(ru):	������ ��� Perl Spreadsheet::ParseExcel
Summary(sv):	Spreadsheet::ParseExcel Perlmodul
Summary(uk):	������ ��� Perl Spreadsheet::ParseExcel
Summary(zh_CN):	Spreadsheet::ParseExcel Perl ģ��
Name:		perl-Spreadsheet-ParseExcel
Version:	0.2603
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6ee6257d4b66cb9e147a0b50603d1387
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-OLE-Storage_Lite >= 0.08
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to get information from Excel file.

%description -l pl
Modu� ten umo�liwia odczyt informacji z plik�w w formacie xls (Microsoft Excel).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/Excel

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install sample/{README,*.pl,res_*} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install sample/Excel/*.xls $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/Excel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Spreadsheet/ParseExcel.pm
%dir %{perl_vendorlib}/Spreadsheet/ParseExcel
%{perl_vendorlib}/Spreadsheet/ParseExcel/*.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/x*.pl
%{_examplesdir}/%{name}-%{version}/[^x]*
