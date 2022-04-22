# This spec file generates an RPM that installs the kubectl-hns binary
# scripts into the /usr/bin directory.
# Copyright 2022 Hewlett Packard Enterprise Development LP

%define bin_dir /usr/bin

Name: cray-kubectl-hns-plugin
Vendor: Hewlett Packard Enterprise Company
License: HPE Proprietary 
Summary: Install and configuration of node_exporter
Version: %(cat .version) 
Release: %(echo ${BUILD_METADATA})
Source: %{name}-%{version}.tar.bz2

# Compiling not currently required:
# BuildArchitectures: noarch

%description
This RPM when installed will install and configure the /usr/bin/kubectl-hns binary.

%files
%defattr(755, root, root)
%dir %{bin_dir}
%{bin_dir}/kubectl-hns

%prep
%setup -q

%build

%install
install -m 755 -d %{buildroot}%{bin_dir}/
install -m 755 kubectl-hns  %{buildroot}%{bin_dir}

exit 0
