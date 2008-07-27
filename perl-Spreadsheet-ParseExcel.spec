#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Spreadsheet
%define		pnam	ParseExcel
Summary:	Spreadsheet::ParseExcel - get information from xls (Microsoft Excel) files
Summary(pl.UTF-8):	Spreadsheet::ParseExcel - odczyt informacji z plików w formacie xls (Microsoft Excel)
Name:		perl-Spreadsheet-ParseExcel
Version:	0.2603
Release:	3
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
Spreadsheet::ParseExcel makes you to get information from Excel95,
Excel97, Excel2000 file.

%description -l pl.UTF-8
Spreadsheet::ParseExcel umożliwia odczyt informacji z plików Excel95,
Excel97 i Excel2000.

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
