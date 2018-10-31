# revision 31077
# category Package
# catalog-ctan /macros/latex/contrib/lplfitch
# catalog-date 2013-07-02 16:20:31 +0200
# catalog-license lppl1.3
# catalog-version 0.9
Name:		texlive-lplfitch
Version:	0.9
Release:	10
Summary:	Fitch-style natural deduction proofs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lplfitch
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lplfitch.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lplfitch.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lplfitch.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros for typesetting natural deduction
proofs in "Fitch" style, with subproofs indented and offset by
scope lines. The proofs from use of the package are in the
format used in the textbook Language, Proof, and Logic by Dave
Barker-Plummer, Jon Barwise, and John Etchemendy.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/lplfitch/lplfitch.sty
%doc %{_texmfdistdir}/doc/latex/lplfitch/README
%doc %{_texmfdistdir}/doc/latex/lplfitch/lplfitch.pdf
#- source
%doc %{_texmfdistdir}/source/latex/lplfitch/lplfitch.dtx
%doc %{_texmfdistdir}/source/latex/lplfitch/lplfitch.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
