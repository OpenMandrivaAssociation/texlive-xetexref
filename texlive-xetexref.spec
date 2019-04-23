Name:		texlive-xetexref
Version:	20181208
Release:	1
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
%doc %{_texmfdistdir}/doc/xetex/xetexref

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
