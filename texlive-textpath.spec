%global tl_name textpath
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Setting text along a path with MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/textpath
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textpath.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/textpath.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This MetaPost package provides macros to typeset text along a free path
with the help of LaTeX, thereby preserving kerning and allowing for
8-bit input (accented characters).

