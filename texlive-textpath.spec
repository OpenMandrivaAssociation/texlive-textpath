# revision 15878
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/textpath
# catalog-date 2007-02-22 10:19:41 +0100
# catalog-license lppl
# catalog-version 1.6
Name:		texlive-textpath
Version:	1.6
Release:	8
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 756789
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 719720
- texlive-textpath
- texlive-textpath
- texlive-textpath

