Name: test
Version: 1
Release: 1%{?dist}
Summary: Test
License: Public Domain
URL: https://github.com/junaruga/report-rpmlint-load

%description

%prep
rpm --version
echo "%{hello}"

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

%files
%{_bindir}/test

%changelog
* Wed Dec 15 2021 Jun Aruga <jaruga@redhat.com> - 1-1
- Init.
