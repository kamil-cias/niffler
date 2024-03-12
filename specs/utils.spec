Name:     niffler
Version:  2
Release:  1
Summary:  Most simple RPM package
License:  GPL
Packager: Kamil Ciaś <kamil.cias@goto.systems>

%description
The niffler app helps you efficiently find all public SSH keys available on your system.

%prep
# we have no source, so nothing here

%build
./niffler

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 niffler %{buildroot}/usr/bin/niffler

%files
/usr/bin/niffler

%changelog
# let's skip this for now
