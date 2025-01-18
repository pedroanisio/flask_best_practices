# Meta Directory

## Overview
The `meta` directory contains configurations and templates for setting up and managing the project using Ansible.

## Structure
```
meta/
│── ansible/                 # Ansible playbooks and configurations
│── templates/               # Jinja2 templates used by Ansible
│   └── Dockerfile.j2        # Jinja2 template for generating Dockerfile
│── README.md                # This documentation
```

## Usage
1. **Ensure Ansible is installed**:
   ```sh
   sudo apt install ansible  # On Ubuntu/Debian
   brew install ansible      # On macOS
   ```

2. **Run the Ansible playbook to generate the Dockerfile**:
   ```sh
   ansible-playbook meta/playbooks/configure_project.yaml
   ```

3. **Verify the generated Dockerfile**:
   ```sh
   cat ../Dockerfile
   ```

## Customization
You can modify the `meta/templates/Dockerfile.j2` template to customize the Dockerfile according to your needs.

### Variables
The Jinja2 template uses the following variables:
- `project_name`: Name of the project
- `python_version`: Python version to use
- `timezone`: Timezone setting for the container

Modify these values in the Ansible playbook (`generate_dockerfile.yml`) under the `vars` section.

## Notes
- Ensure that the `meta/ansible/` directory has the correct permissions to execute the playbook.
- If running on a remote server, configure Ansible's inventory file accordingly.

## Support
For any issues, feel free to raise an issue in the project repository.

Install 
ansible-galaxy collection install community.crypto