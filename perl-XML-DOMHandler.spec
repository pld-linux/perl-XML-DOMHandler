#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	DOMHandler
Summary:	DOMHandler - implements a call-back interface to DOM
Summary(pl.UTF-8):	DOMHandler - implementacja interfejsu callbacków do DOM
Name:		perl-XML-DOMHandler
Version:	1.0
Release:	4
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6dd4dcfed53eb23976c82d097225b430
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-XML-LibXML
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module creates a layer on top of DOM that allows you to program
in a "push" style rather than "pull". Once the document has been
parsed and you have a DOM object, you can call on the DOMHandler's
traverse() method to apply a set of call-back routines to all the
nodes in a tree. You supply the routines in a handler package when
initializing the DOMHandler.

%description -l pl.UTF-8
Ten moduł tworzy warstwę powyżej DOM, pozwalającą na programowaniu w
stylu "pchnij" zamiast "ciągnij". Po przeanalizowaniu dokumentu i
uzyskaniu obiektu DOM, można wywołać metodę DOMHandlera traverse(),
aby zastosować zestaw callbacków na wszystkich węzłach w drzewie.
Funkcje przekazuje się przy inicjalizacji DOMHandlera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
