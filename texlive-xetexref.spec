# revision 20921
# category Package
# catalog-ctan /info/xetexref
# catalog-date 2011-01-03 15:37:34 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-xetexref
Version:	20110103
Release:	3
Summary:	Reference documentation of XeTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/xetexref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexref.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The package comprises unofficial reference documentation for
XeTeX detailing its extended features.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/xetex/xetexref/README
%doc %{_texmfdistdir}/doc/xetex/xetexref/XeTeX-reference.ltx
%doc %{_texmfdistdir}/doc/xetex/xetexref/XeTeX-reference.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110103-2
+ Revision: 757645
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110103-1
+ Revision: 719935
- texlive-xetexref
- texlive-xetexref
- texlive-xetexref

