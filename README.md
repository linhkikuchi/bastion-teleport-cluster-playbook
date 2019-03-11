### Gravitational Teleport: a modern SSH system for managing privileged access across clusters of Linux servers, where multiple users can join the same session or re-play the session later
More info: https://gravitational.com/teleport

### Playbook for setting up teleport auth and proxy servers
- Teleport has 2 clusters running: operations and general. 
- Cluster general is connected to cluster operations as a trusted cluster
- bastion-auth has 2 auth services running, operations on port 3025 and general on port 3026
- bastion-proxy has 2 proxy service running, operations on port 443 & general on port 8443
- bastion-proxy has LDAP set up
- to run tctl on auth servers
```tctl -c /etc/teleport/operations.yaml users add monkey
tctl -c /etc/teleport/general.yaml users add banana```
- to restart the services on auth/proxy servers
```systemctl restart teleport-operations
systemctl restart teleport-general```
 

### To build bastion server, run
 ansible-playbook -i bastion.hosts bastion.yml -u root --vault-password-file ~/.vault_pass