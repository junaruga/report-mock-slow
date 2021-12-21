Name: test
Version: 1
Release: 1%{?dist}
Summary: Test
License: Public Domain
URL: https://github.com/junaruga/report-mock-slow
BuildRequires: wget

%description

%prep
cat > test <<EOF
#!/bin/bash
echo "test"
EOF

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 test %{buildroot}/%{_bindir}/test

%check
echo "Testing ..."
echo "Mesuring the downloading time from cache.ruby-lang.org."
time wget --quiet https://cache.ruby-lang.org/pub/ruby/3.0/ruby-3.0.3.tar.gz
echo "Mesuring the downloading time from rubygems.org."
time wget --quiet https://rubygems.org/downloads/byebug-11.1.3.gem

%files
%{_bindir}/test

%changelog
* Wed Dec 15 2021 Jun Aruga <jaruga@redhat.com> - 1-1
- Init.
