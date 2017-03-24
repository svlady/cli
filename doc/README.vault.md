## GitLab CLI configuration

The CLI tool requires two parameters for accessing GitLab API endpoint:

* `VAULT_API` - the API endpoint URL
* `VAULT_TOKEN` - the authentication token issued by the Vault user. Your API calls will be impersonated as this user, who issued the token. Obviously, the user must be given sufficient permissions for performing management actions on Vault objects.

These parameters are usually provided as shell environment variables. Make sure that your VAULT_TOKEN is well protected, it's a key to your secure credential storage.

```shell
VAULT_API=https://vault.local:8200/v1
VAULT_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxx
export VAULT_API VAULT_TOKEN
```

You can perform this configuration once in your current shell or add these variables to your shell or environment intialization files.

## CLI Usage

The CLI tool is operating on _objects_ identified by their key (or key-path to be precise) by calling _actions_ for those _objects_.

```shell
$ ./vault
Hashicorp Vault CLI
Usage: ./vault <action> <key path> [<value>]

<key path> - the key path in the secure storage, has the following format
             /<key>/.../<path> and can be up to 128 chars long. Currently
             all keys are put under /secret prefix.
<value>    - the value string can be up to 1024 chars long and may contain
             any ASCII characters but double-quotes.

Supported actions:
    list (dir) <key path>
    get (read) <key path>
    del (drop) <key path>
    put (set) <key path> <value>

```

## Examples

The CLI tool usage is pretty straightforward and below you can see several examples for performing basic management actions.

### Browse Vault keys

```shell
$ ./vault list /secret/cli
gitlab/
mysql/
sonar/
ldap/
$ ./vault list /secret/cli/ldap
binddn
bindpw
$
```
### Fetch key value

```shell
$ ./vault get /secret/cli/ldap/binddn
CN=adtool,CN=Service Accounts,OU=HOSTING,DC=LOCAL
$
```

### Adding Sonar token to Vault

```shell
$ ./vault put /secret/cli/sonar/token 0de845da1a8d5453454343f9480dab73b3104fcdcc
$
```
