#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Trace
Version  : 1.070
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/B/BB/BBC/Log-Trace-1.070.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BB/BBC/Log-Trace-1.070.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblog-trace-perl/liblog-trace-perl_1.070-3.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-Log-Trace-license = %{version}-%{release}
Requires: perl-Log-Trace-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Log::Trace v1.070
(c) BBC 2004. This program is free software; you can redistribute it and/or modify it under the GNU GPL.

%package dev
Summary: dev components for the perl-Log-Trace package.
Group: Development
Provides: perl-Log-Trace-devel = %{version}-%{release}
Requires: perl-Log-Trace = %{version}-%{release}

%description dev
dev components for the perl-Log-Trace package.


%package license
Summary: license components for the perl-Log-Trace package.
Group: Default

%description license
license components for the perl-Log-Trace package.


%package perl
Summary: perl components for the perl-Log-Trace package.
Group: Default
Requires: perl-Log-Trace = %{version}-%{release}

%description perl
perl components for the perl-Log-Trace package.


%prep
%setup -q -n Log-Trace-1.070
cd %{_builddir}
tar xf %{_sourcedir}/liblog-trace-perl_1.070-3.debian.tar.xz
cd %{_builddir}/Log-Trace-1.070
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Log-Trace-1.070/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Trace
cp %{_builddir}/Log-Trace-1.070/COPYING %{buildroot}/usr/share/package-licenses/perl-Log-Trace/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Log-Trace/faf387c4cce24590d2f052815d6e278cdbb09ebb
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Trace.3
/usr/share/man/man3/Log::Trace::Manual.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Log-Trace/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
/usr/share/package-licenses/perl-Log-Trace/faf387c4cce24590d2f052815d6e278cdbb09ebb

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Log/Trace.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Trace/Manual.pod
