%global tl_name xetexref
%global tl_revision 73885

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Reference documentation of XeTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/xetexref
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xetexref.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package comprises reference documentation for XeTeX detailing its
extended features.

