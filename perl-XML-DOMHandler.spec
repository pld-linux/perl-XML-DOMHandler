#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	DOMHandler
Summary:	DOMHandler - Implements a call-back interface to DOM
Summary(pl):	DOMHandler - implementacja interfejsu callback�w do DOM
Name:		perl-XML-DOMHandler
Version:	1.0
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-XML-LibXML
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module creates a layer on top of DOM that allows you to program
in a "push" style rather than "pull". Once the document has been
parsed and you have a DOM object, you can call on the DOMHandler's
traverse() method to apply a set of call-back routines to all the
nodes in a tree. You supply the routines in a handler package when
initializing the DOMHandler.

%description -l pl
Ten modu� tworzy warstw� powy�ej DOM, pozwalaj�c� na programowaniu w
stylu "pchnij" zamiast "ci�gnij". Po przeanalizowaniu dokumentu i
uzyskaniu obiektu DOM, mo�na wywo�a� metod� DOMHandlera traverse(),
aby zastosowa� zestaw callback�w na wszystkich w�z�ach w drzewie.
Funkcje przekazuje si� przy inicjalizacji DOMHandlera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
