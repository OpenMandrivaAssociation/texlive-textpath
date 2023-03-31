Name:		texlive-textpath
Version:	15878
Release:	2
Summary:	Setting text along a path with MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/textpath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textpath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textpath.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This MetaPost package provides macros to typeset text along a
free path with the help of LaTeX, thereby preserving kerning
and allowing for 8-bit input (accented characters).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/textpath/textpath.mp
%{_texmfdistdir}/tex/latex/textpath/textpathmp.sty
%doc %{_texmfdistdir}/doc/metapost/textpath/CHANGES
%doc %{_texmfdistdir}/doc/metapost/textpath/README
%doc %{_texmfdistdir}/doc/metapost/textpath/textpath.pdf
%doc %{_texmfdistdir}/doc/metapost/textpath/textpath.tex
%doc %{_texmfdistdir}/doc/metapost/textpath/textpathfigs.mp
%doc %{_texmfdistdir}/doc/metapost/textpath/textpathfigs.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost tex doc %{buildroot}%{_texmfdistdir}
