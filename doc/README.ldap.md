## LDAP CLI configuration

The CLI tool requires several parameters for its function

* `LDAP_URI` - the URI for accessing your LDAP/AD server
* `LDAP_BASE` - the BASE dn is the point from where LDAP server will search for users and other objects
* `LDAP_EXT` - the EXT dn has a similar function as BASE dn and used to separate "internally" (placed under BASE dn) and "externally" (placed under EXT dn) scoped LDAP objects for separating management concerns
* `LDAP_BINDDN` - the DN used for LDAP bind (authentication) operation
* `LDAP_BINDPW` - the password used for LDAP bind

These parameters are usually provided as shell environment variables. However, for additional security, you may want to fetch the bind password from Vault. For this you need to have Vault up and running. See configuration example inside the `ldap` script, in comments.

```shell
LDAP_URI="ldaps://hosting.local"
LDAP_BASE="OU=HOSTING,DC=LOCAL"
LDAP_EXT="OU=EXT,${LDAP_BASE}"
LDAP_BINDDN="CN=adtool,CN=Service Accounts,OU=HOSTING,DC=LOCAL"
LDAP_BINDPW="xxxxxxxxxxxxxxx"
export LDAP_URI LDAP_BASE LDAP_EXT LDAP_BINDDN LDAP_BINDPW
```

You can perform this configuration once in your current shell or add these variables to your shell or environment intialization files.

## Setting up shell auto-completion

The corresponding `.auto` file contains shell auto-completion function, which is providing hints and simplifies command line entry a great deal. For activation just source provided file as shown in the example below. Alternatively, you can setup auto-completion permanently by adding this command to your shell initialization script or otherwise setup autocompletion as described in your distribution documentation.

```shell
$ source ldap.auto # replace 'source' with '.' (no quotes) if you tired typing, those two are synonyms 
```

## CLI Usage

The CLI tool is operating on _objects_ by calling _actions_ for those _objects_. For each _action_ the user may provide additional input parameters. Some _actions_ also supporting the `--format` output parameter, which is specifying resulting output format.

```shell
$ ./ldap
LDAP/AD CLI management tool
Usage: ./ldap <object> <action> [<args 1> ... <arg N>]
Objects and actions:
    group <list|add|del|users|adduser|deluser> <args...>
        list (dir)   [--org <org name>] [--format <short|long>]
        add (create) [--org <org name>] --group <group name>
        del (remove) [--org <org name>] --group <group name>
        users (members)   --group <group name> [--format <short|long>]
        adduser (useradd) --group <group name> --org <org name> --name <user name>
        deluser (userdel) --group <group name> --org <org name> --name <user name>

    org <list|add|del> <args...>
        list (dir) [--pattern <pattern *>] [--format <short|long>]
        add (create) --org <org name>
        del (remove) --org <org name>

    user <list|add|del> <args...>
        groups (memberof) [--org <org name>] --name <user name> [--format <short|long>]
        list (dir)   [--org <org name>] [--container <container>] [--format <short|long>]
        add (create) [--org <org name>] [--container <container>] --first <first name> --last <last name>
                     --login <login name> --mail <email> --password <password>
        del (remove) [--org <org name>] --name <user name>
        getattr --org <org name> --name <user name> --attr <attribute name>
        setattr --org <org name> --name <user name> --attr <attribute name> --value <attr value>

```

## Examples

The CLI tool usage is pretty straightforward and below you can see several examples for performing basic management actions.

### List LDAP groups

```shell
$ ./ldap group list
GitLab Users
Sonar Administrators
Sonar Users
Jenkins Users
Jenkins Job Managers
Jenkins Administrators
Content Editors
Content Authors
Content Publishers
CMS Administrators
$
```

Results displayed as a list of records by default. The next command changes output format to more detailed.

```shell
$ ./ldap group list --format long
CN=GitLab Users,CN=Groups,OU=HOSTING,DC=LOCAL
CN=Sonar Administrators,CN=Groups,OU=HOSTING,DC=LOCAL
CN=Sonar Users,CN=Groups,OU=HOSTING,DC=LOCAL
CN=Jenkins Users,CN=Groups,OU=HOSTING,DC=LOCAL
CN=Jenkins Job Managers,CN=Groups,OU=HOSTING,DC=LOCAL
CN=Jenkins Administrators,CN=Groups,OU=HOSTING,DC=LOCAL
CN=Content Editors,CN=Groups,OU=HOSTING,DC=LOCAL
CN=Content Authors,CN=Groups,OU=HOSTING,DC=LOCAL
CN=Content Publishers,CN=Groups,OU=HOSTING,DC=LOCAL
CN=CMS Administrators,CN=Groups,OU=HOSTING,DC=LOCAL
$
```

### Add new LDAP group

```shell
$ ./ldap group add --group "DevOps Users"
ldap: successfully added group "DevOps Users"
$
```

### Add new LDAP account

```shell
$ ./ldap user add --first John --last Dev --login jdev --mail jdev@company.com --password '...user password...'
ldap: successfully added user jdev : "John Dev"
ldap: set password for user "John Dev"
ldap: unlocked user "John Dev"
ldap: setting AD attributes for user "John Dev"
$
```

### List user groups

```shell
$ ./ldap user groups --name "John Doe"
Content Editors
Sonar Users
GitLab Users
$
```
