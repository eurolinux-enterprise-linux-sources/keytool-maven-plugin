Name:             keytool-maven-plugin
Version:          1.0
Release:          13%{?dist}
Summary:          A plugin that wraps the keytool program and allows to manipulate keystores
License:          MIT and ASL 2.0
# http://mojo.codehaus.org/keytool-maven-plugin/
URL:              http://mojo.codehaus.org/%{name}/
# svn export http://svn.codehaus.org/mojo/tags/keytool-maven-plugin-1.0/ keytool-maven-plugin-1.0
# tar caf keytool-maven-plugin-1.0.tar.xz keytool-maven-plugin-1.0
Source0:          %{name}-%{version}.tar.xz
Source1:          LICENSE-ASL

BuildArch:        noarch

BuildRequires:    java-devel
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-surefire-provider-junit4

%description
A plugin that wraps the keytool program bundled with Sun's Java SDK.
It provides the capability to manipulate keys and keystores
with the goals "keytool:genkey" and "keytool:clean".

%package javadoc
Summary:          API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# fixing licenses
mv LICENSE.txt LICENSE-MIT
cp %{SOURCE1} LICENSE-ASL

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-MIT LICENSE-ASL
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE-MIT LICENSE-ASL

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0-13
- Mass rebuild 2013-12-27

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-12
- Migrate away from mvn-rpmbuild (#997457)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-11
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0-9
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-8
- Add missing BR: maven-surefire-provider-junit4

* Thu Nov 22 2012 Jaromir Capik <jcapik@redhat.com> - 1.0-7
- Missing ASL 2.0 license file included
- Minor spec file changes according to the latest guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed May 25 2011 Jaromir Capik <jcapik@redhat.com> - 1.0-4
- Missing runtime deps (maven) added

* Wed May 25 2011 Jaromir Capik <jcapik@redhat.com> - 1.0-3
- Missing runtime deps (plexus-utils, apache-commons-lang) added

* Fri May 20 2011 Jaromir Capik <jcapik@redhat.com> - 1.0-2
- Missing MIT license added in the license field

* Thu May 19 2011 Jaromir Capik <jcapik@redhat.com> - 1.0-1
- Initial version of the package
