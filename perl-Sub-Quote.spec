%define upstream_name    Sub-Quote

Name:		perl-%{upstream_name}
Version:	2.006008
Release:	1

Summary:	Defer generation of subroutines until they are first called
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Sub::Quote
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/%{upstream_name}-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Method::Modifiers)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(strictures)
BuildRequires:	perl(Devel::GlobalDestruction)
BuildArch:	noarch

%description
Defer generation of subroutines until they are first called.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
