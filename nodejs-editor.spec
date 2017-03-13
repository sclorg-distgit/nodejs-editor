%{?scl:%scl_package nodejs-editor}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-editor
Version:        1.0.0
Release:        2%{?dist}
Summary:        Launch the default text editor from Node.js programs
BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch
#package.json indicates MIT, but no license file included
#upstream notified in https://github.com/substack/node-editor/pull/5
#we're including a copy of the MIT license based off a copy from another
#project by the same author indicating the same license in order to comply
#with the terms of the MIT license
License:        MIT
URL:            https://github.com/substack/node-editor
Source0:        http://registry.npmjs.org/editor/-/editor-%{version}.tgz
Source1:        https://raw.github.com/tchollingsworth/node-editor/05d7fbfcf22329db9aae5c676b0721045e7974d5/LICENSE
BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}.

%prep
%setup -q -n package

#copy LICENSE file to %%{_builddir} so it works with %%doc
cp %{SOURCE1} .

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/editor
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/editor

%nodejs_symlink_deps

%files
%{nodejs_sitelib}/editor
%doc README.markdown LICENSE example

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-2
- rebuilt

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- New upstream release

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.0-2
- New upstream release 0.1.0

* Thu Jan 16 2014 Tomas Hrcka <thrcka@redhat.com> - 0.0.5-1
- New upstream release 0.0.5

* Thu Nov 07 2013 Tomas Hrcka <thrcka@redhat.com> - 0.0.4-3.1
- Software collections support

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-2
- restrict to compatible arches

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.4-1
- initial package
