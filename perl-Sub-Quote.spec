%define upstream_name    Sub-Quote
%define upstream_version 2.005000

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Defer generation of subroutines until they are first called
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/%{upstream_name}-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
