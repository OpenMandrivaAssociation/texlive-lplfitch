Name:		texlive-lplfitch
Version:	31077
Release:	2
Summary:	Fitch-style natural deduction proofs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lplfitch
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lplfitch.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lplfitch.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lplfitch.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
