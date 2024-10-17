Name:		texlive-xetexref
Version:	70299
Release:	1
Summary:	Reference documentation of XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/xetexref
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexref.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexref.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
