"""Test for files."""
import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name, content", [
    ('/etc/yum.repos.d/elasticsearch-6.x.repo',
     'baseurl = https://artifacts.elastic.co/packages/6.x/yum'),
    ('/etc/kibana/kibana.yml', 'server.name: instance')
])
def test_files(host, name, content):
    """Test that file exists."""
    f = host.file(name)
    assert f.exists
    assert f.is_file
    assert f.contains(content)
