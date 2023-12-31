
{ pkgs ? import <nixpkgs> {} }:

let
  pythonPackages = with pkgs.python311Packages; [
    click
    fastapi
    uvicorn
    requests
    python-dotenv
    pandas
    jupyterlab
    ipython
    pip
  ];
# https://ryantm.github.io/nixpkgs/languages-frameworks/python/#how-to-consume-python-modules-using-pip-in-a-virtual-environment-like-i-am-used-to-on-other-operating-systems
in pkgs.mkShell rec {
  buildInputs = [
    # A Python interpreter including the 'venv' module is required to bootstrap
    # the environment.
    pkgs.cookiecutter
    pkgs.python311
    pythonPackages
  ];
}
