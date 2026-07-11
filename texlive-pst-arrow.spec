%global tl_name pst-arrow
%global tl_revision 61069

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.05
Release:	%{tl_revision}.1
Summary:	Special arrows for PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-arrow
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-arrow.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-arrow.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package has all the code from the package pstricks-add which was
related to arrows, like multiple arrows and so on.

