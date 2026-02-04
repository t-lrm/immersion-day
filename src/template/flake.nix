{
  description = "JI student environment (user-profile install): Python env + moulinetteji + PyCharm";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs {
      inherit system;
      config = {
        allowUnfreePredicate = pkg:
          builtins.elem (nixpkgs.lib.getName pkg) [
            "pycharm"
          ];
      };
    };

    python = pkgs.python311;

    moulinetteji = python.pkgs.buildPythonPackage {
      pname = "moulinetteji";
      version = "0.1.0";
      src = ./moulinette;

      pyproject = true;
      build-system = with python.pkgs; [ setuptools wheel ];
      propagatedBuildInputs = with python.pkgs; [ pyfiglet ];

      # prevents fail on missing tests
      doCheck = false;
    };

    pyEnv = python.withPackages (ps: [
      moulinetteji
      ps.pygame
      ps.black
    ]);

    pycharm = pkgs.jetbrains.pycharm;

    ji = pkgs.symlinkJoin {
      name = "ji-tools";
      paths = [
        pyEnv
        pkgs.git
        pycharm
      ];
    };
  in
  {
    packages.${system} = {
      inherit moulinetteji pyEnv pycharm ji;
      default = ji;
    };
  };
}

