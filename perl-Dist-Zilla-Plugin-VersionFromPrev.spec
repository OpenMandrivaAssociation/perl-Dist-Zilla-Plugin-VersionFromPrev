%define upstream_name    Dist-Zilla-Plugin-VersionFromPrev
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Get the last version via Git tag with C< git tag -l | sort -nr | head -n1 >
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::Role::VersionProvider)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This plugin was written because the author didn't like the time-based
version RJBS likes to use as implemented in the
Dist::Zilla::Plugin::AutoVersion manpage. Instead this plugin supports the
classic CPAN version schema where you start at '0.01' and move towards
'0.99', then increment to '1.00' and keep going from there.

This is how you use the plugin:

    [VersionFromPrev]

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
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

