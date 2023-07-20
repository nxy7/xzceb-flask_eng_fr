{
  description = "Project starter";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flakeUtils.url = "github:numtide/flake-utils";
    nix2container.url = "github:nlewo/nix2container";
  };

  outputs = { self, nixpkgs, flakeUtils, nix2container, ... }@inputs:
    flakeUtils.lib.eachSystem [ "x86_64-linux" ] (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        };
      in {
        devShell = pkgs.mkShell {
          packages = with pkgs; [
            (python310.withPackages
              (ps: with ps; [ jinja2 flask deep-translator ]))
            python310Packages.jinja2
            python310Packages.python-lsp-server
            pipenv
            pylint
          ];
        };
      });
}
