# cray-kubectl-hns-plugin

This repo creates an rpm for installation on NCNs so `kubectl hns *` commands can work.

The .version file in this repo should be updated to stay in sync with the version of the kubectl-hns
binary being bundled in the rpm.  The initial binary was pulled from:

https://github.com/kubernetes-sigs/hierarchical-namespaces/releases/download/v1.0.0/kubectl-hns_linux_amd64

See https://github.com/kubernetes-sigs/hierarchical-namespaces for the latest `kubectl-hns` plugin info.
