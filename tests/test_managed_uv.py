import os
import subprocess
import pytest

from hermes_cli import managed_uv


def test_update_managed_uv_handles_oserror(monkeypatch, tmp_path):
    # Simulate resolve_uv returning a path
    uv_path = str(tmp_path / "uv.exe")
    monkeypatch.setattr(managed_uv, "resolve_uv", lambda: uv_path)

    # Make subprocess.run raise OSError when attempting self update
    def fake_run(cmd, *args, **kwargs):
        if "self" in cmd:
            raise OSError("[WinError 4551] An Application Control policy has blocked this file")
        # For --version call, return a dummy CompletedProcess
        class CP:
            returncode = 0
            stdout = "uv 1.2.3"
            stderr = ""
        return CP()

    monkeypatch.setattr(subprocess, "run", fake_run)

    # Should not raise
    res = managed_uv.update_managed_uv(force=True)
    assert res == uv_path


def test_update_managed_uv_env_opt_out(monkeypatch, tmp_path):
    uv_path = str(tmp_path / "uv.exe")
    monkeypatch.setattr(managed_uv, "resolve_uv", lambda: uv_path)

    called = {"run": False}

    def fake_run(cmd, *args, **kwargs):
        called["run"] = True
        raise AssertionError("subprocess.run should not be invoked when opt-out is set")

    monkeypatch.setattr(subprocess, "run", fake_run)

    monkeypatch.setenv("HERMES_MANAGED_UV_SELF_UPDATE", "0")

    res = managed_uv.update_managed_uv(force=True)
    assert res == uv_path
    assert not called["run"]
