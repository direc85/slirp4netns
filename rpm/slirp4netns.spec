#
# spec file for package slirp4netns
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           slirp4netns
Version:        1.3.1
Release:        1
Summary:        User-mode networking for unprivileged network namespaces
License:        BSD-2-Clause AND GPL-2.0-only AND MIT
Group:          System/Management
URL:            https://github.com/rootless-containers/slirp4netns
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libcap-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libslirp-devel

%description
slirp for network namespaces, without copying buffers across the namespaces.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure
%make_build all

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
