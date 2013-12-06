# revision 30636
# category Package
# catalog-ctan /info/xetexref
# catalog-date 2013-05-21 21:04:45 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-xetexref
Version:	20130521
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
The package comprises reference documentation for XeTeX
detailing its extended features.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/xetex/xetexref/Makefile
%doc %{_texmfdistdir}/doc/xetex/xetexref/Makefile.ini
%doc %{_texmfdistdir}/doc/xetex/xetexref/README
%doc %{_texmfdistdir}/doc/xetex/xetexref/xetex-reference.pdf
%doc %{_texmfdistdir}/doc/xetex/xetexref/xetex-reference.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
