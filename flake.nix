{
  description = "Nix devshells";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
    python = pkgs.python311;

    moulinetteSrc = builtins.fetchGit {
      url = "git@gitlab.cri.epita.fr:timothee.le-roux-maertens/moulinette-ji.git";
      rev = "37babe2ffea1b312fd70b4c3adacccc3c829aa70"; # commit hash
      ref = "feat/improvements";
    };

    moulinetteji = python.pkgs.buildPythonPackage {
      pname = "moulinetteji";
      version = "0.1.0";
      src = moulinetteSrc;

      pyproject = true;
      build-system = with python.pkgs; [ setuptools wheel ];
      propagatedBuildInputs = with python.pkgs; [ pyfiglet jinja2 ];
      doCheck = false; # prevent fail on missing tests
    };

    pyEnv = python.withPackages (_: [
      moulinetteji
    ]);
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = [ pkgs.jq pyEnv ];
    };
  };
}

