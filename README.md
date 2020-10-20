# Ansible Role: Kibana

[![Build Status](https://travis-ci.org/javiergayala/ansible-role-kibana.svg?branch=master)](https://travis-ci.org/javiergayala/ansible-role-kibana) ![Ansible Role](https://img.shields.io/ansible/role/24682?logo=ansible) ![Ansible Role](https://img.shields.io/ansible/role/d/24682) ![Ansible Quality Score](https://img.shields.io/ansible/quality/24682)

Installs Kibana on RedHat/CentOS.

This role installs and configures the latest version of Kibana (6.x) from the official [Elastic.co](https://www.elastic.co/) [Repo](https://www.elastic.co/guide/en/elasticsearch/reference/current/rpm.html#rpm-repo).

## Requirements

None.

## Role Variables

### Default values (see `defaults/main.yml`):

```yaml
es_major_version: "6.x"
```

The version of Kibana should always match the verion of Elasticsearch in your ELK stack.  This represents the major version of Elasticsearch.

```yaml
es_use_repository: undefined
```

This value is not defined anywhere in the role.  I have documented it here because it is a value usually defined in the [elastic.elasticsearch](https://github.com/elastic/ansible-elasticsearch) role by [Elastic.co](https://www.elastic.co/).  If you are installing this Kibana role alongside the `elastic.elasticsearch` role, then that role will typically install the repository for you.  Allowing this Kibana role to also install the repository will slightly alter the repo file which leads to the role no longer producing an idempotent result.  However, if you tell the `elastic.elasticsearch` role NOT to install the repository, then this Kibana role *will* install the repository in order to access the software.

```yaml
es_version: "6.2.3"
```

The full version number of Elasticsearch/Kibana.

```yaml
kibana_enabled: "yes"
```

This defines whether the Kibana service should be enabled at boot.

```yaml
kibana_params: {}
```

The `kibana_params` variable is a dictionary that can contain custom settings that you wish to modify within the Kibana configuration file.  The key name of dictionary entry should match the setting you wish to see in the configuration file, and the value of the dictionary entry should match the parameter value you wish to set.

(e.g. `kibana_params: { server.name: "{{ ansible_fqdn }}" }`).

```yaml
kibana_repo_key: 'https://artifacts.elastic.co/GPG-KEY-elasticsearch'
```

The URL to the PGP key used for the [Elastic.co](https://www.elastic.co/) respository.

```yaml
kibana_run_state: started
```

This defines whether the Kibana service should be started.

### RedHat specific values (see `vars/kibana-RedHat.yml`)

```yaml
kibana_home: /usr/share/kibana
```

The path where Kibana is installed.

```yaml
kibana_bin_dir: "{{ kibana_home }}/bin"
```

The path where the Kibana binary is installed.

```yaml
kibana_config_dir: "/etc/kibana"
```

The path to the Kibana configuration directory.

```yaml
kibana_config_file: "{{ kibana_config_dir }}/kibana.yml"
```

The full path to the Kibana configuration file.

```yaml
kibana_data_dir: /var/lib/kibana
```

The path where Kibana data is stored.

```yaml
kibana_optimize_dir: "{{ kibana_home }}/optimize"
```

The path to the Kibana optimize directory where it stores transpiled source code.

```yaml
kibana_plugins_dir: "{{ kibana_home }}/plugins"
```

The path to the Kibana plugins directory.


## Dependencies

None.

## Example Playbook

```yaml
- hosts: servers
  roles:
     - role: javiergayala.kibana
       kibana_params:
         'server.name': "{{ ansible_fqdn }}"
```

## License

BSD

## Author Information

This role was created in 2018 by [Javier Ayala](http://www.javierayala.com/).
