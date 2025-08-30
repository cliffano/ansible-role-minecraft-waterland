import pytest

def test_mcw_resource_pack_dir(host):

    mcw_resource_pack_dir = host.file('~/.minecraft/resourcepacks/Waterland')
    assert mcw_resource_pack_dir.exists
    assert mcw_resource_pack_dir.is_directory
    assert mcw_resource_pack_dir.mode == 0o755

def test_mcw_resource_pack_assets_dir(host):

    mcw_resource_pack_assets_dir = host.file('~/.minecraft/resourcepacks/Waterland/assets')
    assert mcw_resource_pack_assets_dir.exists
    assert mcw_resource_pack_assets_dir.is_directory
    assert mcw_resource_pack_assets_dir.mode == 0o755


def test_mcw_resource_pack_meta_file(host):

    mcw_resource_pack_meta_file = host.file('~/.minecraft/resourcepacks/Waterland/pack.mcmeta')
    assert mcw_resource_pack_meta_file.exists
    assert mcw_resource_pack_meta_file.is_file
    assert mcw_resource_pack_meta_file.mode == 0o644

def test_mcw_resource_pack_icon_file(host):

    mcw_resource_pack_icon_file = host.file('~/.minecraft/resourcepacks/Waterland/pack.png')
    assert mcw_resource_pack_icon_file.exists
    assert mcw_resource_pack_icon_file.is_file
    assert mcw_resource_pack_icon_file.mode == 0o644