%global tl_name lplfitch
%global tl_revision 75712

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9
Release:	%{tl_revision}.1
Summary:	Fitch-style natural deduction proofs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lplfitch
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lplfitch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lplfitch.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lplfitch.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros for typesetting natural deduction proofs in
"Fitch" style, with subproofs indented and offset by scope lines. The
proofs from use of the package are in the format used in the textbook
"Language, Proof, and Logic" by Dave Barker-Plummer, Jon Barwise, and
John Etchemendy. (In fact, the prefix "lpl" in the package name stands
for "Language, Proof, and Logic".)

