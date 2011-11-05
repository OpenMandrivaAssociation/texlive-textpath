# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/textpath
# catalog-date 2007-02-22 10:19:41 +0100
# catalog-license lppl
# catalog-version 1.6
Name:		texlive-textpath
Version:	1.6
Release:	1
Summary:	Setting text along a path with MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/textpath
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textpath.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textpath.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This MetaPost package provides macros to typeset text along a
free path with the help of LaTeX, thereby preserving kerning
and allowing for 8-bit input (accented characters).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
